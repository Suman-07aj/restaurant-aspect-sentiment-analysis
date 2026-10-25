"""
Streamlit Application for Aspect-Based Sentiment Analysis of Restaurant Reviews.
"""

import streamlit as st
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import torch and transformer first to prevent Windows DLL initialization conflicts (WinError 1114 with c10.dll)
try:
    import torch
    from transformer import predict_sentiment as transformer_predict
    TRANSFORMER_AVAILABLE = True
except (ImportError, OSError) as e:
    print(f"Warning: Could not import transformer model: {e}")
    transformer_predict = None
    TRANSFORMER_AVAILABLE = False

from baseline import predict_sentiment as baseline_predict
import joblib

# Page configuration
st.set_page_config(
    page_title="Aspect-Based Sentiment Analysis",
    page_icon="🍽️",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
    }
    .result-box {
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .result-box h2 {
        color: inherit !important;
        font-weight: 700 !important;
    }
    .positive {
        background-color: #d4edda;
        border: 2px solid #28a745;
        color: #155724 !important;
    }
    .negative {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
        color: #721c24 !important;
    }
    .neutral {
        background-color: #fff3cd;
        border: 2px solid #ffc107;
        color: #856404 !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🍽️ Aspect-Based Sentiment Analysis</h1>
        <h2>Restaurant Reviews</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Check which models are available
    models_dir = os.path.join(os.path.dirname(__file__), 'models')
    baseline_model_path = os.path.join(models_dir, 'baseline_model.joblib')
    baseline_vectorizer_path = os.path.join(models_dir, 'tfidf_vectorizer.joblib')
    transformer_model_path = os.path.join(models_dir, 'transformer_model')
    transformer_tokenizer_path = os.path.join(models_dir, 'transformer_tokenizer')
    
    # Check baseline model
    baseline_available = os.path.exists(baseline_model_path) and os.path.exists(baseline_vectorizer_path)
    
    # Check transformer model
    transformer_available = (TRANSFORMER_AVAILABLE and 
                            os.path.exists(transformer_model_path) and 
                            os.path.exists(transformer_tokenizer_path))
    
    if not baseline_available:
        st.error("⚠️ Baseline model not found! Please run `python src/baseline.py` to train the model first.")
        st.stop()
    
    # Load baseline model
    try:
        baseline_model = joblib.load(baseline_model_path)
        baseline_vectorizer = joblib.load(baseline_vectorizer_path)
    except Exception as e:
        st.error(f"⚠️ Error loading baseline model: {e}")
        st.stop()
    
    # Load transformer model if available
    transformer_model = None
    transformer_tokenizer = None
    if transformer_available:
        try:
            from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
            transformer_model = DistilBertForSequenceClassification.from_pretrained(transformer_model_path)
            transformer_tokenizer = DistilBertTokenizer.from_pretrained(transformer_tokenizer_path)
            transformer_model.eval()
        except Exception as e:
            st.warning(f"⚠️ Warning: Could not load transformer model: {e}")
            transformer_available = False
    
    # Input section
    st.subheader("Enter Review and Aspect")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        review = st.text_area(
            "Review",
            placeholder="The food was amazing but the service was very slow.",
            height=100,
            max_chars=1000
        )
    
    with col2:
        aspect = st.text_input(
            "Aspect",
            placeholder="food, service, ambience, price...",
            max_chars=50
        )
    
    # Model selector
    model_options = ["TF-IDF + Logistic Regression"]
    if transformer_available:
        model_options.append("DistilBERT")
    
    model_choice = st.selectbox(
        "Select Model",
        model_options
    )
    
    # Analyze button
    analyze_button = st.button("🔍 Analyze Sentiment", type="primary", use_container_width=True)
    
    # Edge case handling and prediction
    if analyze_button:
        # Validate inputs
        if not review or not review.strip():
            st.warning("⚠️ Please enter a review.")
            st.stop()
        
        if not aspect or not aspect.strip():
            st.warning("⚠️ Please enter an aspect.")
            st.stop()
        
        if len(review) > 1000:
            st.warning("⚠️ Review is too long. Please keep it under 1000 characters.")
            st.stop()
        
        if len(aspect) > 50:
            st.warning("⚠️ Aspect is too long. Please keep it under 50 characters.")
            st.stop()
        
        # Check if aspect is present in review (warning only)
        aspect_lower = aspect.lower()
        review_lower = review.lower()
        if aspect_lower not in review_lower:
            st.info(f"ℹ️ Note: The aspect '{aspect}' does not appear to be mentioned in the review. The prediction may be less accurate.")
        
        # Make prediction based on selected model
        try:
            with st.spinner("Analyzing sentiment..."):
                if model_choice == "TF-IDF + Logistic Regression":
                    result = baseline_predict(review, aspect, baseline_model, baseline_vectorizer)
                elif model_choice == "DistilBERT":
                    if not TRANSFORMER_AVAILABLE or transformer_predict is None:
                        st.error("⚠️ Transformer model is not available due to PyTorch DLL error. Please use the baseline model.")
                        st.stop()
                    result = transformer_predict(review, aspect, transformer_model, transformer_tokenizer)
                else:
                    st.error("⚠️ Invalid model selection")
                    st.stop()
            
            # Display results
            st.markdown("---")
            st.subheader("Prediction")
            
            sentiment = result['sentiment']
            confidence = result['confidence']
            
            # Color-coded result box
            if sentiment == "Positive":
                emoji = "🟢"
                css_class = "positive"
            elif sentiment == "Negative":
                emoji = "🔴"
                css_class = "negative"
            else:
                emoji = "🟡"
                css_class = "neutral"
            
            st.markdown(f"""
            <div class="result-box {css_class}">
                <h2 style="text-align: center; margin: 0; color: inherit !important;">{emoji} {sentiment.upper()}</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Confidence and model info
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Confidence", f"{confidence:.1f}%")
            with col2:
                st.metric("Model", model_choice)
            
            # Show probability breakdown
            st.markdown("---")
            st.subheader("Probability Breakdown")
            
            probs = result['probabilities']
            for label, prob in probs.items():
                p_val = float(prob)
                if p_val > 1.0:
                    p_val = p_val / 100.0
                p_val = min(max(p_val, 0.0), 1.0)
                try:
                    st.progress(p_val, text=f"{label}: {p_val*100:.1f}%")
                except TypeError:
                    st.write(f"**{label}**: {p_val*100:.1f}%")
                    st.progress(p_val)
            
        except Exception as e:
            st.error(f"⚠️ Error during prediction: {e}")
    
    # Example section
    st.markdown("---")
    st.subheader("Example Reviews")
    
    with st.expander("Click to see example inputs"):
        st.markdown("""
        **Example 1:**
        - Review: "The food was amazing but the service was very slow."
        - Aspect: food
        - Expected: Positive
        
        **Example 2:**
        - Review: "The food was amazing but the service was very slow."
        - Aspect: service
        - Expected: Negative
        
        **Example 3:**
        - Review: "The pasta was perfectly cooked and flavorful."
        - Aspect: food
        - Expected: Positive
        
        **Example 4:**
        - Review: "The service was terrible and disorganized."
        - Aspect: service
        - Expected: Negative
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em;">
        <p>Aspect-Based Sentiment Analysis System | College NLP Micro-Project</p>
        <p>Uses TF-IDF + Logistic Regression for sentiment classification</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
