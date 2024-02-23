# Python Photo Manipulation Project

This Python project allows you to apply psychedelic effects to images using various techniques such as channel shifts and wave distortions.

## Features

- Apply channel shifts to create psychedelic effects
- Soften the image with Gaussian blur (commented out by default)
- Apply wave distortion for a psychedelic wave effect

## Requirements

- Python 3.x
- Pillow (Python Imaging Library, `pip install pillow`)
- NumPy (`pip install numpy`)

## Usage

1. Clone the repository or download the `psychedelic.py` script.

2. Ensure you have Python 3.x installed on your system.

3. Install the required dependencies using pip:

   ```bash
   pip install pillow numpy
   ```

4. Run the script with the following command:

   ```python
   python psychedelic.py
   ```

5. Follow the instructions provided by the script to apply psychedelic effects to your images.

## Sample Usage

You can replace `image_path` and `output_path` variables in the script with your desired image input and output paths.

```python
image_path = "/path/to/your/image.jpg"
output_path = "/path/to/save/psychedelic_image.jpg"

psychedelic_effect(image_path, output_path)
```

## Contributors

- [Jason Gallagher](https://github.com/JsonGallagher)

## License

This project is licensed under the MIT License 