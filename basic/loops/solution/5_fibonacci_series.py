#Write a program to print fibonacci series....



def fibonacci(n):
    a=0
    b=1
    c = 0
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        print(a,end=" ")
        print(b,end=" ")
        while(c < n):
            c=a+b
            a=b
            b=c
            print(c,end=" ")
       


fib = fibonacci(5)