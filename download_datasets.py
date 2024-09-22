import os
import gdown

# Google Drive folder ID
folder_url = "https://drive.google.com/drive/folders/1NSbIqcCX6a-f4gJ-qSkHYFTwX9wlMKo8?usp=sharing"
folder_id = folder_url.split('/')[-1].split('?')[0]

# Destination directory
destination = os.path.join(os.getcwd(), 'downloaded_folder')  # Modify the folder name if needed

# Create the destination directory if it doesn't exist
if not os.path.exists(destination):
    os.makedirs(destination)

# Download the entire folder
gdown.download_folder(id=folder_id, output=destination, quiet=False, use_cookies=False)

print(f"Folder has been downloaded to {destination}")
