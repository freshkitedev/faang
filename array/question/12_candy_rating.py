# There are N children standing in a line with some rating value. You want to distribute a minimum number of candies to these children such that:

# Each child must have at least one candy.
# The children with higher ratings will have more candies than their neighbors.
# You need to write a program to calculate the minimum candies you must give.
class Main:
    def candy(self, ratings):
        # code here

import unittest
class Test(unittest.TestCase):
  def test_findElement1(self):
      m = Main()
      ratings = [1, 5, 2, 1]
      actual = m.candy(ratings)
      expected = 7
      self.assertEqual(actual, expected)
  def test_findElement2(self):
      m = Main()
      ratings = [1, 5, 2, 1, 4]
      actual = m.candy(ratings)
      expected = 11
      self.assertEqual(actual, expected)
unittest.main(verbosity=2)
