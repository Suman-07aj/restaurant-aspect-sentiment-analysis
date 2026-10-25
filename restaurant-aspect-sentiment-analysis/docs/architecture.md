# Architecture Diagram

## System Architecture for Aspect-Based Sentiment Analysis

### Overall Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                          USER INPUT                              │
├─────────────────────────────────────────────────────────────────┤
│  Review: "The food was amazing but the service was very slow."  │
│  Aspect: "food"                                                  │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    INPUT VALIDATION                              │
├─────────────────────────────────────────────────────────────────┤
│  - Check empty review/aspect                                    │
│  - Check input length                                           │
│  - Check aspect presence in review                              │
│  - Handle special characters                                    │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PREPROCESSING                                 │
├─────────────────────────────────────────────────────────────────┤
│  Format: "[ASPECT] aspect [TEXT] review" (Baseline)             │
│  Format: "review [SEP] aspect" (Transformer)                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   MODEL SELECTION    │
              └──────────┬───────────┘
                         │
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
┌──────────────────────┐      ┌──────────────────────┐
│   BASELINE MODEL     │      │  TRANSFORMER MODEL   │
│  TF-IDF + LR         │      │  DistilBERT          │
└──────────┬───────────┘      └──────────┬───────────┘
           │                               │
           ▼                               ▼
┌──────────────────────┐      ┌──────────────────────┐
│  TF-IDF              │      │  Tokenizer           │
│  Vectorization       │      │  Encoding            │
└──────────┬───────────┘      └──────────┬───────────┘
           │                               │
           ▼                               ▼
┌──────────────────────┐      ┌──────────────────────┐
│  Logistic Regression │      │  DistilBERT          │
│  Classifier          │      │  Encoder             │
└──────────┬───────────┘      └──────────┬───────────┘
           │                               │
           └───────────────┬───────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      OUTPUT                                      │
├─────────────────────────────────────────────────────────────────┤
│  Sentiment: Positive / Negative / Neutral                       │
│  Confidence: XX%                                                 │
│  Model: [Selected Model]                                        │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                   STREAMLIT UI                                   │
├─────────────────────────────────────────────────────────────────┤
│  Display prediction, confidence, probability breakdown          │
└─────────────────────────────────────────────────────────────────┘
```

### TF-IDF + Logistic Regression Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                          USER INPUT                              │
├─────────────────────────────────────────────────────────────────┤
│  Review: "The food was amazing but the service was very slow."  │
│  Aspect: "food"                                                  │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      PREPROCESSING                               │
├─────────────────────────────────────────────────────────────────┤
│  Combine review + aspect into single text:                      │
│  "[ASPECT] food [TEXT] The food was amazing but the service..." │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      TF-IDF VECTORIZATION                        │
├─────────────────────────────────────────────────────────────────┤
│  - Convert text to numerical features                           │
│  - Max features: 5000                                            │
│  - N-gram range: (1, 2)                                         │
│  - Stop words: English                                          │
│  - Output: Sparse matrix (samples × features)                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                 LOGISTIC REGRESSION CLASSIFIER                   │
├─────────────────────────────────────────────────────────────────┤
│  - Multi-class classification (Positive, Negative, Neutral)     │
│  - Max iterations: 1000                                         │
│  - Class weights: balanced                                      │
│  - Output: Sentiment class + probability scores                 │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      OUTPUT                                      │
├─────────────────────────────────────────────────────────────────┤
│  Sentiment: Positive                                            │
│  Confidence: 92%                                                │
│  Model: TF-IDF + Logistic Regression                            │
└─────────────────────────────────────────────────────────────────┘
```

### DistilBERT Transformer Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                          USER INPUT                              │
├─────────────────────────────────────────────────────────────────┤
│  Review: "The food was amazing but the service was very slow."  │
│  Aspect: "food"                                                  │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      PREPROCESSING                               │
├─────────────────────────────────────────────────────────────────┤
│  Combine review + aspect with separator:                        │
│  "The food was amazing but the service was very slow. [SEP] food"│
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      TOKENIZATION                                 │
├─────────────────────────────────────────────────────────────────┤
│  - DistilBERT tokenizer                                         │
│  - Add special tokens ([CLS], [SEP])                            │
│  - Max length: 128                                              │
│  - Padding and truncation                                       │
│  - Output: Input IDs, Attention Mask                            │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   DISTILBERT ENCODER                             │
├─────────────────────────────────────────────────────────────────┤
│  - Pre-trained transformer layers                               │
│  - Self-attention mechanism                                     │
│  - Contextual word representations                              │
│  - Output: Hidden states                                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              CLASSIFICATION HEAD                                 │
├─────────────────────────────────────────────────────────────────┤
│  - Linear layer on [CLS] token                                  │
│  - 3 output classes (Positive, Negative, Neutral)              │
│  - Softmax activation                                           │
│  - Output: Class probabilities                                  │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      OUTPUT                                      │
├─────────────────────────────────────────────────────────────────┤
│  Sentiment: Positive                                            │
│  Confidence: 95%                                                │
│  Model: DistilBERT                                              │
└─────────────────────────────────────────────────────────────────┘
```

### Streamlit Application Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    STREAMLIT INTERFACE                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐                      │
│  │   Review Input   │  │   Aspect Input  │                      │
│  └────────┬────────┘  └────────┬────────┘                      │
│           │                    │                                 │
│           └──────────┬─────────┘                                 │
│                      ▼                                           │
│           ┌──────────────────────┐                               │
│           │  Analyze Button      │                               │
│           └──────────┬───────────┘                               │
│                      ▼                                           │
│           ┌──────────────────────┐                               │
│           │  Input Validation    │                               │
│           │  - Empty check       │                               │
│           │  - Length check      │                               │
│           │  - Aspect presence   │                               │
│           └──────────┬───────────┘                               │
│                      ▼                                           │
│           ┌──────────────────────┐                               │
│           │  Load Model          │                               │
│           │  (baseline_model.joblib)                             │
│           └──────────┬───────────┘                               │
│                      ▼                                           │
│           ┌──────────────────────┐                               │
│           │  Predict Sentiment   │                               │
│           └──────────┬───────────┘                               │
│                      ▼                                           │
│           ┌──────────────────────┐                               │
│           │  Display Results     │                               │
│           │  - Sentiment label   │                               │
│           │  - Confidence score  │                               │
│           │  - Probability breakdown                           │
│           └──────────────────────┘                               │
└─────────────────────────────────────────────────────────────────┘
```

### Model Training Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    TRAINING PIPELINE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────┐                                          │
│  │  Raw Dataset     │                                          │
│  │  (CSV file)      │                                          │
│  └────────┬─────────┘                                          │
│           │                                                     │
│           ▼                                                     │
│  ┌──────────────────┐                                          │
│  │  Preprocessing   │                                          │
│  │  - Combine text  │                                          │
│  │  - Format:       │                                          │
│  │    [ASPECT]...   │                                          │
│  └────────┬─────────┘                                          │
│           │                                                     │
│           ▼                                                     │
│  ┌──────────────────┐                                          │
│  │  Train-Test     │                                          │
│  │  Split (80-20)   │                                          │
│  │  Stratified     │                                          │
│  └────────┬─────────┘                                          │
│           │                                                     │
│           ▼                                                     │
│  ┌──────────────────┐                                          │
│  │  TF-IDF Fit      │                                          │
│  │  (Training only) │                                          │
│  └────────┬─────────┘                                          │
│           │                                                     │
│           ▼                                                     │
│  ┌──────────────────┐                                          │
│  │  LR Training     │                                          │
│  │  (Training only) │                                          │
│  └────────┬─────────┘                                          │
│           │                                                     │
│           ▼                                                     │
│  ┌──────────────────┐                                          │
│  │  Evaluation      │                                          │
│  │  - Accuracy      │                                          │
│  │  - Precision     │                                          │
│  │  - Recall        │                                          │
│  │  - F1-Score      │                                          │
│  └────────┬─────────┘                                          │
│           │                                                     │
│           ▼                                                     │
│  ┌──────────────────┐                                          │
│  │  Save Models     │                                          │
│  │  - .joblib files │                                          │
│  └──────────────────┘                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### File Structure

```
project/
│
├── app.py                          # Streamlit application
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
│
├── data/
│   └── processed/
│       └── restaurant_reviews.csv  # Preprocessed dataset
│
├── models/
│   ├── baseline_model.joblib       # Trained Logistic Regression
│   └── tfidf_vectorizer.joblib     # Trained TF-IDF vectorizer
│
├── src/
│   ├── preprocess.py               # Dataset preprocessing
│   ├── baseline.py                 # TF-IDF + LR model
│   └── transformer.py              # (Optional) Transformer model
│
└── docs/
    └── architecture.md             # This architecture diagram
```

### Key Components

1. **Data Preprocessing** (`src/preprocess.py`)
   - Downloads/prepares restaurant review dataset
   - Formats data as (review, aspect, sentiment)
   - Saves to CSV for model training

2. **Baseline Model** (`src/baseline.py`)
   - TF-IDF vectorization
   - Logistic Regression classifier
   - Model training and evaluation
   - Prediction function for inference

3. **Streamlit App** (`app.py`)
   - User interface for input
   - Input validation and edge case handling
   - Model loading and prediction
   - Result visualization

4. **Model Artifacts** (`models/`)
   - `baseline_model.joblib`: Trained classifier
   - `tfidf_vectorizer.joblib`: Fitted vectorizer

### Technology Stack

- **Language**: Python 3.12
- **ML Framework**: scikit-learn
- **Web Framework**: Streamlit
- **Data Processing**: pandas, numpy
- **Model Persistence**: joblib

### Model Specifications

**TF-IDF Vectorizer:**
- Max features: 5000
- N-gram range: (1, 2)
- Stop words: English
- Lowercase: True

**Logistic Regression:**
- Max iterations: 1000
- Random state: 42
- Class weights: balanced
- Multi-class: One-vs-Rest

### Performance Metrics

The model is evaluated using:
- Accuracy
- Precision (weighted)
- Recall (weighted)
- F1-Score (weighted)

Metrics are computed on a held-out test set (20% of data).
