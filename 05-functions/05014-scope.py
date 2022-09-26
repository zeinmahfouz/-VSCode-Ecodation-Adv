def scopeTest():
    a = 34
    print(a)
a = 19
scopeTest()
print(a)

def scopeTest():
    a = 34
    print(id(a))

a = 19
scopeTest()
print(id(a))

def scopeTest():
    global a
    a = 34
    print(id(a))

a = 19
scopeTest()
print(id(a))

def scopeTest(arg):
    print(arg)
    arg = [19, 34, 35]
    
liste = [19, 34]
scopeTest(liste)
print(liste)


