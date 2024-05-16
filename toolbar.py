import os
from cairosvg import svg2png
from PIL import Image, ImageDraw
import json

def combine_images(json_file, output_filename):
  with open(json_file, "r") as f:
    image_paths = json.load(f)

  images = []
  # Process images based on extension
  for path in image_paths:
    try:
      if path.lower().endswith(".svg"):
        # Use CairoSVG for SVG images
        temp_file = f"{path}.png"
        svg2png(url=path, write_to=temp_file, dpi=72)  # Adjust DPI if needed
        image = Image.open(temp_file)
      else:
        # Use Pillow for other image formats
        image = Image.open(path)
      image = image.convert("RGBA")
      resized_image = image.resize((16, 16), Image.LANCZOS)
      images.append(resized_image)
      if path.lower().endswith(".svg"):
        os.remove(temp_file)  # Clean up temporary file for SVGs
    except FileNotFoundError:
      print(f"Error: File not found - {path}")
    except Exception as e:
      print(f"Error processing image: {path} ({e})")

  # Combine images
  if images:
    total_width = 16 * len(images) 
    total_height = max(image.height for image in images)
    combined_image = Image.new("RGBA", (total_width, total_height))
    draw = ImageDraw.Draw(combined_image)
    x_offset = 0
    for image in images:
      combined_image.paste(image, (x_offset, 0))
      x_offset += image.width

    # Save the combined image
    combined_image.save(output_filename)
    print(f"Toolbar bitmap strip saved to: {output_filename}")
  else:
    print("No valid images found. Please check your JSON file.")
    
combine_images("toolbar.json", "toolbar.png")
