import os

with open("README_bak.md", "r") as fp:
    f = fp.readlines()

with open("README.md", "w+") as fp:
    for line in f:
        fp.writelines(line)

    subfolders = next(os.walk('.'))[1]
    for folder in list(subfolders):
        if folder == ".git":
            continue

        msg = '''* [%s](%s) \n''' % (folder, folder.replace(" ", "\ "))

        fp.writelines(msg)
