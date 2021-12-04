# You have an array of non-negative integers,you are initially positioned at the 
# first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine the minimum jumps needed to reach the last index in O(n) Time complexity and O(1) Space Complexity
# Asked in : Adobe Intuit

def minJumpsToEnd(nums): 
    #Practise Yourself :  Write your code Here 
    jump_len = max_jump_len = nums[0]
    jump = 1

    for i in range(1, len(nums) - 1):

        jump_len -= 1
        max_jump_len -= 1

        if(nums[i] > max_jump_len):
            max_jump_len = nums[i]
        
        if (jump_len == 0):
            jump += 1
            jump_len = max_jump_len

    return jump

import unittest
class Test(unittest.TestCase):
  
    def test_MoveZeroToEnd3(self):
        actual = minJumpsToEnd([2,5,1,1,4])
        expected = 2
        self.assertEqual(actual, expected)

    def test_MoveZeroToEnd2(self):
        actual = minJumpsToEnd([2,3,1,1,4])
        expected = 2
        self.assertEqual(actual, expected)

    def test_MoveZeroToEnd1(self):
        actual = minJumpsToEnd([2,2,1,1,4,5,6])
        expected = 4
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
