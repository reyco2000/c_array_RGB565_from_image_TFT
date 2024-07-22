
This program reads a JPEG file, converts it into an RGB565 C array,used on embedded systems with TFT screens
and writes the C array to a file with the same name as the input file but with a .c extension.
The program takes the filename as an argument from the command line.
The output C array is represented as const unsigned char, with the low byte first, followed by the high byte.
Additionally, the output file includes a comment with the image size.
 
 Dependencies: Pillow library for image processing
 To install Pillow, run: pip install Pillow
 
 Usage: python convert_to_rgb565.py <image_file>


 Author: Reinaldo Torres reyco2000@gmail.com July 2024
 This code is free and open source, and can be used and modified for any purpose.

