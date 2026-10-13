def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(20):
    print(f"{fib(i):>5}",end="")
    if((i+1)%10==0):
        print()
