def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter n:"))
fib_sequence = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")