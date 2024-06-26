# Pi-Image-Comparison
Python module to compare images through average hashing algorithm. 
Thought for raspberry pi, example script tested on Raspberry Pi 2 Model B and requirements file is for that, however it should work on newer pis too.
The module includes some basic error handling too, feel free to change it for your needs.

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

### Integration
*To integrate into your project see function use in example and feel free to change accordingly to your needs.*

See below for available functions.

## PIC Module Functions
### 1. hash_and_compare_images(target_path, images_path_array)
Function that takes an array of image paths and a target image path, hashes the images and confronts the hashes to identify duplicates, the function calls internal functions 'hash_image' and 'compare_images' to achieve the result.

Parameters:
1. target_path = path to target image.
2. images_path_array = array of image paths to confront against the target.

Returns:
Array of duplicate image paths in the 'images_path_array'.

### 1.1 hash_image(image_path)
*Note: this function is called by the 'hash_and_compare_images' function.*
Fucntion to convert image to hash for comparison. Including basic error handling to ensure compatability.

Parameters:
1. images_path = image paths to image to be hashed.

Returns:
Image hash or error message.

### 1.2 compare_images(target_hash, images_path_array)
*Note: this function is called by the 'hash_and_compare_images' function.*
Fucntion to hash array of images into hashes and compare themwith the target hash.

Parameters:
1. target_hash = hash of target image.
2. images_path_array = array of image paths to hash and confront against the target hash.

Returns:
Array of duplicate image paths in the 'images_path_array'.

### 2. validate_image_folder(folder_path)
Function to validate existance of image folder.

Parameters:
1. folder_path = folder paths where images are stored.

Returns:
void.

### 3. validate_target_image(folder_path, target_image)
Function to validate existance of target image in folder and returns a full target image path

Parameters:
1. folder_path = folder paths where images are stored.
2. target_image = target image filename

Returns:
target image path.

### 4. get_image_list(folder_path, target_image)
Function to retrieve an array of image paths in the images folder, excluding the target image, for comparison.
Includes basic error handling to only include image files ('.png', '.jpg', '.jpeg', '.bmp', '.gif').

Parameters:
1. folder_path = folder paths where images are stored.
2. target_image = target image filename

Returns:
Array of image paths.
