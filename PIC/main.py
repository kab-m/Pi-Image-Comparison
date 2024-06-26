# Usage example of image_hasher.

import os
from PIC import hash_and_compare_images, validate_image_folder, validate_target_image, get_image_list


# Define the folder to saved images
IMAGE_FOLDER = 'Images/'
TARGET_IMG = "target.png"


def main():
    # Validate the image folder
    validate_image_folder(IMAGE_FOLDER)

    # Validate the target image and get its path
    target_path = validate_target_image(IMAGE_FOLDER, TARGET_IMG)

    # Get the list of all images in the folder except the target
    images_path_array = get_image_list(IMAGE_FOLDER, TARGET_IMG)

    # Compare the new image with others
    duplicates = hash_and_compare_images(target_path, images_path_array)

    # Print results
    if duplicates:
        print(f"Found {len(duplicates)} duplicate(s):")
        for dup in duplicates:
            print(dup)
    else:
        print("No duplicates found.")
    
    
if __name__ == '__main__':
    main()