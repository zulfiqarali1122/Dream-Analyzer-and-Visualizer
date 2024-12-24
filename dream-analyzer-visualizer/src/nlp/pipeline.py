from src.nlp.theme_extractor import extract_themes
from src.nlp.sentiment_analysis import analyze_sentiment
from src.nlp.categorization import categorize_dream
import sys
import os

# Add the project directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)

from src.nlp.theme_extractor import extract_themes
from src.nlp.sentiment_analysis import analyze_sentiment
from src.nlp.categorization import categorize_dream


def process_dream(dream_description):
    """
    Processes a dream description through the NLP pipeline.

    Args:
        dream_description (str): The textual description of a dream.

    Returns:
        dict: A dictionary containing the results of the pipeline.
    """
    # Extract themes
    themes = extract_themes(dream_description)
    
    # Analyze sentiment
    sentiment = analyze_sentiment(dream_description)
    
    # Categorize dream
    category = categorize_dream(dream_description)
    
    # Combine all results
    results = {
        "themes": themes,
        "sentiment": sentiment,
        "category": category
    }
    
    return results

# Example usage
if __name__ == "__main__":
    dream = "I was flying over a stormy ocean at sunset, feeling a mix of fear and wonder."
    results = process_dream(dream)
    print("Dream Analysis Results:")
    print(results)
