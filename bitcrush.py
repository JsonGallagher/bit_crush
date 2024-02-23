from PIL import Image, ImageChops, ImageFilter
import numpy as np
import os

def psychedelic_effect(image_path, output_dir):
    # Open the original image
    img = Image.open(image_path)
    
    # Apply a mild blur to soften the image
    # img = img.filter(ImageFilter.GaussianBlur(2))
    
    # Separate the color channels
    r, g, b = img.split()
    
    # Apply channel shifts
    r = ImageChops.offset(r, -250, 0)  # Shift red channel
    g = ImageChops.offset(g, -250, 0)  # Shift green channel in the opposite direction
    b = ImageChops.offset(g, -20, 0)  # Shift blue channel in the opposite direction
    
    # Recombine the channels
    img_psychedelic = Image.merge('RGB', (r, g, b))
    
    # Apply wave distortion with a more subtle effect
    np_img = np.array(img_psychedelic)
    x = np.arange(np_img.shape[1])

    # Reduce the amplitude and adjust the frequency for a more subtle effect
    y = np.sin(x / 30.0) * 10  # Increasing the divisor will spread the waves out more, decreasing the amplitude makes the effect subtler
    
    for i in range(np_img.shape[0]):
        np_img[i] = np.roll(np_img[i], int(y[i % x.shape[0]]), axis=0)
    
    img_psychedelic = Image.fromarray(np_img)
    
    # Generate unique output filename
    output_filename = generate_unique_filename(output_dir, 'image-crushed', 'jpeg')
    
    # Save the psychedelic image
    img_psychedelic.save(output_filename)

def generate_unique_filename(output_dir, base_filename, extension):
    counter = 1
    while True:
        output_filename = os.path.join(output_dir, f"{base_filename}-{counter:03d}.{extension}")
        if not os.path.exists(output_filename):
            return output_filename
        counter += 1

# Update these paths for your specific use case
image_path = "/Users/bgmarketing/Desktop/bit_crush/image.jpg"
output_dir = "/Users/bgmarketing/Desktop/bit_crush/outputs"

psychedelic_effect(image_path, output_dir)
