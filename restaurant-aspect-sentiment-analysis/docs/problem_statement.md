# Problem Statement

## Problem

Traditional sentiment analysis provides an overall sentiment score for a review, but restaurant reviews often contain mixed opinions about different aspects (food, service, ambience, price). A customer may love the food but hate the service, and overall sentiment analysis fails to capture this nuance.

## Objective

Build an Aspect-Based Sentiment Analysis (ABSA) system that predicts sentiment for a specific aspect within a restaurant review.

## Formal Definition

Given:
- A review R (text)
- An aspect A (e.g., "food", "service", "ambience", "price")

Predict:
- Y ∈ {Positive, Neutral, Negative}

## Application

The system can be used by:
- Restaurant owners to identify specific areas for improvement
- Review platforms to provide more granular feedback
- Customers to quickly find reviews relevant to their interests
- Market researchers to analyze sentiment trends across aspects

## Input

1. **Review Text**: A natural language review of a restaurant
   - Example: "The food was amazing but the service was very slow."
   
2. **Aspect**: A specific aspect to analyze
   - Example: "food", "service", "ambience", "price"

## Output

Sentiment label with confidence:
- Positive
- Neutral
- Negative

Example:
```
Review: "The food was amazing but the service was very slow."
Aspect: food
Output: Positive (Confidence: 92%)

Review: "The food was amazing but the service was very slow."
Aspect: service
Output: Negative (Confidence: 95%)
```

## Target Users

1. **Restaurant Owners/Managers**: Identify specific strengths and weaknesses
2. **Review Platforms**: Enhance review analysis capabilities
3. **Customers**: Filter reviews by aspect of interest
4. **Researchers**: Study aspect-level sentiment patterns

## Real-World Need

Restaurant reviews are inherently multi-faceted. A single review can contain positive sentiment about food but negative sentiment about service. Overall sentiment analysis loses this granularity, making it difficult for businesses to take targeted action. ABSA provides the fine-grained analysis needed for actionable insights.

## Scope

This project focuses on:
- Restaurant reviews only (not other product categories)
- Pre-defined aspects (food, service, ambience, price)
- English language reviews
- Three sentiment classes: Positive, Neutral, Negative
- Supervised learning approach with labeled data

## Assumptions

1. The aspect is provided by the user (not automatically extracted)
2. Reviews are in English
3. The dataset is representative of restaurant reviews
4. Sentiment is expressed explicitly in the text
5. The aspect mentioned is relevant to the review

## Measurable Success Criteria

1. **Classification Performance**: Achieve reasonable accuracy on test set
   - Target: Accuracy > 70% on test set (based on baseline performance in literature)
   
2. **Model Comparison**: Successfully compare baseline and transformer models
   - Document accuracy, precision, recall, F1-score for both models
   - Provide comparison table
   
3. **Working Inference Application**: Functional Streamlit application
   - Accepts review and aspect input
   - Returns sentiment prediction with confidence
   - Handles edge cases gracefully
   
4. **Edge Case Handling**: Correct handling of invalid inputs
   - Empty review/aspect
   - Very long inputs
   - Aspect not present in review
   - Unknown/OOV words
   - Non-English text (with appropriate message)
   
5. **Error Analysis**: Identify at least 10 actual failure cases
   - Categorize errors by type
   - Provide analysis for each
   
6. **Documentation**: Complete documentation for all requirements
   - Problem statement ✓
   - Dataset documentation
   - Architecture diagram
   - Technology justification
   - Literature survey
   - Evaluation results

## Limitations

1. Aspect extraction is not automated (user must provide aspect)
2. Limited to English language
3. Demo dataset size is small (38 samples for demonstration)
4. No GPU available (CPU-only training)
5. Transformer model training may be slow on CPU
6. Does not handle implicit sentiment well
7. May struggle with sarcasm and complex linguistic phenomena
