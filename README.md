# Pi-Image-Comparison
Python module to compare images through average hashing algorithm. Thought for raspberry pi, example script tested on Raspberry Pi 2 Model B and requirements file is for that, however it should work on newer pis too.

## Requirements
Other than basic built in python modules such as 'os', 'sys' and 'numpy' which is used by external modules 'pillow' and 'imagehash'.

Inside your 'venv' install the dependencies:
```
pip install pillow imagehash
```
**OR** using the requirements.txt file:
```
pip install -r requirements.txt
```

## Example Usage
### To run the example script:
1. Place your target image and the images to compare in the 'Images' folder.
2. Update the 'TARGET_IMG' variable in 'main.py' with the filename of your target image **OR** rename the target image to 'target.png'.
3. Run the 'main.py' script.
```
python main.py
```
This script will print out a list of duplicate images found in the directory compared to the target image.

*To integrate into your project see function use in example and feel free to change accordingly to your needs.*

## PIC Module Functions
### hash_and_compare_images(target_path, images_path_array)
Function that takes an array of image paths and a target image path, hashes the images and confronts the hashes to identify duplicates, the function calls internal functions 'hash_image' and 'compare_images' to achieve the result.

Parameters:
1. target_path = path to target image
2. images_path_array = array of image paths to confront against the target

Returns:
Array of duplicate image paths in the 'images_path_array'.
