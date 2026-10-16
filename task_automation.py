import os
import shutil

print("===== FILE AUTOMATION TOOL =====")

source_folder = input("Enter source folder path: ").strip().strip('"')
destination_folder = input("Enter destination folder path: ").strip().strip('"')

if not os.path.exists(source_folder):
    print("Source folder does not exist.")
else:
    os.makedirs(destination_folder, exist_ok=True)

    moved = 0

    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".jpeg")):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
                print(f"Moved: {filename}")
                moved += 1

    if moved == 0:
        print("No JPG/JPEG files found.")
    else:
        print(f"\nTotal files moved: {moved}")

print("Automation completed!")