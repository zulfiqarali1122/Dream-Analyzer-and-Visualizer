 
from textblob import TextBlob

def analyze_sentiment(dream_description):
    """
    Analyzes the sentiment of a given dream description.

    Args:
        dream_description (str): The textual description of a dream.
        
    Returns:
        dict: A dictionary containing sentiment polarity and subjectivity.
    """
    blob = TextBlob(dream_description)
    
    # Sentiment polarity ranges from -1 (negative) to 1 (positive)
    # Subjectivity ranges from 0 (objective) to 1 (subjective)
    sentiment = {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    }
    
    return sentiment

# Example usage
if __name__ == "__main__":
    dream = "I was flying over a stormy ocean at sunset, feeling a mix of fear and wonder."
    sentiment = analyze_sentiment(dream)
    print("Sentiment Analysis:", sentiment)
