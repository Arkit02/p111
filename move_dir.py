import os
file_dir="E:/STUDY"
listOfFile=os.listdir(file_dir)
print(listOfFile)

for fileName in listOfFile:
    name,extension=os.path.splitext(fileName)
    print(name)
    print(extension)