import zipfile
import os

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(path))
            ziph.write(file_path, arcname)

if __name__ == '__main__':
    zip_file_name = 'grey_build.bdi'
    directory = 'skin'

    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(directory, zipf)