#conding=utf8

import os
result_Path = "./directory.md"
result_file = open(result_Path, 'a', encoding="utf-8")
current_path = "./"

# default setting
maxLevel = 4

# default ignored file
ignore_files = ["README.md",".git","genDirectory.py","directory.md"]
ignore_ftypes = [".py",".html",".png",".jpg",".rar",".zip"]

# interWalker traverses the folder generation directory
def interWalker(path, lv):
    files = os.listdir(path)
    pf = genPrefix(lv)
    for f in files:
        if f in ignore_files:
            continue

        _, ftype = os.path.splitext(f)
        if ftype in ignore_ftypes:
            continue

        url = path+f
        url = handleFormat(url)
        result_file.write(pf)
        result_file.write("[{}]({})\n".format(f, url))

        if lv >= maxLevel:
            continue
        if os.path.isdir(path + f):
            interWalker(path + f + "/", lv+1)

def genPrefix(lv):
    prefix = ""
    for i in range(0,lv):
        if i == lv-1:
            prefix += "- "
            continue
        prefix += "\t"
    return prefix

# handleFormat handles the special formats
# maybe we can modify the file name directly
def handleFormat(url):
    # '%20' is space sign in url
    return url.replace(' ','%20')

interWalker(current_path, 1)
result_file.close()

