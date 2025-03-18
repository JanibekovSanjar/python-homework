import numpy as np
from PIL import Image
import os


def save_file(arr, name, mode='RGB'):
    # Ensure the 'images' directory exists
    output_dir = 'images'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    img = Image.fromarray(arr, mode=mode)
    img.save(os.path.join(output_dir, f'{name}.jpg'))


def flip_image(image_loc):
    name_without_ext = os.path.splitext(os.path.basename(image_loc))[0]  # Extract name without extension
    with Image.open(image_loc) as img:
        img_arr = np.array(img)
        flipped = img_arr[::-1, ::-1, :]
        save_file(flipped, name_without_ext + '_flipped')


def add_random_noise(image_loc):
    name_without_ext = os.path.splitext(os.path.basename(image_loc))[0]
    with Image.open(image_loc) as img:
        img_arr = np.array(img)
        mean = 0
        std = 30
        noised = np.clip(img_arr + np.random.normal(mean, std, img_arr.shape), 0, 255).astype(np.uint8)
        save_file(noised, name_without_ext + '_noised')


def brighten_channels(image_loc, val):
    name_without_ext = os.path.splitext(os.path.basename(image_loc))[0]
    with Image.open(image_loc) as img:
        img_arr = np.array(img)
        brightened = np.clip(img_arr + val, 0, 255).astype(np.uint8)
        save_file(brightened, name_without_ext + '_brightened')


def apply_mask(image_loc):
    name_without_ext = os.path.splitext(os.path.basename(image_loc))[0]
    with Image.open(image_loc) as img:
        img_arr = np.array(img)
        h, w, _ = img_arr.shape
        h = (h - 100) // 2
        w = (w - 100) // 2
        for i in range(h, h + 100):
            for j in range(w, w + 100):
                img_arr[i, j] = np.array([0, 0, 0])
        save_file(img_arr, name_without_ext + '_masked')


# Ensure the input file exists
img_file = 'images/birds.jpg'
if not os.path.exists(img_file):
    raise FileNotFoundError(f"The file '{img_file}' does not exist. Please check the path.")

# Apply transformations
flip_image(img_file)
add_random_noise(img_file)
brighten_channels(img_file, 50)
apply_mask(img_file)