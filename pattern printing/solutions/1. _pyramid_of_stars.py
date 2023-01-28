# Write a program to print the pyramid of stars for the given rows ?
#First enter the number of rows to print the pyramid of stars.
#Find the columns for the rows.
#expected result for five rows
#                  *
#                 ***
#                *****
#               *******
#              *********


def printPyramid(row):#this is our function.
    for i in range(1, row+1):#this loop will run from 1 to row times to print the rows.
        for j in range(1, row*2):#this loop will run from 1 to (2*rows)-1 times to print the columns.
            if (j <= (row-i) or j >= (row +i)):#this is our condition to print if this condition is satisfied then it will print the empty space.
                print(" ", end = "")
            else:
                print('*', end = "")#if our condition is not satisfied then it will print the star, this end inside the print statement will not allow to jump to the new line and print in the same line.
        print()#this will enter the new line.



row = int(input("enter the number of rows to print the pyramid: "))#getting the input from the user and convertin it to
printPyramid(row)#calling the function.


