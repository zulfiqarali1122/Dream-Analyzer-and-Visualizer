import cv2
import numpy as np
import os

def create_video_from_images(image_paths, output_path, fps=24):
    """
    Create a video from a list of image paths.

    Args:
        image_paths (list): List of paths to images.
        output_path (str): Path to save the output video.
        fps (int): Frames per second for the video.
    """
    # Read the first image to get dimensions
    first_image = cv2.imread(image_paths[0])
    height, width, _ = first_image.shape

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Add each image to the video
    for image_path in image_paths:
        img = cv2.imread(image_path)
        out.write(img)

    # Release video writer
    out.release()
    print(f"Video saved to {output_path}")

def add_text_frame(text, output_path, width=1024, height=1024, duration=5, fps=24):
    """
    Create a frame with text overlay.

    Args:
        text (str): The text to display.
        output_path (str): Path to save the text frame image.
        width (int): Width of the frame.
        height (int): Height of the frame.
        duration (int): Duration of the frame in seconds.
        fps (int): Frames per second.
    """
    # Create a black frame
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Add text to the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    color = (255, 255, 255)  # White text
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2

    cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, thickness)

    # Save the frame for specified duration
    for _ in range(fps * duration):
        cv2.imwrite(output_path, frame)
