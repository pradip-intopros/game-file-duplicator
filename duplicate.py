
import os
import json
import shutil
import re

def update_prefab_file(file_path, old_prefix, new_prefix):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = json.load(file)

    # Find the first cc.Node object and update its _name attribute
    for obj in content:
        if '__type__' in obj and obj['__type__'] == 'cc.Node':
            if obj['_name'].startswith(old_prefix):
                obj['_name'] = obj['_name'].replace(old_prefix, new_prefix, 1)
            break  # Stop after updating the first cc.Node

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=2, ensure_ascii=False)

def update_ts_file(file_path, old_prefix, new_prefix):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Update the class name
    pattern = r'(export\s+default\s+class\s+)' + re.escape(old_prefix) + r'(\w+)(\s*extends\s+\w+\s*{)'
    new_content = re.sub(pattern, f'\\1{new_prefix}\\2\\3', content, count=1)

    # Update the import statements
    import_pattern = r'(\bimport\s.*from\s+[\'"]\./)' + re.escape(old_prefix) + r'(\w+)'
    new_content = re.sub(import_pattern, f'\\1{new_prefix}\\2', new_content)

    # Update any other occurrences of the old prefix in the file
    new_content = new_content.replace(old_prefix, new_prefix)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def copy_and_rename_prefabs(src_folder, dst_folder, old_prefix, new_prefix):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for root, dirs, files in os.walk(src_folder):
        for dir in dirs:
            src_dir = os.path.join(root, dir)
            dst_dir = src_dir.replace(src_folder, dst_folder, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)

        for file in files:
            src_file = os.path.join(root, file)
            dst_file = src_file.replace(src_folder, dst_folder, 1)

            # Copy the file to the new location
            shutil.copy2(src_file, dst_file)

            # Renaming files and updating contents
            if file.startswith(old_prefix) and (file.endswith(".prefab") or file.endswith(".ts")):
                new_name_with_extension = new_prefix + file[len(old_prefix):]
                new_dst_file = os.path.join(os.path.dirname(dst_file), new_name_with_extension)
                os.rename(dst_file, new_dst_file)
                print(f'Renamed "{dst_file}" to "{new_dst_file}".')

                # Update the prefab file if the file is a .prefab
                if file.endswith('.prefab'):
                    update_prefab_file(new_dst_file, old_prefix, new_prefix)

                # Update the TypeScript file if the file is a .ts
                if file.endswith('.ts'):
                    update_ts_file(new_dst_file, old_prefix, new_prefix)

if __name__ == "__main__":
    src_folder = input("Enter the source folder path: ")
    dst_folder = input("Enter the destination folder path: ")
    old_prefix = input("Enter the old prefix: ")
    new_prefix = input("Enter the new prefix: ")

    copy_and_rename_prefabs(src_folder, dst_folder, old_prefix, new_prefix)
    print("Copying and renaming completed.")
