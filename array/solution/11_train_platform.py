# List of arrival and departure time is given, 
# Find the minimum number of platforms are required for the railway as no train waits
def minimumNumberPlatform(arrival, departure, n): 
    
    #Practise Yourself :  Write your code Here
    arrival.sort() 
    departure.sort() 
    # plat_needed indicates number of platforms needed at a time 
    plat_needed = 1
    minplatform = 1
    i = 1
    j = 0
   
    while (i < n and j < n): 
      # If next event in sorted order is arrival, increment count of platforms needed
        if (arrival[i] <= departure[j]): 
            plat_needed+= 1
            i+= 1
            if (plat_needed > minplatform):  
               minplatform = plat_needed
        # Else decrement count of platforms needed 
        elif (arrival[i] > departure[j]): 
            plat_needed-= 1
            j+= 1
  
    return minplatform 
  

import unittest

class Test(unittest.TestCase):
    def test_printfrequency_1(self):
        actual = minimumNumberPlatform([100,140,150,200,215,400],[110, 300, 220, 230, 315, 600],6)
        expected = 4
        self.assertEqual(actual, expected)

    def test_printfrequency_2(self):
        actual = minimumNumberPlatform([900,940,950,1100,1500,1800],[910, 1200, 1120, 1130, 1900, 2000],6)
        expected = 3
        self.assertEqual(actual, expected)

    def test_printfrequency_3(self):
        actual = minimumNumberPlatform([200, 210, 300, 320, 350, 500],[230, 340, 320, 430, 400, 520],6)
        expected = 3
        self.assertEqual(actual, expected)

    def test_printfrequency_4(self):
        actual = minimumNumberPlatform([900, 1100, 1235],[1000, 1200, 1240],3)
        expected = 1
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)