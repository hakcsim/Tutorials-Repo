class Open_File():

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exec_type, exc_val, trackback):
        self.file.close()

with Open_File('test.txt', 'r') as f:
    print(f.read())

print(f.closed)    

from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    try:
        f = open(file_name, mode)
        yield f
    finally:    
        f.close()

with open_file('test.txt', 'r') as f:
    print(f.read())

print(f.closed)    

import os

@contextmanager
def change_dir(dir_name):
    try:
        cwd = os.getcwd()
        os.chdir(dir_name)
        yield
    finally:
        os.chdir(cwd)

with change_dir('test_files'):
    print(os.listdir())

print(os.getcwd())    
