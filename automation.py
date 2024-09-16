# Python Script to Automate File Organization
import os
import shutil

# Define the source directory and target folder structure
source_dir = r"your_file_directory"
target_dir = r"your_targeted_file_directory"


# Create target folders if they don't exist
os.makedirs(target_dir, exist_ok=True)

# Define file extensions and corresponding target folders
file_types = {
    "images": [".jpg", ".png", ".gif", ".jpeg"],
    "documents": [".pdf", ".doc", ".docx", ".txt"],
    "videos": [".mp4", ".avi", ".mov"],
    "audio": [".mp3", ".wav"],
    "others": []  # For files with unsupported extensions
}

# Iterate through files in the source directory
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    file_ext = os.path.splitext(filename)[1]

    # Find the appropriate target folder based on the extension
    target_folder = None
    for key, extensions in file_types.items():
        if file_ext in extensions:
            target_folder = os.path.join(target_dir, key)
            break
    if not target_folder:
        target_folder = os.path.join(target_dir, "others")

    # Create the target folder if it doesn't exist
    os.makedirs(target_folder, exist_ok=True)

    # Move the file to the target folder
    shutil.move(file_path, os.path.join(target_folder, filename))

print("File organization completed!")