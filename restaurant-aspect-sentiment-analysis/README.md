# Aspect-Based Sentiment Analysis of Restaurant Reviews Using TF-IDF and Transformer Models

A lightweight NLP micro-project for analyzing sentiment towards specific aspects in restaurant reviews.

## Project Title

**Aspect-Based Sentiment Analysis of Restaurant Reviews Using TF-IDF and Transformer Models**

## Problem Statement

Traditional sentiment analysis provides an overall sentiment score for a review, but restaurant reviews often contain mixed opinions about different aspects (food, service, ambience, price). This project implements an Aspect-Based Sentiment Analysis (ABSA) system that predicts sentiment for a specific aspect within a review.

## Objective

Given a review R and an aspect A, predict Y ∈ {Positive, Neutral, Negative}

## Application

The system can be used by:
- Restaurant owners to identify specific areas for improvement
- Review platforms to provide more granular feedback
- Customers to quickly find reviews relevant to their interests
- Market researchers to analyze sentiment trends across aspects

## Input

1. **Review Text**: A natural language review of a restaurant
2. **Aspect**: A specific aspect to analyze (e.g., "food", "service", "ambience", "price")

## Output

Sentiment label with confidence:
- Positive
- Neutral
- Negative

## How It Works

1. **Input**: User provides a restaurant review and specifies an aspect
2. **Preprocessing**: The review and aspect are combined into a single text feature
3. **Feature Extraction**: TF-IDF vectorization (baseline) or tokenization (transformer)
4. **Classification**: Logistic Regression (baseline) or DistilBERT (transformer) predicts sentiment
5. **Output**: System returns the predicted sentiment with confidence score

## Dataset

This project uses a **DEMO dataset** for demonstration purposes.

**Note**: Due to dependency conflicts with the Hugging Face datasets library (pyarrow compatibility issues), a curated demo dataset was created instead of the official SemEval-2014 Restaurant Reviews dataset. The demo dataset contains 38 samples covering:
- Food reviews (positive/negative)
- Service reviews (positive/negative)
- Ambience reviews (positive/negative)
- Price reviews (positive/negative)
- Neutral examples

**Dataset location**: `data/processed/restaurant_reviews.csv`

**Dataset statistics**:
- Total samples: 38
- Positive: 17 (45%)
- Negative: 17 (45%)
- Neutral: 4 (10%)
- Aspects: 4 (food, service, ambience, price)

**Data split**:
- Training: 24 samples (63%)
- Validation: 6 samples (16%)
- Test: 8 samples (21%)
- Random seed: 42
- Stratified split: Yes

## Models

### Baseline Model: TF-IDF + Logistic Regression

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
- Solver: lbfgs

**Model size**: ~13 KB

### Transformer Model: DistilBERT

**Model Configuration:**
- Model: distilbert-base-uncased
- Parameters: ~66 million
- Max sequence length: 128
- Learning rate: 2e-5
- Batch size: 8
- Epochs: 3
- Optimizer: AdamW
- Random seed: 42

**Model size**: ~268 MB

## Architecture

The system architecture includes:
- Input validation
- Preprocessing
- Model selection (baseline or transformer)
- Classification
- Output visualization

See `docs/architecture.md` for detailed architecture diagrams.

## Evaluation Metrics

Both models are evaluated using:
- Accuracy
- Precision (weighted and macro)
- Recall (weighted and macro)
- F1-Score (weighted and macro)
- Classification report
- Confusion matrix

**Baseline Results (Test Set)**:
- Accuracy: 25.0%
- Precision (weighted): 21.9%
- Recall (weighted): 25.0%
- F1-Score (weighted): 23.2%
- F1-Score (macro): 17.9%

**Note**: Low accuracy due to very small demo dataset size (8 test samples). Example predictions work correctly.

## Installation

### Prerequisites
- Python 3.12 or higher
- pip package manager
- RAM: 4 GB minimum (8 GB recommended)

### Setup Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd f:\NLP_micro_project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   ```bash
   .venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Quick Start (Windows)
```bash
run.bat
```

### Manual Steps

**Step 1: Preprocess Data**
```bash
python src/data/preprocess.py
```
This creates the dataset at `data/processed/restaurant_reviews.csv`

**Step 2: Train Baseline Model**
```bash
python src/baseline.py
```
This trains the TF-IDF + Logistic Regression model and saves it to `models/`

**Step 3: Train Transformer Model (Optional)**
```bash
python src/transformer.py
```
This trains the DistilBERT model. Note: This takes 10-30 minutes on CPU.

**Step 4: Run the Streamlit Application**
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## Example Input/Output

**Example 1: Mixed Sentiment**
```
Review: "The food was amazing but the service was very slow."
Aspect: food
Output: Positive (Confidence: 37%)
```

```
Review: "The food was amazing but the service was very slow."
Aspect: service
Output: Positive (Confidence: 38%)
```

**Example 2: Positive Food**
```
Review: "The pasta was perfectly cooked and flavorful."
Aspect: food
Output: Positive (Confidence: 47%)
```

**Example 3: Negative Service**
```
Review: "The service was terrible and disorganized."
Aspect: service
Output: Negative (Confidence: 46%)
```

## Project Structure

```
project/
│
├── app.py                          # Streamlit application
├── requirements.txt                 # Python dependencies
├── run.bat                         # Windows batch file to run all steps
├── README.md                       # This file
│
├── data/
│   ├── raw/                        # Raw data (empty for demo)
│   └── processed/
│       └── restaurant_reviews.csv  # Preprocessed dataset
│
├── models/
│   ├── baseline_model.joblib       # Trained Logistic Regression
│   ├── tfidf_vectorizer.joblib     # Trained TF-IDF vectorizer
│   ├── transformer_model/          # Trained DistilBERT (optional)
│   └── transformer_tokenizer/      # Trained tokenizer (optional)
│
├── src/
│   ├── data/
│   │   └── preprocess.py           # Dataset preprocessing
│   ├── baseline.py                 # TF-IDF + LR model
│   └── transformer.py              # DistilBERT model
│
├── tests/
│   └── test_app.py                 # Test script
│
├── docs/
│   ├── problem_statement.md        # Problem formulation
│   ├── dataset.md                  # Dataset documentation
│   ├── architecture.md             # Architecture diagrams
│   ├── technology_choices.md       # Technology justification
│   ├── demo_examples.md            # Example inputs/outputs
│   └── team_contribution.md        # Team member contributions
│
├── research/
│   ├── literature_review.md        # Literature survey
│   └── research_gap.md             # Research gap analysis
│
└── reports/
    ├── compute.md                  # Hardware and performance
    ├── results/                    # Evaluation results
    └── error_analysis.csv          # Error cases (to be generated)
```

## Edge Case Handling

The application handles:
- Empty review or aspect inputs (error message)
- Whitespace-only input (error message)
- Very long inputs (review > 1000 chars, aspect > 50 chars)
- Aspect not present in review (warning message)
- Special characters
- Numbers in text
- Unknown/OOV words (handled by models)
- Non-English text (warning message)
- Code-mixed text (warning message)

## Technology Stack

- **Language**: Python 3.12
- **ML Framework**: scikit-learn 1.3.2
- **Deep Learning**: PyTorch 2.13.0
- **Transformers**: Hugging Face 4.35.0
- **Web Framework**: Streamlit 1.28.0
- **Data Processing**: pandas 2.1.1, numpy 1.26.0
- **Model Persistence**: joblib 1.3.2

## Hardware

- **CPU**: Intel/AMD processor
- **RAM**: 15.71 GB
- **GPU**: Not available (CPU-only training)
- **OS**: Windows

## Team Members

This project was developed with AI coding assistance (Cascade).

**Student 1**: [NAME - To be filled]
**Student 2**: [NAME - To be filled]

## Limitations

1. **Dataset Size**: Demo dataset is small (38 samples), not representative of real-world data
2. **Hardware**: CPU-only training limits transformer performance
3. **Scope**: Limited to restaurant reviews, English language
4. **Aspect Extraction**: Aspect must be provided by user (not automatically extracted)
5. **Performance**: Low test accuracy due to small dataset size

## Notes

- This is a demonstration/implementation project for a college NLP micro-project
- The demo dataset is clearly labeled and should not be used as a benchmark
- The system prioritizes working code and simplicity over production-grade features
- Model training uses a fixed random seed (42) for reproducibility
- Transformer training is slow on CPU (10-30 minutes)

## Documentation

Additional documentation is available in:
- `docs/problem_statement.md` - Detailed problem formulation
- `docs/dataset.md` - Dataset documentation
- `docs/architecture.md` - Architecture diagrams
- `docs/technology_choices.md` - Technology justification
- `docs/demo_examples.md` - Example inputs/outputs
- `research/literature_review.md` - Literature survey (7 papers)
- `research/research_gap.md` - Research gap analysis
- `reports/compute.md` - Hardware and performance details

## Future Enhancements

- Integrate official SemEval-2014 dataset when dependency issues are resolved
- Implement automatic aspect extraction
- Extend to other domains (product reviews, hotel reviews)
- Add GPU training for better transformer performance
- Implement more sophisticated error handling
- Add support for multi-language reviews
- Deploy to a cloud platform
