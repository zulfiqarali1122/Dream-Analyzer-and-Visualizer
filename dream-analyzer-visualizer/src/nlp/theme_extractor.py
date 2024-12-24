 
import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")  # Make sure to install this model with: python -m spacy download en_core_web_sm

def extract_themes(dream_description):
    """
    Extracts key themes from a given dream description.
    
    Args:
        dream_description (str): The textual description of a dream.
        
    Returns:
        dict: A dictionary with extracted entities and keywords.
    """
    # Process the text
    doc = nlp(dream_description)
    
    # Extract named entities
    entities = [ent.text for ent in doc.ents]
    
    # Extract nouns and verbs (potential themes)
    keywords = [token.text for token in doc if token.pos_ in ("NOUN", "VERB") and not token.is_stop]
    
    return {
        "entities": entities,
        "keywords": keywords
    }

# Example usage
if __name__ == "__main__":
    dream = "I was flying over a stormy ocean at sunset, feeling a mix of fear and wonder."
    themes = extract_themes(dream)
    print("Extracted Themes:", themes)
