def fib_iter(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def fib_rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
    
Fibbonacci_iter = 5
Fibbonacci_rec = 5
print("Fibonacci반복(",Fibbonacci_iter,") =", fib_iter(Fibbonacci_iter))
print("Fibonacci순환(",Fibbonacci_rec,") =", fib_rec(Fibbonacci_rec))