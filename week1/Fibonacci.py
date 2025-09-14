import time

# 반복적 Fibonacci 함수
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
    
# 재귀적 Fibonacci 함수
def fib_rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

# 테스트할 Fibonacci 수 (기본값이 5임)
Fibonacci_iter = 5
Fibonacci_rec = 5
iter_result = fib_iter(Fibonacci_iter)
rec_result = fib_rec(Fibonacci_rec)
print(f"Fibonacci반복({Fibonacci_iter}) =", iter_result) #반복
print(f"Fibonacci순환({Fibonacci_rec}) =", rec_result) #순환(재귀)

#반복순환 비교
for i in range(1,40):
    # 반복 방식 측정
    start = time.time()
    iter_result = fib_iter(i)
    end = time.time()
    iter_time = end - start
    
    # 재귀 방식 측정
    start = time.time()
    rec_result = fib_rec(i)
    end = time.time()
    rec_time = end - start

    # 최종 출력
    print(f"n= {i:2d} \t반복: {iter_time}\t순환: {rec_time:}")