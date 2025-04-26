import os
import shutil

# Create a directory to hold the files
directory = "path/to/your/directory"
os.makedirs(directory, exist_ok=True)

# Move each file in the specified directory into the new directory
for filename in os.listdir(directory):
    source_file = os.path.join(directory, filename)
    target_file = os.path.join(directory, f"copy_{filename}")
    shutil.move(source_file, target_file)
