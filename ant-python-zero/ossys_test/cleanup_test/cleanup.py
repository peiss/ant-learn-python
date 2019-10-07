"""
按后缀名清理文件夹
"""
import sys
import os


def cleanup(dirpath):
    """
    对目录按照后缀名进行清理
    步骤1：用字典按后缀名收集对应的文件
    步骤2：如果后缀名的目录不存在，则创建
    步骤3：移动文件到目标目录
    :param dirpath:
    :return:
    """
    # key:value = ext:list(fname)
    ext_fnames = {}
    for fname in os.listdir(dirpath):
        fdir, fileext = os.path.splitext(fname)
        # 取出.jpg前面的.
        fileext = fileext[1:]
        if fileext not in ext_fnames:
            ext_fnames[fileext] = []
        ext_fnames[fileext].append(fname)

    for ext,fnames in ext_fnames.items():
        ext_dir = "%s/%s"%(dirpath, ext)
        if not os.path.isdir(ext_dir):
            os.mkdir(ext_dir)
        for fname in fnames:
            old_fpath = "%s/%s"%(dirpath, fname)
            new_fpath = "%s/%s"%(ext_dir, fname)
            os.rename(old_fpath, new_fpath)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("please give the cleanup dir path")

    dirpath = sys.argv[1]
    if not os.path.isdir(dirpath):
        raise Exception("%s is not a dir"%dirpath)

    cleanup(dirpath)
    print("success")