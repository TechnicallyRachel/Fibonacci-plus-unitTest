def fib(n): # return Fibonacci series of numbers up to "nth"
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def main():
    print fib(10)

if __name__ == '__main__' : main()

