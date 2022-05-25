def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
n=int(input("enter the number of terms:"))
if n<=0:
    print("please enter positive number:")
else:
    print("fibonacci sequence:")
    for i in range(n):
      print(fib(i))  