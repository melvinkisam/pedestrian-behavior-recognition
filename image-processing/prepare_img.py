import os
import shutil

# Define the path to the image folder
path = './cropped(0-1199)/'
dest_dir = './imgD/' # path to new image folder
img_type = 'D'

# Check whether the folder already exist or not
# If not, proceed to make directories of the following categories
if not os.path.exists(dest_dir+'running'):
    os.makedirs(dest_dir+'running')
if not os.path.exists(dest_dir+'standing'):
    os.makedirs(dest_dir+'standing')
if not os.path.exists(dest_dir+'walking'):
    os.makedirs(dest_dir+'walking')

# Loop through the entire images of the original folder
# By using string comparison, copy the images to the proper categories based on their names
for image in os.listdir(path+'running/'):
    # If image contain "cloudy" string, copy it to the cloudy folder
    if img_type in image:
        shutil.copy(os.path.join(path+'running', image), os.path.join(dest_dir, 'running', image))

for image in os.listdir(path+'standing/'):
    # If image contain "cloudy" string, copy it to the cloudy folder
    if img_type in image:
        shutil.copy(os.path.join(path+'standing', image), os.path.join(dest_dir, 'standing', image))

for image in os.listdir(path+'walking/'):
    # If image contain "cloudy" string, copy it to the cloudy folder
    if img_type in image:
        shutil.copy(os.path.join(path+'walking', image), os.path.join(dest_dir, 'walking', image))
