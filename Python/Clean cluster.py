import os

folder_path = r"C:\Users\evilk\Downloads\PNG"
files = os.listdir(folder_path)
i = 1 # Starting counter for renaming

# Loop through files in the folder
for file in files:
    if file.endswith(".png"):  # Check if file is a PNG
        old_path = os.path.join(folder_path, file)  # Old file path
        new_path = os.path.join(folder_path, f"{i}.png")  # New name with sequential number
        
        # Debug: print the old and new paths to verify
        os.rename(old_path, new_path)  # Rename the file
        print(f"Renamed: {file} -> {i}.png")
        i += 1  # Increment counter for the 
        print(f"Trying to rename: {old_path} -> {new_path}")
    
        # Check if the new path already exists to avoid overwrite
        # if not os.path.exists(new_path):
        #     try:
        #         next file
        #     except Exception as e:
        #         print(f"Error renaming {file}: {e}")
        # else:
        #     print(f"File {new_path} already exists, skipping rename.")
    else:
        print(f"Skipping {file}, not a PNG file.")
