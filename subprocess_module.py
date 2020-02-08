import subprocess

# # send to stdout

# # shell = True
# subprocess.run('ls -al', shell=True)

# print()

# # no shell
# subprocess.run(['ls', '-al'])

# p1 = subprocess.run(['ls', '-al'])
# print(p1.args)
# print(p1.returncode)
# print(p1.stdout)

# send to subprocess pipe

p1 = subprocess.run(['ls', '-al'], capture_output=True)
print(p1.args)
print(p1.returncode)
print(p1.stdout.decode()) # convert bytes to string 

p1 = subprocess.run(['ls', '-al'], capture_output=True, text=True)
print(p1.args)
print(p1.returncode)
print(p1.stdout)

# same as capture_output=True
p1 = subprocess.run(['ls', '-al'], stdout=subprocess.PIPE, text=True)
print(p1.args)
print(p1.returncode)
print(p1.stdout)

# send to file
with open('test_files/output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-al'], stdout=f, text=True)

# dne folder does not exist - does not throw exception
p1 = subprocess.run(['ls', '-al', 'dne'], capture_output=True, text=True)
print(p1.args)
print(p1.returncode)  # error non-zero return code
print(p1.stderr)
print(p1.stdout)

# will throw exception
try:
    p1 = subprocess.run(['ls', '-al', 'dne'], capture_output=True, text=True, check=True)
    print(p1.args)
    print(p1.returncode)  # error non-zero return code
    print(p1.stderr)
    print(p1.stdout)
except Exception as ex:
    print('Exception:', ex)

#ignore all errors
p1 = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL)    
print(p1.args)
print(p1.returncode)  # error non-zero return code
print(p1.stderr)
print(p1.stdout)

# pipe output of command to input of another command
p1 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True)
print(p1.stdout)

p2 = subprocess.run(['grep', '-n', 'Fifth'], capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)

# another way for cat test.txt | grep -n line
p1 = subprocess.run('cat test.txt | grep -n Sixth', shell=True, capture_output=True, text=True)
print(p1.stdout)

