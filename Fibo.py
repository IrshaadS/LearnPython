# Fibonacci functions for module demo


def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, end=' ')
        a, b  = b, a + b
    print()


def fib2(n):
    result = []

    a, b = 0, 1

    while a < n:
        result.append(a)
        a, b = b, a + b
    
    return result



#The below code will make this module executable through command line (As Script)

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))