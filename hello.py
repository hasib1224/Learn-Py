import sys
print("hello world",sys.version)

name = 1j

def myFunction():
    name = 1j
    print("This is my function",name)

myFunction()
print("This is my function",type(name))