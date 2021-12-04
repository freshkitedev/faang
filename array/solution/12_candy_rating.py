# There are N children standing in a line with some rating value. You want to distribute a minimum number of candies to these children such that:

# Each child must have at least one candy.
# The children with higher ratings will have more candies than their neighbors.
# You need to write a program to calculate the minimum candies you must give.
class Main:
    def candy(self, ratings):
        if (ratings == None or len(ratings) == 0):
            return 0
        tmp = [0] * len(ratings)
        tmp[0] = 1
        sum = 1
        ratings.sort()

        for i in range(1, len(ratings), 1):
            if (ratings[i] > ratings[i - 1]):
                tmp[i] = tmp[i-1] + 1

            else:
                tmp[i] = 1
            sum += tmp[i]

        return sum

    def candy1(self, ratings):
        if (ratings == None or len(ratings) == 0):
            return 0

        left = [0] * len(ratings)
        left[0] = 1
        right = [0] * len(ratings)
        right[len(ratings)-1] = 1
        result = 0

        for i in range(1, len(ratings), 1):
            if (ratings[i] > ratings[i - 1]):
              left[i] = left[i - 1] + 1
            else:
              left[i] = 1

        for i in range(len(ratings) - 2, -1, -1):
            cur = 1
            if (ratings[i] > ratings[i + 1]):
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1

        for i in range(0, len(ratings), 1):
            result += max(right[i], left[i])

        return result

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
