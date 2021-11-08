import os

import regex
from natsort import natsort_key

folders = list(next(os.walk("."))[1])
for folder in folders:
    count = 0
    digits = 0
    numHolder = "{num}"
    titleHolder = "{title}"
    titles = None
    regx = True
    oldName = "{title} - E{num}.*\.mkv"
    newName = "{title} - EP{num}.mkv"
    if titleHolder in newName and titleHolder not in oldName:
        try:
            with open("Titles.txt", "r") as f:
                titles = {}
                for i, l in enumerate(f):
                    titles[l.partition(" ")[0]] = l.partition(" ")[2].replace("\n", "")
        except IOError:
            print("Dude.. Want titles, provide titles. That's how life works.")
            input("")
            exit()
    files = list(next(os.walk(f".\\{folder}"))[2])
    data = []
    success = []
    failed = []
    files.sort(key=natsort_key)
    if regx:
        filePattern = oldName
    else:
        filePattern = regex.escape(oldName)
        numHolder = r"\{num\}"
        titleHolder = r"\{title\}"
    numPattern = "(" + filePattern.replace(titleHolder, ".+").replace(numHolder, r")\K(\d+(-\d+)*)(?=") + ")"
    titlePattern = "(" + filePattern.replace(titleHolder, r")\K(.+)(?=").replace(numHolder, r"\d+(-\d+)*") + ")"
    filePattern = filePattern.replace(numHolder, r"\d+(-\d+)*").replace(titleHolder, r".+")
    for file in files:
        if regex.fullmatch(filePattern, file):
            num = regex.search(numPattern, file)[0]
            if titles:
                try:
                    title = titles[num]
                except KeyError:
                    title = ""
            elif "{title}" in newName:
                title = regex.search(titlePattern, file)[0]
            else:
                title = ""
            data.append((file, num, title))
            for number in num.split("-"):
                digits = max(digits, len(str(int(number))))
    for file, n, title in data:
        num = ""
        for number in reversed(n.split("-")):
            number = str(int(number))
            num = f"{number}-{num}"
            for _ in range(digits - len(number)):
                num = f"0{num}"
        num = num[:-1]
        name = newName.format(num=num, title=title)
        try:
            if os.path.exists(name):
                raise FileExistsError
            os.rename(folder + "\\" + file, folder + "\\" + name)
            success.append((file, name))
            count += 1
        except:
            failed.append((file, name))
    if count == 0 and not failed:
        print(f"YARE YARE DAZE.. \"{oldName}\" doesn't even exist!")
    elif count == 0:
        print("SUGE! All files failed!\n"
              "Nani ga Anta?!")
        for old, new in failed:
            print(f"{old} -> {new}")
    else:
        print(f"YATTA.. Renamed {count} files, From \"{success[0][0]}\" to \"{success[-1][1]}\".")
        if failed:
            print("But i have failed to rename some files for some reason.\n"
                  "You'll figure it out.\n"
                  "Have a nice day.\n"
                  "Files failed:")
            for old, new in failed:
                print(f"{old} -> {new}")