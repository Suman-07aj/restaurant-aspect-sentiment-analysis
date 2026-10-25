# Technology Choices

## Why Python?

**Reason**: Python is the de facto standard for NLP and machine learning.

**Justification**:
- Extensive library ecosystem (scikit-learn, PyTorch, transformers)
- Simple and readable syntax
- Strong community support
- Excellent documentation
- Widely used in both academia and industry

## Why scikit-learn?

**Reason**: Robust, well-documented classical ML library.

**Justification**:
- Provides efficient implementations of TF-IDF and Logistic Regression
- Easy to use API
- Built-in evaluation metrics
- Well-suited for baseline models
- Industry-standard for classical ML

## Why TF-IDF?

**Reason**: Simple, effective text representation for baseline.

**Justification**:
- Captures word importance through frequency
- Computationally efficient
- Works well for sentiment analysis
- Interpretable features
- No pre-training required
- Good baseline for comparison with transformers

## Why Logistic Regression?

**Reason**: Simple, interpretable classifier for baseline.

**Justification**:
- Fast training and inference
- Provides probability estimates (confidence scores)
- Works well with high-dimensional sparse features (TF-IDF)
- Interpretable coefficients
- Handles multi-class classification
- Good baseline performance for text classification

## Why DistilBERT?

**Reason**: Lightweight transformer model with good performance.

**Justification**:
- Smaller and faster than BERT (40% fewer parameters)
- Retains 97% of BERT's performance
- Suitable for CPU training (though slow)
- Pre-trained on large corpus (good language understanding)
- State-of-the-art for NLP tasks
- Provides contextual word representations
- Handles aspect-context relationships better than TF-IDF

## Why Hugging Face Transformers?

**Reason**: Standard library for transformer models.

**Justification**:
- Easy model loading and fine-tuning
- Pre-trained models readily available
- Consistent API across models
- Active development and support
- Tokenizer integration
- Compatible with PyTorch

## Why Streamlit?

**Reason**: Simple, Python-based web framework for ML demos.

**Justification**:
- Pure Python (no HTML/CSS/JavaScript required)
- Fast development
- Built-in UI components
- Easy deployment
- Good for interactive ML demos
- Supports real-time inference
- Suitable for college project demonstrations

## Why Macro F1?

**Reason**: Handles class imbalance better than weighted F1.

**Justification**:
- Treats all classes equally
- Not biased towards majority class
- Standard metric for multi-class classification
- Required by faculty
- More informative for imbalanced datasets
- Fair comparison across models

## Why SEED=42?

**Reason**: Reproducibility of experiments.

**Justification**:
- Standard practice in ML research
- Ensures same data splits across runs
- Enables fair comparison
- Debugging easier with deterministic behavior
- Required for scientific rigor
- Common convention (answer to life, universe, everything)

## Why Joblib?

**Reason**: Efficient model serialization.

**Justification**:
- Optimized for numpy arrays
- Faster than pickle for large objects
- Standard for scikit-learn model persistence
- Simple API
- Compatible with scikit-learn

## Why Train/Validation/Test Split?

**Reason**: Proper evaluation methodology.

**Justification**:
- **Training set**: Model learning
- **Validation set**: Hyperparameter tuning, early stopping
- **Test set**: Final evaluation (unseen data)
- Prevents data leakage
- Standard ML practice
- Required for credible results

## Why Stratified Split?

**Reason**: Maintains class distribution across splits.

**Justification**:
- Ensures each split has similar class distribution
- Important for imbalanced datasets
- Prevents bias in evaluation
- Standard practice for classification

## Why Class Weights?

**Reason**: Handles class imbalance in training.

**Justification**:
- Gives more weight to minority classes
- Prevents model from being biased towards majority class
- Built-in feature of Logistic Regression
- Simple and effective
- Alternative to oversampling/undersampling

## Technology Stack Summary

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| Language | Python | 3.12 | Implementation |
| ML Framework | scikit-learn | 1.3.2 | Baseline model |
| Deep Learning | PyTorch | 2.13.0 | Transformer |
| Transformers | Hugging Face | 4.35.0 | DistilBERT |
| Web Framework | Streamlit | 1.28.0 | UI |
| Data Processing | pandas | 2.1.1 | Data handling |
| Numerical Computing | numpy | 1.26.0 | Arrays |
| Model Persistence | joblib | 1.3.2 | Saving models |
| Progress Bars | tqdm | 4.66.1 | Training visualization |

## Hardware Considerations

**Current Setup**:
- CPU: Intel/AMD processor (no GPU available)
- RAM: 15.71 GB
- Training: CPU-only (slow for transformers)

**Impact**:
- Baseline (TF-IDF + LR): Fast (< 1 minute)
- Transformer (DistilBERT): Slow (10-30 minutes on CPU)
- Inference: Fast for both models

**Future Improvements**:
- GPU would accelerate transformer training significantly
- Cloud training (Colab, AWS) for faster results
