 
def categorize_dream(dream_description):
    """
    Categorizes a dream description into predefined categories.

    Args:
        dream_description (str): The textual description of a dream.

    Returns:
        str: The category of the dream.
    """
    # Predefined categories with keywords
    categories = {
        "Adventure": ["travel", "journey", "explore", "mountain", "ocean"],
        "Nightmare": ["fear", "chase", "monster", "dark", "death"],
        "Fantasy": ["magic", "castle", "dragon", "fairy", "wizard"],
        "Romance": ["love", "kiss", "wedding", "heart", "relationship"],
        "Mystery": ["hidden", "secret", "unknown", "puzzle", "clue"]
    }

    # Lowercase the dream description for easier matching
    dream_description_lower = dream_description.lower()

    # Check for keywords in the description
    for category, keywords in categories.items():
        if any(keyword in dream_description_lower for keyword in keywords):
            return category

    # Default category if no match is found
    return "Uncategorized"

# Example usage
if __name__ == "__main__":
    dream = "I was exploring a magical forest with a hidden castle guarded by a dragon."
    category = categorize_dream(dream)
    print("Dream Category:", category)
