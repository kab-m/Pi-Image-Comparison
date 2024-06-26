# Pi Image Hasher Module
# Author: kab-m

from PIL import Image, UnidentifiedImageError
import imagehash
import os
import sys

# Hash a single image
def hash_image(image_path):
    
    try:
        image = Image.open(image_path)
        return imagehash.average_hash(image)
    
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        sys.exit(0)  # Terminate the program

    except UnidentifiedImageError:
        print(f"Cannot identify image file: {image_path}")
        sys.exit(0)  # Terminate the program

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        sys.exit(0)  # Terminate the program


# Hash array of images and compare target hash for duplicates
def compare_images(target_hash, images_path_array):
    
    duplicates = []

    for img_path in images_path_array:
        img_hash = hash_image(img_path)

        if img_hash == target_hash:
            duplicates.append(img_path)

    return duplicates


# Hash target image and compare it against an array of images
def hash_and_compare_images(target_path, images_path_array):
    
    target_hash = hash_image(target_path)

    if target_hash is None:
        return []
    
    return compare_images(target_hash, images_path_array)


# Validate the image folder
def validate_image_folder(folder_path):
    
    if not os.path.exists(folder_path):
        print(f"Image folder '{folder_path}' does not exist.")
        sys.exit(0)  # Terminate the program


# Validate the target image
def validate_target_image(folder_path, target_image):
    
    target_path = os.path.join(folder_path, target_image)

    if not os.path.exists(target_path):
        print(f"Target image {target_image} not found in {folder_path}.")
        sys.exit(0)  # Terminate the program

    return target_path


# Get the list of all images in the folder except the target image
def get_image_list(folder_path, target_image):
    
    try:
        images_path_array = [
            os.path.join(folder_path, f) for f in os.listdir(folder_path)
            if f != target_image and f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))
        ]
        return images_path_array
    
    except Exception as e:
        print(f"Error accessing files in {folder_path}: {e}")
        sys.exit(0)  # Terminate the program