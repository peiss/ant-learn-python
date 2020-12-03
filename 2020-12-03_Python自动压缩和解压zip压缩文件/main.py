import os
import zipfile


def zip_file(dir_path):
    with zipfile.ZipFile(dir_path + ".zip", "w", zipfile.ZIP_DEFLATED) as zfile:
        for iter_dir_path, dirs, files in os.walk(dir_path):
            for file in files:
                fpath = os.path.join(iter_dir_path, file)
                zfile.write(fpath)


def unzip_file(zip_file, target_dir):
    with zipfile.ZipFile(zip_file, "r") as zfile:
        for file in zfile.namelist():
            zfile.extract(file, target_dir)


# zip_file("数据文件夹")
unzip_file("数据文件夹.zip", "解压文件夹")
