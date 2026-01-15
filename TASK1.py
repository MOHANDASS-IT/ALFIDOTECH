import os
import logging

logging.basicConfig(
    filename="mohan.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def rename_files(folder_path):
    prefix = input("Enter prefix to add to files: ")

    try:
        for filename in os.listdir(folder_path):
            old_path = os.path.join(folder_path, filename)

            if os.path.isfile(old_path):
                new_name = prefix + filename
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                logging.info(f"Renamed {filename} to {new_name}")

        print("✅ Files renamed successfully")

    except Exception as e:
        logging.error(f"Error while renaming files: {e}")
        print("❌ Error:", e)
def sort_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                ext = filename.split('.')[-1]
                ext_folder = os.path.join(folder_path, ext)

                if not os.path.exists(ext_folder):
                    os.mkdir(ext_folder)

                os.rename(file_path, os.path.join(ext_folder, filename))
                logging.info(f"Moved {filename} to {ext_folder}")

        print("✅ Files sorted successfully")

    except Exception as e:
        logging.error(f"Error while sorting files: {e}")
        print("❌ Error:", e)
def clean_empty_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                os.remove(file_path)
                logging.info(f"Deleted empty file: {filename}")

        print("✅ Empty files removed")

    except Exception as e:
        logging.error(f"Error while cleaning files: {e}")
        print("❌ Error:", e)

def main():
    folder_path = input("Enter folder path: ")

    if not os.path.exists(folder_path):
        print("❌ Invalid folder path")
        return

    print("\nChoose Operation:")
    print("1. Rename Files")
    print("2. Sort Files by Extension")
    print("3. Clean Empty Files")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        rename_files(folder_path)
    elif choice == "2":
        sort_files(folder_path)
    elif choice == "3":
        clean_empty_files(folder_path)
    else:
        print("❌ Invalid choice")
if __name__ == "__main__":
    main()
