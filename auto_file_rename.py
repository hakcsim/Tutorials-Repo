import os
import shutil

path = os.path.join(os.getcwd(), 'test_files')

os.chdir(path)

print(os.getcwd())

d = {}

for f in os.listdir():
    if os.path.isfile(os.path.join(path, f)):
        print(f)
        f_name, f_ext = os.path.splitext(f)
        tokens = f_name.split('-')

        if len(tokens) == 3:
            print(tokens)
            new_filename = '{}-{}{}'.format(tokens[2].strip()[1:].zfill(2), tokens[0].strip(), f_ext)
            print(new_filename)
            shutil.copyfile(os.path.join(path, f), os.path.join(path, new_filename))
            #os.rename(os.path.join(path, f), os.path.join(path, new_filename))



