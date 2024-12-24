 
# **Dream Analyzer and Visualizer**

A Python-based application that analyzes and visualizes user-submitted dream descriptions. The application extracts themes, analyzes sentiment, and generates ultra-realistic visualizations based on the dreams using Stable Diffusion.

---

## **Features**
- **Dream Analysis**:
  - Extracts key themes and keywords from the dream description.
  - Categorizes the dream (e.g., "Adventure", "Fantasy", etc.).
  - Analyzes the sentiment (polarity and subjectivity).
  
- **Dream Visualization**:
  - Generates realistic images based on the extracted themes using the Stable Diffusion model.
  - Combines the generated images into a video, offering a cinematic representation of the dream.

---

## **Tech Stack**
- **Programming Language**: Python
- **Natural Language Processing**:
  - SpaCy
  - TextBlob
- **Visualization**:
  - Diffusers (Stable Diffusion)
  - OpenCV
- **Video Creation**:
  - OpenCV
  - NumPy
- **Framework**: Hugging Face Diffusers for image generation

---

## **Setup and Installation**

### Prerequisites
1. Python 3.8 or higher
2. CUDA-compatible GPU (optional for faster processing)
3. Stable Diffusion model dependencies installed via Hugging Face's Diffusers library

### Installation
1. Clone the repository or download the project files:

Usage Instructions
Run the Application:
Execute the following command to start the dream analyzer and visualizer application:

bash
Copy code
python -m src.app
Provide a Dream Description:
When prompted, enter a brief description of your dream. Example:

css
Copy code
I was floating above a tranquil ocean, the sun setting in the distance, and I felt completely at ease.
Analysis and Visualization:

The application will:
Analyze the dream description to extract themes, sentiment, and category.
Generate ultra-realistic images for the dream themes using Stable Diffusion.
Create a cinematic video combining these images.
Generated Outputs:

Images will be saved in the assets/ folder.
The final video will be saved as dream_visualization.mp4 in the project directory.
Example Workflow
Input Dream:

css
Copy code
I walked through a dense, misty forest, illuminated by soft moonlight. The air was cool and full of whispers.
Output:

Themes Extracted: ["forest", "misty", "moonlight", "cool", "whispers"]
Sentiment:
Polarity: 0.12 (Positive)
Subjectivity: 0.45
Category: Mystery
Video:
A cinematic depiction of a misty forest under moonlight, featuring cool tones and mysterious ambiance.
