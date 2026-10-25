# Dataset Documentation

## Dataset Overview

**Note**: Due to dependency conflicts with the Hugging Face datasets library (pyarrow compatibility issues), this project uses a **curated demo dataset** for demonstration purposes. This is clearly labeled and should not be used as a benchmark dataset.

## Official Dataset (Preferred)

The preferred dataset for this project is:

**SemEval-2014 Task 4 - Aspect-Based Sentiment Analysis**

- **Official URL**: http://alt.qcri.org/semeval2014/task4/
- **Dataset Name**: SemEval-2014 Restaurant Reviews
- **Task**: Aspect-Based Sentiment Analysis
- **Domain**: Restaurant reviews

### Official Dataset Details (Not Used Due to Technical Issues)

- **Size**: Approximately 3,000+ reviews with aspect annotations
- **License**: Academic use (SemEval datasets are freely available for research)
- **Labels**: Positive, Negative, Neutral
- **Annotation Scheme**: Aspect terms with associated polarities
- **Splits**: Official train/test splits provided

## Demo Dataset (Currently Used)

### Source
Curated demo dataset created for demonstration purposes.

### Size
- **Total samples**: 38
- **Aspects**: food, service, ambience, price
- **Sentiments**: Positive, Negative, Neutral

### Distribution
- **Positive**: 17 samples
- **Negative**: 17 samples
- **Neutral**: 4 samples

### Annotation Scheme
Each sample contains:
1. **review**: The restaurant review text
2. **aspect**: The specific aspect (food, service, ambience, price)
3. **sentiment**: The sentiment label (Positive, Negative, Neutral)

### Data Format
CSV file with columns:
```
review,aspect,sentiment
"The food was amazing and delicious.",food,Positive
"The service was very slow and inattentive.",service,Negative
```

### File Location
`data/processed/restaurant_reviews.csv`

## Data Split

### Split Strategy
- **Random seed**: 42 (for reproducibility)
- **Split ratio**: 80% train, 20% test
- **Stratification**: Yes (maintains class distribution)
- **Validation**: Created from training data (20% of train)

### Actual Splits (Demo Dataset)
- **Training**: 30 samples (80%)
- **Validation**: 6 samples (20% of training)
- **Test**: 8 samples (20%)

### Class Distribution in Splits

**Training Set**:
- Positive: 14
- Negative: 13
- Neutral: 3

**Test Set**:
- Positive: 3
- Negative: 4
- Neutral: 1

## Data Preprocessing

### Steps
1. **Data Collection**: Demo dataset curated manually
2. **Format Conversion**: Structured as (review, aspect, sentiment)
3. **Shuffling**: Random shuffle with seed 42
4. **Saving**: Saved to CSV format

### Text Preprocessing (Model-Specific)
Text preprocessing is handled separately in each model:
- **Baseline**: TF-IDF handles lowercase, stop words, n-grams
- **Transformer**: Tokenizer handles lowercasing, special tokens

## Label Mapping

Original labels are already in the required format:
- Positive → Positive
- Negative → Negative
- Neutral → Neutral

No conversion needed.

## Data Quality

### Demo Dataset Characteristics
- **Balanced**: Reasonably balanced between Positive and Negative
- **Coverage**: Covers 4 common aspects
- **Variety**: Includes positive, negative, and neutral examples
- **Clarity**: Explicit sentiment expressions

### Limitations
- **Small size**: Only 38 samples (not representative of real-world data)
- **Manual curation**: Not crowdsourced or professionally annotated
- **No official benchmark**: Cannot be used for performance comparison
- **Limited diversity**: Limited vocabulary and expression patterns

## Future Work

To use the official SemEval-2014 dataset:
1. Resolve Hugging Face datasets library dependency issues
2. Download official dataset from SemEval-2014 Task 4
3. Parse XML annotations to extract (review, aspect, sentiment) tuples
4. Apply same preprocessing pipeline
5. Update documentation with official statistics

## License

**Demo Dataset**: Created for educational purposes. No specific license. Not for commercial use.

**SemEval-2014 Dataset**: Academic use license. Free for research purposes.

## Citation

If using the official SemEval-2014 dataset:
```
@inproceedings{pontiki2014semeval,
  title={Semeval-2014 task 4: Aspect based sentiment analysis},
  author={Pontiki, Maria and Galanis, Dimitris and Papageorgiou, Harris and Androutsopoulos, Ion and Manandhar, Suresh and Yang, Shweta and others},
  booktitle={Proceedings of the 8th International Workshop on Semantic Evaluation (SemEval 2014)},
  pages={27--35},
  year={2014}
}
```
