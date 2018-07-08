import os
path1=(r"/home/ayush/Desktop")#give the path of directory1
list_file1=os.listdir(r"/home/ayush/Desktop")#fetching list of file from directory 1

path2=(r"/home/ayush/Documents")#give the path of directory2
list_file2=os.listdir(r"/home/ayush/Documents")#fetchin list of file from directory 2


for i in list_file1:
  print(i)
  if i in list_file2:
       common_file=os.path.join(path1,i)#identifying common file
       os.remove(common_file)#removing the common file
       print('\n\n')
for j in list_file1:
  print(j)
