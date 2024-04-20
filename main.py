from pathlib import Path
import zipfile



def traverse(path: Path):

    directories = list(filter(lambda x: x.is_dir(), path.iterdir()))
    for directory in directories: traverse(Path(directory))


    files = list(filter(lambda x: x.is_file(), path.iterdir()))

    for file in files:
        if zipfile.is_zipfile(file):
            print(f"{file}: is a zip file")
        else:
            print(f"{file}: is not a zip file")
            # with zipfile.ZipFile(file, 'r') as zip_ref:
            # # Extract all contents to the directory
            #     zip_ref.extractall(file)
            #     print(f"Unzipped: {file}")


def main():
    # item = "dir_1.zip"
    # with zipfile.ZipFile(item, 'r') as zip_ref:
    #     zip_ref.extractall(item)
    traverse(Path('test_data/final'))

if __name__ == "__main__":
    main()



# given current path
#     has directories
#         given current path

#         are any files zips
#             burst

#             has directories
#                 given current path
#             return
