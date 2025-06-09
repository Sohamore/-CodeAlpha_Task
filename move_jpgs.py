import os
import shutil

source_folder = r'C:\Users\Soham\OneDrive\Desktop\images'
destination_folder = r'C:\Users\Soham\OneDrive\Desktop\organize_images'

print("Source folder exists:", os.path.exists(source_folder))
print("Destination folder exists:", os.path.exists(destination_folder))

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print("Created destination folder.")

# Move all .jpg or .jpeg files
for file_name in os.listdir(source_folder):
    print("Found file:", file_name)
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.aivf')):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
        print(f"Moved: {source_path} --> {destination_path}")

print("✅ All matching files moved.")
