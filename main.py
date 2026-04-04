import os
import re

def to_camel_case(text):
    # Remove the file extension first to process only the name
    name, ext = os.path.splitext(text)
    
    # Replace underscores and hyphens with spaces to create a clean word list
    clean_name = re.sub(r'[-_]', ' ', name)
    
    # Split by space, capitalize each word, and join them
    words = clean_name.split()
    camel_case_name = "".join(word.capitalize() for word in words)
    
    return camel_case_name + ext

def rename_md_files(root_folder):
    # Check if directory exists
    if not os.path.isdir(root_folder):
        print(f"Error: {root_folder} is not a valid directory.")
        return

    # Walk through the directory tree
    for root, dirs, files in os.walk(root_folder):
        for filename in files:
            # Check for .md files
            if filename.lower().endswith(".md"):
                old_path = os.path.join(root, filename)
                
                # Generate new name
                new_filename = to_camel_case(filename)
                new_path = os.path.join(root, new_filename)
                
                # Only rename if the name is actually different
                if old_path != new_path:
                    try:
                        os.rename(old_path, new_path)
                        print(f"Renamed: '{filename}' -> '{new_filename}'")
                    except OSError as e:
                        print(f"Error renaming {filename}: {e}")

if __name__ == "__main__":
    # Change '.' to your specific folder path if needed
    target_directory = "/home/nij/test/Prompts_list" 
    rename_md_files(target_directory)
    print("Process complete.")