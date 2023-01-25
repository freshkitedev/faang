# write a program to find sum of digits of an integer.
def sumofint(n):
    sum = 0
    while(n>0):
        rem = n % 10
        sum = sum + rem
        n = n//10
    return sum    

print(sumofint(154))
