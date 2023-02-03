#Find the sum of even and odd positioned digits in a number and subtract summed odd and even number.
#Position is if 456493 is our number then the poition is the index 123456 now take the even and odd positioned number and sum them.
#After the summing the odd and even positoned digits in that number just subtract the even and odd result. 


def Odd_even(num):
    
    q = num #assining the value of num to q.
    even = 0
    odd = 0
    count =0
    while(q != 0):  #First finding the count of the number. condition if the number is not equal to zero (or) if the number is greater than zero
        count+=1    #Incrementing the count variable for every time the loop runs.
        q=q//10     #To truncate (eliminate the last digit in that number so that we would be able to count the number of digits.)

    q = num         #reassining the value of num to q. Because the value of q in now 0 after the above loop.

    while(q != 0):        #Running the untill q is not equal to zero.
        rem = q % 10      #storing the last value in the rem variable.
        if(count%2==0):   #checking the condition if count is odd or even.That is the total number of digits (count)not the value in the rem.
            even += rem   #If even add the current digit to our even variable.
        elif(count%2==1): #If count is odd.
            odd += rem    #Add the current digit to our odd variable.
        q = q // 10       #Eliminating the last digit.
        count-=1          #Decrementing the count by 1 every time the loop runs.

    #To avoid the negative sign infront the result variable we are checking the below condition.
    if(odd>even):         #if odd is greater than even result = odd-even.
        result = odd-even
    elif(even>odd):       #if even is greater than odd result = even-odd.
        result = even-odd

    return odd, even, result #Returning the odd even and result values to the actual variable.


import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = Odd_even(456)
        expected = 10, 5, 5
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = Odd_even(456493)
        expected = 19, 12, 7
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = Odd_even(45)
        expected = 4, 5, 1
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = Odd_even(67895432198765)
        expected = 37, 43, 6
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
