# Demo Examples

This document contains example inputs and expected outputs for the Aspect-Based Sentiment Analysis system.

## Example 1: Mixed Sentiment (Different Aspects)

**Review**: "The food was amazing but the service was very slow."

**Aspect**: food
**Expected**: Positive
**Reasoning**: The review explicitly states "food was amazing"

**Aspect**: service
**Expected**: Negative
**Reasoning**: The review explicitly states "service was very slow"

---

## Example 2: Positive Food

**Review**: "The pasta was perfectly cooked and flavorful."

**Aspect**: food
**Expected**: Positive
**Reasoning**: "perfectly cooked" and "flavorful" are positive descriptors

---

## Example 3: Negative Service

**Review**: "The service was terrible and disorganized."

**Aspect**: service
**Expected**: Negative
**Reasoning**: "terrible" and "disorganized" are negative descriptors

---

## Example 4: Positive Ambience

**Review**: "The ambience was cozy and romantic."

**Aspect**: ambience
**Expected**: Positive
**Reasoning**: "cozy" and "romantic" are positive descriptors

---

## Example 5: Negative Price

**Review**: "The prices were too high for the quality."

**Aspect**: price
**Expected**: Negative
**Reasoning**: "too high" indicates negative sentiment about price

---

## Example 6: Neutral Statement

**Review**: "The food was okay, nothing special."

**Aspect**: food
**Expected**: Neutral
**Reasoning**: "okay" and "nothing special" indicate neutral sentiment

---

## Example 7: Positive Price

**Review**: "Great value for the money."

**Aspect**: price
**Expected**: Positive
**Reasoning**: "Great value" indicates positive sentiment about price

---

## Example 8: Negative Food

**Review**: "The seafood smelled bad."

**Aspect**: food
**Expected**: Negative
**Reasoning**: "smelled bad" is clearly negative

---

## Example 9: Positive Service

**Review**: "The staff was friendly and helpful."

**Aspect**: service
**Expected**: Positive
**Reasoning**: "friendly" and "helpful" are positive descriptors

---

## Example 10: Negative Ambience

**Review**: "The restaurant was too crowded and uncomfortable."

**Aspect**: ambience
**Expected**: Negative
**Reasoning**: "crowded" and "uncomfortable" are negative descriptors

---

## Edge Case Examples

### Edge Case 1: Aspect Not in Review

**Review**: "The food was delicious."
**Aspect**: service
**Expected**: Model should still make a prediction, but may be less accurate
**Note**: System should warn user that aspect is not mentioned

### Edge Case 2: Very Long Review

**Review**: "The food was absolutely amazing, the best I've ever had in my entire life. The flavors were perfectly balanced and the presentation was beautiful. However, the service left much to be be desired. We waited for over an hour for our appetizers and the waiter seemed completely disinterested in helping us. The ambience was nice though, with soft lighting and pleasant music."
**Aspect**: food
**Expected**: Positive
**Note**: System should handle long input gracefully

### Edge Case 3: Empty Input

**Review**: ""
**Aspect": food
**Expected**: Error message "Please enter a review"

### Edge Case 4: Empty Aspect

**Review**: "The food was good."
**Aspect**: ""
**Expected**: Error message "Please enter an aspect"

### Edge Case 5: Mixed Sentiment for Same Aspect

**Review**: "The food was good but the pasta was overcooked."
**Aspect**: food
**Expected**: Could be Positive or Neutral depending on model interpretation
**Note**: This is a challenging case for aspect-based sentiment analysis

---

## Usage in Demo

For the live demonstration, use these recommended examples:

1. **Showcase mixed sentiment**: Example 1 (food vs service)
2. **Show positive**: Example 2 or 3
3. **Show negative**: Example 4 or 5
4. **Show neutral**: Example 6
5. **Show edge case handling**: Edge Case 1 or 2

These examples demonstrate:
- Different aspects (food, service, ambience, price)
- Different sentiments (Positive, Negative, Neutral)
- Mixed sentiment in single review
- Edge case handling
