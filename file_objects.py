with open('test.txt', 'r') as f:
    print(f.name)
    print(f.mode)

    f_contents = f.read()
    print(f_contents)

print(f.closed)    

with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')    
    f_contents = f.readline()
    print(f_contents, end='')    
    for line in f:
        print(line, end='')

with open('test.txt', 'r') as f:
    
    f_contents = f.read(100)
    print(f_contents, end='')    
    
    f_contents = f.read(100)
    print(f_contents, end='')   

    f_contents = f.read(100)    
    print(f_contents, end='')   # end of line, print empty 


with open('test.txt', 'r') as f:
    
    size_to_read = 10

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.readline(size_to_read)


with open('test.txt', 'r') as f:
    
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents)

    print(f.tell())

    f_contents = f.read(size_to_read)
    print(f_contents)

    print(f.tell())

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)

    print(f.tell())

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('ABC')

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)        

with open('puppy.jpg', 'rb') as rf:
    with open('puppy_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)        

with open('puppy.jpg', 'rb') as rf:
    with open('puppy_copy_2.jpg', 'wb') as wf:
        chunk_size = 4096

        chunk = rf.read(chunk_size)

        while len(chunk) > 0:
            wf.write(chunk)
            chunk = rf.read(chunk_size)
