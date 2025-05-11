import os
import cv2
import numpy as np

# Define the path to the image folder
path = './cropped(0-1199)/'
output_path = './AB/'
behaviors = ['running/', 'standing/', 'walking/']

# Check whether the folder already exists or not
# If not, proceed to make directories of the following categories
for behavior in behaviors:
    behavior_path = os.path.join(output_path, behavior)
    if not os.path.exists(behavior_path):
        os.makedirs(behavior_path)

def stack_images_to_array(input_path, desired_datatypes):
    image_dir = os.listdir(input_path)
    chunk_size = 4
    image_chunks = [image_dir[i:i+chunk_size] for i in range(0, len(image_dir), chunk_size)]

    stacked_images = []

    for chunk in image_chunks:
        images = []

        for file_path in chunk:
            for desired_datatype in desired_datatypes:
                if f'_{desired_datatype}.' in file_path:
                    image = cv2.imread(os.path.join(input_path, file_path))
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    images.append(image)

        if len(images) == len(desired_datatypes):
            stacked_image = np.stack(images, axis=-1)
            stacked_images.append(stacked_image)

    return np.array(stacked_images)

# Specify the datatypes you want to stack for a given behavior
desired_datatypes = ['A', 'B']  # Change this to the desired datatypes

running_path = os.path.join(path, behaviors[0])
standing_path = os.path.join(path, behaviors[1])
walking_path = os.path.join(path, behaviors[2])

running_data = stack_images_to_array(running_path, desired_datatypes)
standing_data = stack_images_to_array(standing_path, desired_datatypes)
walking_data = stack_images_to_array(walking_path, desired_datatypes)

# Save the numpy arrays for each behavior
np.save(os.path.join(output_path, behaviors[0] + 'running.npy'), running_data)
np.save(os.path.join(output_path, behaviors[1] + 'standing.npy'), standing_data)
np.save(os.path.join(output_path, behaviors[2] + 'walking.npy'), walking_data)
