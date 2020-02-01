
try:
    f =  open('test.txt', 'r')
    #x = y
except FileNotFoundError as e:
    print(e)     
except Exception as e:
    print(e)    
else:
    print(f.read())
    f.close()    
finally:
    print('Executing finally...')

try:
    f =  open('test.txt', 'r')
    
    if f.name == 'test.txt':
        raise Exception('Raised exception') 

except FileNotFoundError as e:
    print(e)     
except Exception as e:
    print(e)    
else:
    print(f.read())
    f.close()    
finally:
    print('Executing finally...')


for i in range(10):

    print(i)

    if (i == 11):
        break
else:
    print('for loop did not break')    

while (i < 20):

    i += 1

    if i == 24:
        break
else:
    print('while loop did not break')


