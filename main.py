print('This will always be run, imported or not')

def imported():
    print(__name__)

def main():
    print(__name__)

if __name__ == '__main__':
    # __name__ is '__main__' if the scr4ipt is running directly
    main()
else:
    # __name__ is 'main' if script is imported 
    imported()