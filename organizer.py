import os
import shutil

# ✅ Define the folder you want to organize (use raw string to avoid backslash issues)
SOURCE_FOLDER = r"C:/path/to/your/folder"  # <-- change this to your folder path

# 📦 Define file type categories
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Others': []  # fallback for anything else
}

def organize_files():
    # Loop through each file in the folder
    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)
        
        # Check if it's a file (skip folders)
        if os.path.isfile(file_path):
            # Get the file extension (lowercase)
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            # Try to match the file type category
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_folder = os.path.join(SOURCE_FOLDER, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"✅ Moved {filename} to {folder}/")
                    moved = True
                    break
            
            # If no match, move to 'Others'
            if not moved:
                target_folder = os.path.join(SOURCE_FOLDER, 'Others')
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"✅ Moved {filename} to Others/")

if __name__ == "__main__":
    print(f"📁 Organizing files in: {SOURCE_FOLDER}")
    organize_files()
    print("🎉 File organization complete.")
