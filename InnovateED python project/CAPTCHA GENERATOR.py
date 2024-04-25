import random
from PIL import Image, ImageDraw, ImageFont
import string

def generate_captcha(width, height, length=6, font_size=30):
    # Generate random string for captcha
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    # Create blank image
    image = Image.new('RGB', (width, height), color = (255, 255, 255))

    # Choose a font
    font = ImageFont.truetype("arial.ttf", font_size)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Calculate text size and position
    text_width, text_height = draw.textsize(captcha_text, font)
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Add text to the image
    draw.text((x, y), captcha_text, fill=(0, 0, 0), font=font)

    # Add noise
    for _ in range(500):
        draw.point((random.randint(0, width), random.randint(0, height)), fill=(0, 0, 0))

    # Save the image as PNG format
    image.save("captcha.png")

    return captcha_text

# Example usage
captcha_text = generate_captcha(200, 100)
print("CAPTCHA text:", captcha_text)
