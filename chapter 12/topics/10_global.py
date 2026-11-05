a = 89 # Global keyword

def Func():
    global a # We are changing the global keyword
    a = 3
    print(a)

Func()
print(a)