import os
import re
import sys

dir_path = "C:/Users/Tuf/OneDrive/Desktop/python/Proiect"


def create_files_path(file):
    if not os.path.exists(dir_path):
        raise FileNotFoundError(f"Directory '{dir_path}' not found.")
    else:
        file_path = os.path.join(dir_path, file)
    return file_path


def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            content = re.sub("\s+", " ", content)
            content = re.sub("\n", " ", content)
            phrases = re.findall("[A-Z0-9].*?[.?!]", content)
    except Exception as e:
        print(f"Error processing files: {e}")
    return phrases


def common_phrases():
    content1 = read_from_file(create_files_path(file1))
    content2 = read_from_file(create_files_path(file2))
    # print(content1)
    # print()
    # print(content2)
    for prop1 in content1:
        for prop2 in content2:
            if prop2 == prop1:
                print(prop1)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python main.py <file1> <file2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    common_phrases()
