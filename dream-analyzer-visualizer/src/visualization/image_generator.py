from diffusers import StableDiffusionPipeline
import torch
import os

def generate_image_from_theme(theme, output_path):
    """
    Generate an image based on a theme using Stable Diffusion.

    Args:
        theme (str): The theme or description for the image.
        output_path (str): The file path to save the generated image.
    """
    # Load the Stable Diffusion model
    model_id = "CompVis/stable-diffusion-v1-4"  # Or another model you prefer
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    # Generate an image based on the theme
    prompt = f"A cinematic depiction of {theme}, ultra-realistic, beautiful scene, 4K resolution"
    image = pipe(prompt).images[0]

    # Save the generated image
    image.save(output_path)
    print(f"Image saved to {output_path}")

# Example Usage
# generate_image_from_theme("a tranquil forest lake during sunset", "output_image.png")
