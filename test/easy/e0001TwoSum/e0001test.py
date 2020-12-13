import unittest
import easy.e0001TwoSum.e0001 as m


class TestSolution(unittest.TestCase):

    def test1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expect = [0, 1]

        s = m.Solution()
        output = s.twoSum(nums, target)
        self.assertEqual(output, expect)

    def test2(self):
        nums = [3,2,4]
        target = 6
        expect = [1, 2]

        s = m.Solution()
        output = s.twoSum(nums, target)
        self.assertEqual(output, expect)

    def test3(self):
        nums = [3,3]
        target = 6
        expect = [0, 1]

        s = m.Solution()
        output = s.twoSum(nums, target)
        self.assertEqual(output, expect)


if __name__ == '__main__':
    unittest.main()
