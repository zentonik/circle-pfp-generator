# Circle PFP Generator

# Overview

This Python script is a versatile tool for transforming images into circular profile pictures with customizable borders. The script downloads an image from a specified URL, resizes it, and applies a circular mask to create a clean, circular profile picture. The result is then saved as a PNG image with a transparent background.

# Features

Image Loading: Utilizes the load_image_from_url function to download an image from a given URL and returns a Pillow Image object.

Circular Profile Picture Creation: The core functionality is provided by the create_circle_pfp function, which performs the following steps:

Resizes the input image to the specified diameter.

Creates a new image with a transparent background.

Draws a circle on the transparent background.

Pastes the resized image onto the circle.

Draws a customizable border around the circle.

Utilizes a mask to remove everything outside the circular region.

Saves the result as a PNG image with transparency.

# Instructions

Replace image_url with the URL of the image you want to use.

Specify the desired output_path where the resulting image will be saved.

Tweak parameters such as diameter and border_width as needed.

# Libraries

PIL (Pillow)

Matplotlib

Requests



