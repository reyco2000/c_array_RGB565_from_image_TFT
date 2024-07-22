import sys
from PIL import Image

# This program reads a JPEG file, converts it into an RGB565 C array,
# and writes the C array to a file with the same name as the input file but with a .c extension.
# The program takes the filename as an argument from the command line.
# The output C array is represented as const unsigned char, with the low byte first, followed by the high byte.
# Dependencies: Pillow library for image processing
# To install Pillow, run: pip install Pillow

def convert_image_to_rgb565_array(image_path):
    # Open the image file
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB mode
    
    # Get image dimensions
    width, height = img.size
    
    # Initialize the C array
    c_array = []
    
    # Convert each pixel to RGB565 and add to the array
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            rgb565 = ((r & 0xf8) << 8) | ((g & 0xfc) << 3) | (b >> 3)
            c_array.append(rgb565 & 0xFF)         # Low byte
            c_array.append((rgb565 >> 8) & 0xFF)  # High byte
    
    return c_array, width, height

def write_c_array_to_file(array, width, height, output_path):
    with open(output_path, 'w') as file:
        file.write(f"// RGB565 C array\n")
        file.write(f"// Image size: {width}x{height}\n")
        file.write(f"const unsigned char image[{height * width * 2}] = {{\n")
        
        for i in range(0, len(array), 12):  # 12 bytes per line (6 pixels)
            file.write("    ")
            file.write(", ".join(f"0x{array[j]:02X}" for j in range(i, min(i + 12, len(array)))))
            if i + 12 < len(array):
                file.write(",\n")
            else:
                file.write("\n")
            
        file.write("};\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_to_rgb565.py <image_file>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    output_path = image_path.rsplit('.', 1)[0] + '.c'
    
    c_array, width, height = convert_image_to_rgb565_array(image_path)
    write_c_array_to_file(c_array, width, height, output_path)
    
    print(f"C array written to {output_path}")

if __name__ == "__main__":
    main()
