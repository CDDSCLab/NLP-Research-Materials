#conding=utf8

import os
result_Path = "./README.md"
result_file = open(result_Path, 'w', encoding="utf-8")
copyright_info = f'\n:book: 申明：本仓库收集的所有资料均来源于网络,仅供学习交流使用。如有侵权请联系删除！'

result_file.write(f'# 分布式存储与计算NLP小组资料分享\n\
    收集机器学习和自然语言处理相关的资料，欢迎大家补充！\n\n\
### 目录\n')

current_path = "./"

# default setting
maxLevel = 4

# default ignored file
ignore_files = ["README.md",".git","genDirectory.py","directory.md"]
ignore_ftypes = [".py",".html",".png",".jpg",".rar",".zip"]
max_fold_lv = 3
at_root_file = []
# interWalker traverses the folder generation directory

def interWalker(path, lv):

    files = os.listdir(path)
    
    need_details = False

    for f in files:
        if f in ignore_files:
            continue
        # if the lv < max fold lv,then we need a folding element
        if lv<max_fold_lv and os.path.isdir(path + f):
            need_details = True
            result_file.write("<details>\n")
            # add folding title
            result_file.write(f"<summary>{f}</summary>\n\n")

        # split filename and filetype
        _, ftype = os.path.splitext(f)
        if ftype in ignore_ftypes:
            continue

        # construct the markdown url syntax
        pf = genPrefix(lv-max_fold_lv+1)
        url = handleFormat(path+f)

        file_url = f"{pf}[{f}]({url})\n"

        # files that at the root we need to put them at the bottom of the toc
        if lv==1 and os.path.isfile(path+f):
            at_root_file.append(f"△ [{f}]({url})\n")
        else:
            result_file.write(file_url)

        if lv >= maxLevel:
            continue
        if os.path.isdir(path + f):
            interWalker(path + f + "/", lv+1)

        if need_details:
            result_file.write("</details>\n\n")
            need_details=False

def genPrefix(lv):
    prefix="\t"*(lv-1)+'- '
    return prefix

# handleFormat handles the special formats
# maybe we can modify the file name directly
def handleFormat(url):
    # '%20' is space sign in url
    return url.replace(' ','%20')

interWalker(current_path, 1)
# write files url at the root
result_file.write("\n".join(at_root_file))
result_file.write(copyright_info)
result_file.close()
