import os

with open("README_bak.md", "r") as fp:
    f = fp.readlines()

with open("README.md", "w+") as fp:
    for line in f:
        fp.writelines(line)

    for folder in list(os.listdir(".")):
        if folder == ".git":
            continue

        msg = '''* [%s](%s) \n''' % (folder, folder)

        fp.writelines(msg)
