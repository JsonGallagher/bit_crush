from PIL import Image, ImageChops, ImageFilter
import numpy as np

def psychedelic_effect(image_path, output_path):
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
    
    # Apply wave distortion with a more susource venv/bin/activatebtle effect
    np_img = np.array(img_psychedelic)
    x = np.arange(np_img.shape[1])

    # Reduce the amplitude and adjust the frequency for a more subtle effect
    y = np.sin(x / 30.0) * 10  # Increasing the divisor will spread the waves out more, decreasing the amplitude makes the effect subtler
    
    for i in range(np_img.shape[0]):
        np_img[i] = np.roll(np_img[i], int(y[i % x.shape[0]]), axis=0)
    
    img_psychedelic = Image.fromarray(np_img)
    
    # Save the psychedelic image
    img_psychedelic.save(output_path)

# Update these paths for your specific use case
image_path = "/Users/bgmarketing/Desktop/bit_crush/img_polaroid.jpg"
output_path = "/Users/bgmarketing/Desktop/bit_crush/img_polaroid-crushed.jpeg"

psychedelic_effect(image_path, output_path)
