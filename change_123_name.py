import os
file_names=os.listdir("123")
print(file_names)
os.chdir("./123")
for name in file_names:
    index=name.find(".")
    os.rename(name,name[:index]+"_rename"+name[index:])