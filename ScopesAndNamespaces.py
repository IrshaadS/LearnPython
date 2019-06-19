#Scopes and namespaces

def scope_test():
    def do_local():
        a = "local a"
    
    def do_nonlocal():
        nonlocal a
        a = "non local a"
    
    def do_global():
        global a
        a = "global a"

    a = "test a"

    do_local()
    print("After local assignment :", a)

    do_nonlocal()
    print("After nonlocal Assignment", a)

    do_global()
    print("After global assignment", a)

scope_test()
print("In global scope:", a)
