# Sketchify 🎨

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An image-to-pencil-sketch converter using computer vision techniques. Transforms any image into a realistic pencil sketch through grayscale conversion, inversion, Gaussian blur, and division blending.

---

## Project Statistics 📊

- **4 processing steps** (Grayscale → Inversion → Blur → Division Blending)
- **3 intermediate visualizations** (Grayscale, Inverted, Final Sketch)
- **Adjustable sketch intensity** (default: 220.0)
- **Automatic aspect ratio preservation** (max 800x600)
- **21x21 Gaussian kernel** for smooth blur effect
- **Real-time processing** (near-instant for standard images)

---

## Project Overview 🎯

Sketchify is a learning project built while exploring computer vision, image processing, and OpenCV. It demonstrates fundamental image processing techniques to create artistic pencil sketch effects from photographs.

### Development Context
- Built as a hands-on learning project for computer vision and image processing
- Explores OpenCV's image manipulation capabilities
- Demonstrates practical application of grayscale conversion, inversion, and blending techniques
- Foundation for understanding digital image processing algorithms

### What I Learned
- Grayscale conversion and color space manipulation
- Image inversion techniques
- Gaussian blur for noise reduction
- Division blending for sketch effects
- Aspect ratio preservation during resizing
- OpenCV window management and display

---

## How It Works 🔧

The sketch conversion process involves 4 key steps:

1. **Grayscale Conversion**
   - Converts RGB image to grayscale
   - Reduces color information to intensity values

2. **Image Inversion**
   - Inverts pixel values (255 - pixel_value)
   - Creates negative effect

3. **Gaussian Blur**
   - Applies 21x21 Gaussian kernel
   - Smooths inverted image
   - Reduces noise and creates soft edges

4. **Division Blending**
   - Divides grayscale by inverted blur
   - Scale factor: 220.0 (adjustable)
   - Produces pencil sketch effect

---

## Real-World Applications 🚀

- **Artists**: Reference sketches for drawing practice
- **Social Media**: Artistic filters for photos
- **Education**: Learning tool for image processing concepts
- **Fun Projects**: Creative photo transformations for kids and hobbyists

---

## Installation & Setup 🛠️

### Prerequisites
- Python 3.8 or higher
- OpenCV library

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/patelritiq/Sketchify.git
   cd Sketchify
   ```

2. **Install OpenCV:**
   ```bash
   pip install opencv-python
   ```

---

## Usage 📖

1. **Place your image in the project folder**

2. **Update the image path in `sketch.py`:**
   ```python
   image_path = "your_image.jpg"
   ```

3. **Run the script:**
   ```bash
   python sketch.py
   ```

4. **View the results:**
   - Original image
   - Grayscale version
   - Inverted version
   - Final pencil sketch

5. **Press any key to advance through each stage**

---

## Configuration ⚙️

You can adjust the sketch intensity by modifying the `sketch_intensity` variable:

```python
sketch_intensity = 220.0  # Higher = darker sketch, Lower = lighter sketch
```

**Recommended values:**
- Light sketch: 180-200
- Normal sketch: 220 (default)
- Dark sketch: 240-260

---

## Technical Details 🔬

### Image Processing Pipeline
- **Input**: RGB image (any size)
- **Resize**: Max 800x600 (maintains aspect ratio)
- **Grayscale**: BGR to GRAY conversion
- **Inversion**: 255 - pixel_value
- **Blur**: Gaussian kernel (21x21, sigma=0)
- **Blending**: Division with scale factor
- **Output**: Grayscale pencil sketch

### Performance
- **Processing Time**: Near-instant (<1 second for standard images)
- **Memory Usage**: Minimal (depends on image size)
- **Supported Formats**: JPG, PNG, BMP, TIFF (all OpenCV-supported formats)

---

## Limitations ⚠️

- Requires manual image path configuration
- Processes one image at a time
- No automatic saving (displays only)
- Fixed Gaussian kernel size
- Limited to grayscale output

---

## Future Enhancements 🔮

- [ ] GUI for user-friendly controls
- [ ] Batch processing for multiple images
- [ ] Automatic output saving
- [ ] Adjustable blur kernel size
- [ ] Color sketch options
- [ ] Real-time webcam sketching
- [ ] Command-line arguments
- [ ] Different sketch styles (charcoal, ink, etc.)

---

## Troubleshooting 🔧

### Issue: "Error: Unable to load image"

**Solution:**
- Ensure image file exists in the project directory
- Check image filename and extension
- Verify image format is supported by OpenCV

### Issue: Sketch too light/dark

**Solution:**
- Adjust `sketch_intensity` variable
- Higher values = darker sketch
- Lower values = lighter sketch

### Issue: Image too large/small

**Solution:**
- Modify `max_width` and `max_height` variables
- Default: 800x600 pixels

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author 👨‍💻

**Ritik Pratap Singh Patel**

- Computer vision and image processing enthusiast
- OpenCV learner

---

## Acknowledgments 🙏

This project was developed as a learning exercise in computer vision and image processing using OpenCV. It demonstrates fundamental techniques for artistic image transformation.

---

## Quick Start 🚀

```bash
# Clone repository
git clone https://github.com/patelritiq/Sketchify.git
cd Sketchify

# Install OpenCV
pip install opencv-python

# Run the program
python sketch.py
```

Transform your photos into artistic pencil sketches! 🎨✨
