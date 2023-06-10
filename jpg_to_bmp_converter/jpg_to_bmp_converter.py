from PIL import Image
import os
 
# Function to convert jpg to bmp
def convert_to_bmp(filename):
    # Open the image file
    with Image.open(filename) as im:
        # Save the file with bmp extension
        new_filename = os.path.splitext(filename)[0] + ".bmp"
        im.save(new_filename, format="BMP")
 
# Function to convert all jpg files in a folder to bmp
def convert_folder(folder_path):
    # Get all the jpg files in the folder
    jpg_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(".jpg")]
    # Convert each jpg file to bmp
    for filename in jpg_files:
        convert_to_bmp(os.path.join(folder_path, filename))
 
# Menu to choose folder with jpg images and folder to save converted bmp images
jpg_folder_path = input("Enter path of folder with .jpg images: ")
bmp_folder_path = input("Enter path of folder to save converted .bmp images: ")
convert_folder(jpg_folder_path)
print("All .jpg files in folder {} converted to .bmp and saved in folder {}.".format(jpg_folder_path, bmp_folder_path))
 
# softy plug