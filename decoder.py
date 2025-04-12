from PIL import Image
import base64 as b64

import color as clr

def image_to_binary_text(image_file, square_size=20):
    # Open the image
    image = Image.open(image_file)
    pixels = image.load()
    
    # Get the dimensions of the image
    width, height = image.size
    grid_size = width // square_size  # Number of squares per row
    
    # Initialize an empty result string
    result = ""
    
    # Loop through each square in the grid
    for row in range(height // square_size):
        for col in range(grid_size):
            # Calculate the top-left pixel of the current square
            x = (col * square_size) + 1
            y = (row * square_size) + 1
            
            # Get the color of the pixel (we sample the top-left corner of each square)
            r, g, b = pixels[x, y]
            
            # Map the color back to the corresponding character
            if (r, g, b) == clr.Red or (r, g, b) == clr.Yellow or (r, g, b) == clr.Blue:         # Primary → '0'
                result += "0"
            elif (r, g, b) == clr.Orange or (r, g, b) == clr.Green or (r, g, b) == clr.Purple:   # Secondary → '1'
                result += "1"
            elif (r, g, b) == clr.Black:                                                         # Black → space
                result += " "
            else:
                continue  # Ignore any other unexpected colors
    
    return result

def binary_to_string(binary_string):
    # Split the binary string into chunks of 8 bits (separated by space)
    binary_values = binary_string.split()
    
    # Convert each binary chunk to an integer, then to its corresponding ASCII character
    decoded_characters = []
    
    for b in binary_values:
        if len(b) > 8:  # Special case for '='
            decoded_characters.append("=")
        else:
            decoded_characters.append(chr(int(b, 2)))
    
    # Join the characters to form the final string
    return ''.join(decoded_characters)


def base64_to_string(string):
    base64Bytes = string.encode('utf-8')
    originalBytes = b64.b64decode(base64Bytes)
    decodedString = originalBytes.decode('utf-8')
    return decodedString