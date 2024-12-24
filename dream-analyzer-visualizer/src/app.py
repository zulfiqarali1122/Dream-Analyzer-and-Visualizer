from src.nlp.theme_extractor import extract_themes
from src.nlp.sentiment_analysis import analyze_sentiment
from src.nlp.categorization import categorize_dream
from src.visualization.image_generator import generate_image_from_theme
from src.visualization.video_generator import create_video_from_images, add_text_frame

def get_user_dream():
    # Ask the user for their dream description
    dream = input("Enter your dream description: ")
    return dream

def process_dream(dream):
    # Process the dream description
    themes = extract_themes(dream)
    sentiment = analyze_sentiment(dream)
    category = categorize_dream(dream)
    return {'themes': themes, 'sentiment': sentiment, 'category': category}

def main():
    print("Welcome to the Dream Analyzer and Visualizer!")
    
    # Get the dream description from the user
    dream_description = input("Enter your dream description: ")

    # Process the dream using the pipeline
    dream_analysis = process_dream(dream_description)

    # Output the analysis results
    print("Dream Analysis Results:", dream_analysis)

    # Generate images based on dream themes
    image_paths = []
    for idx, theme in enumerate(dream_analysis['themes']):
        image_path = f"assets/generated_images/theme_{idx}.png"
        generate_image_from_theme(theme, image_path)
        image_paths.append(image_path)

    # Add a text frame for the intro
    intro_text = (f"Dream Category: {dream_analysis['category']}\n"
                  f"Sentiment: Polarity={dream_analysis['sentiment']['polarity']}, "
                  f"Subjectivity={dream_analysis['sentiment']['subjectivity']}")
    text_frame_path = "assets/generated_images/intro_frame.png"
    add_text_frame(intro_text, text_frame_path)
    image_paths.insert(0, text_frame_path)

    # Generate a video from the images
    output_video_path = "dream_video.mp4"
    create_video_from_images(image_paths, output_video_path)

    print("Dream visualization video generated successfully!")

if __name__ == "__main__":
    main()
