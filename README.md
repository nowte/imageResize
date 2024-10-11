<p align="center">
  <img src="https://imgur.com/aNPHSWq.png" alt="Logo" width="150" height="150" />
</p>
<p align="center">
<a href="https://github.com/nowte/imageResize/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/ImageResize-v1.0-blue.svg" height="20"/></a>
<a href="https://github.com/nowte/imageResize/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/nowte/imageResize?style=for-the-badge" height="20"/></a>
</p>

<p align="center">
  <b></b>
</p>

## Table of Contents

- [🔍 Introduction](#introduction)
- [📦 Features](#features)
- [🛠️ Installation](#installation)
- [🚀 Usage](#usage)
- [🎨 Customization](#customization)
- [📑 How It Works](#how-it-works)
- [⚙️ Contributing](#contributing)
- [📧 Contact](#contact)
- [📝 License](#license)

## 🔍 Introduction

**ImageResize** is a powerful Python application that allows users to resize images while maintaining their aspect ratios. It is designed to be user-friendly, offering both a graphical user interface (GUI) and command-line options. Whether you're a developer looking for a quick solution to resize images or a casual user who needs a simple tool, ImageResize has you covered!

## 📦 Features

- **Multiple Image Formats**: Supports various image formats, including PNG, JPEG, BMP, and GIF.
- **User-Friendly Interface**: Choose between using a GUI or entering commands in the terminal.
- **Aspect Ratio Preservation**: Resizes images without losing quality or distorting the aspect ratio.
- **Custom Resizing**: Enter custom dimensions or choose a default size for resizing.
- **Automatic Save Locations**: Save resized images in the same directory as the original or specify a new location.
- **Error Handling**: Comprehensive error messages to guide users through the process.

## 🛠️ Installation

To install ImageResize, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nowte/ImageResize.git
   cd ImageResize
   
## 🚀 Usage

Launch the Application: Run the main.py file to start the application.
Select Image: Choose an image to resize by either using the file picker dialog or manually entering the file path.
Input Dimensions: Enter the desired width and height in pixels for resizing.
Save Resized Image: Decide whether to save the resized image in the original directory or specify a new path.
Enjoy the Results: Once the process is complete, your resized image will be saved as per your preferences!

## 🎨 Customization

Feel free to modify the source code to customize ImageResize for your specific needs. You can change the default resizing dimensions, add more file formats, or adjust the user interface as required.

## 📑 How It Works

ImageResize utilizes the PIL (Python Imaging Library) to handle image processing. The application works by:

Opening the Image: Loads the selected image file using PIL.
Calculating Dimensions: Computes the new dimensions while maintaining the original aspect ratio.
Resizing the Image: Uses the LANCZOS filter to resize the image, ensuring high quality.
Saving the Output: Saves the resized image in the specified format and location.

## ⚙️ Contributing

Contributions are welcome! If you want to enhance ImageResize, feel free to fork the repository and submit a pull request. Please ensure your changes align with the project's goals and maintain code quality.

Steps to Contribute:
Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them with a clear message.
Push your branch and open a pull request.

## 📧 Contact

For questions, suggestions, or feedback, please reach out:

Email: your_email@example.com
GitHub: nowte
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

Thank you for using ImageResize! 🎉
