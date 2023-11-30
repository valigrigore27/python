import os
import sys


# def read_and_print_files(directory_path, file_extension):
#     try:
#
#         if not os.path.exists(directory_path):
#             raise FileNotFoundError(f"Directory '{directory_path}' not found.")
#
#         for filename in os.listdir(directory_path):
#             if filename.endswith(file_extension):
#                 file_path = os.path.join(directory_path, filename)
#                 try:
#                     with open(file_path, 'r') as file:
#                         content = file.read()
#                         print(f"Contents of {filename}:\n{content}\n")
#                 except Exception as e:
#                     print(f"Error reading {filename}: {e}")
#     except Exception as e:
#         print(f"Error: {e}")
#
#
# if __name__ == "__main__":
#
#     if len(sys.argv) != 3:
#         print("Usage: python main.py <directory_path> <file_extension>")
#         sys.exit(1)
#
#     directory_path = sys.argv[1]
#     file_extension = sys.argv[2]
#
#     read_and_print_files(directory_path, file_extension)


# __________________________________________________________________________________________________


# _____________________________________________________________________________________

def get_total_size(directory_path):
    total_size = 0

    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        for foldername, subfolders, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)

                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                except Exception as e:
                    print(f"Error getting size of {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

    return total_size


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    total_size = get_total_size(directory_path)

    if total_size > 0:
        print(f"Total size of all files in {directory_path}: {total_size} bytes")

# __________________________________________________________________________________________

#
# def count_files_by_extension(directory_path):
#     extension_counts = {}
#
#     try:
#         if not os.path.exists(directory_path):
#             raise FileNotFoundError(f"Directory '{directory_path}' not found.")
#
#         if not os.listdir(directory_path):
#             print(f"The directory '{directory_path}' is empty.")
#             return
#
#         for filename in os.listdir(directory_path):
#             if os.path.isfile(os.path.join(directory_path, filename)):
#                 _, extension = os.path.splitext(filename)
#
#                 extension_counts[extension] = extension_counts.get(extension, 0) + 1
#
#         if extension_counts:
#             print("File counts by extension:")
#             for extension, count in extension_counts.items():
#                 print(f"{extension}: {count} files")
#         else:
#             print("No files with extensions found in the directory.")
#
#     except Exception as e:
#         print(f"Error: {e}")
#
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python main.py <directory_path>")
#         sys.exit(1)
#
#     directory_path = sys.argv[1]
#
#     count_files_by_extension(directory_path)
