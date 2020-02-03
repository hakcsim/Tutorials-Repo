import os

print(os.getcwd())

# os.chdir("/Users/haksim/Projects/Tutorials/CoreySchafer/")

print(os.getcwd())

print(os.listdir())

# os.mkdir("OS-Demo")
# os.rmdir("OS-Demo")

# os.makedirs("OS-Demo/OS-Demo-Sub1/OS-Demo-Sub2")
# os.removedirs("OS-Demo/OS-Demo-Sub1/OS-Demo-Sub2")

print(os.listdir())

# os.rename('test.txt', 'demo.txt')

print(os.stat("os_module.py"))
print(os.stat("os_module.py").st_mtime)
from datetime import datetime

mod_time = os.stat("os_module.py").st_mtime

print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print("Current Path:", dirpath)
#     print("Directories:", dirnames)
#     print("Files:", filenames)
#     print()

print(os.environ)
print(os.environ.get("HOME"))

file_path = os.path.join(os.getcwd(), "test.txt")

print(file_path)

print(os.path.basename(file_path))
print(os.path.dirname(file_path))
print(os.path.split(file_path))
print(os.path.splitext(file_path))
print(os.path.exists(file_path))
print(os.path.isfile(file_path))
print(os.path.isdir(file_path))

import glob

# get all Python script files
for file in glob.glob('*.py'):
    print(file)

