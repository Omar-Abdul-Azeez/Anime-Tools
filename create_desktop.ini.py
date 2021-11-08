import os


folders = next(os.walk('.'))[1]
for folder in folders:
    f = open(folder + "\\desktop.ini", "w+")
    f.write("[.ShellClassInfo]\nConfirmFileOp=0\n")
    f.write("IconResource={},0".format(folder + ".ico"))
    f.write("\nIconFile={}\nIconIndex=0".format(folder + ".ico"))
    f.close()
    os.system('attrib +r \"{}\\{}\"'.format(os.getcwd(), folder))
    os.system('attrib +h \"{}\\desktop.ini\"'.format(folder))
    os.system('attrib +h \"{}\"'.format(folder + "\\" + folder + ".ico"))
