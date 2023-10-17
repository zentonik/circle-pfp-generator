from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import requests
from io import BytesIO

def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def create_circle_pfp(image, output_path, diameter=300, border_width=6):
    
    img = image.resize((diameter, diameter), Image.LANCZOS)

    
    mask = Image.new("L", (diameter, diameter), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((border_width, border_width, diameter - border_width, diameter - border_width), fill=255)

    
    result_img = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))
    result_img.paste(img, (0, 0), mask)

    
    result_img.save(output_path)
    result_img.show()


image_url = "https://imagelink"
output_path = "circle_pfp.png"

image = load_image_from_url(image_url)
create_circle_pfp(image, output_path)
