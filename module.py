import os
print("platform",os.getenv("os)"))
print("current dir",os.getcwd())
print("file available",os.listdir(r'C:\Users\User\Documents\TESTING ITCRATS INTRANET PORTAL.xlsx_files'))
os.chdir("../")
print("new-path",os.getcwd())



path=r"C:\Users\User\Documents\TESTING ITCRATS INTRANET PORTAL.xlsx_files"
dir="test"
new_path=os.path.join(path,dir)
print(new_path)
print("new_path",os.makedirs(new_path))
