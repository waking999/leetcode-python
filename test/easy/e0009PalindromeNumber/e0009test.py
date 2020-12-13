import unittest
import easy.e0009PalindromeNumber.e0009 as m


class TestSolution(unittest.TestCase):

    def test1(self):
        x = 121
        expect = True

        s = m.Solution()
        output = s.isPalindrome(x)
        self.assertEqual(output, expect)

    def test2(self):
        x = -121
        expect = False

        s = m.Solution()
        output = s.isPalindrome(x)
        self.assertEqual(output, expect)

    def test3(self):
        x = 10
        expect = False

        s = m.Solution()
        output = s.isPalindrome(x)
        self.assertEqual(output, expect)

    def test4(self):
        x = -101
        expect = False

        s = m.Solution()
        output = s.isPalindrome(x)
        self.assertEqual(output, expect)


if __name__ == '__main__':
    unittest.main()
