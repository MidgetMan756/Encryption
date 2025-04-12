import base64 as b64
from PIL import Image, ImageDraw
import math
import random

import color as clr

def string_to_base64(string):
    stringBytes = string.encode('utf-8')
    base64Bytes = b64.b64encode(stringBytes)
    base64String = base64Bytes.decode('utf-8')
    return base64String

def string_to_binary(string):
    binary = ' '.join(format(ord(char), '08b') for char in string)
    return binary

def create_binary_image(binary_string, square_size=20, output_file="binary_image.png"):
    # Calculate dimensions of the square grid
    num_bits = len(binary_string)
    grid_size = math.ceil(math.sqrt(num_bits))  # Determine size of square (width = height)
    
    # Create a new blank image
    image = Image.new("RGB", (grid_size * square_size, grid_size * square_size), "white")
    draw = ImageDraw.Draw(image)
    
    # Draw squares for each binary bit
    for i, bit in enumerate(binary_string):
        row = i // grid_size  # Determine the row
        col = i % grid_size   # Determine the column
        
        # Determine the color for each bit
        if bit == '0':
            color = random.randint(1,3)
            match color:
                case 1:
                    color = clr.Red
                case 2:
                    color = clr.Yellow
                case 3:
                    color = clr.Blue
        elif bit == '1':
            color = random.randint(1,3)
            match color:
                case 1:
                    color = clr.Orange
                case 2:
                    color = clr.Green
                case 3:
                    color = clr.Purple
        elif bit == ' ':  
            color = clr.Black
        else:
            continue  # Ignore invalid characters
        
        # Calculate square coordinates
        x0 = col * square_size
        y0 = row * square_size
        x1 = x0 + square_size
        y1 = y0 + square_size
        
        # Draw the square
        draw.rectangle([x0, y0, x1, y1], fill=color, outline=(127, 127, 127, 0))
    
    # Save the image
    image.save(output_file)
    print(f"Binary image saved as {output_file}")