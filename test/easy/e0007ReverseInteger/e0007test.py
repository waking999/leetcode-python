import unittest
import easy.e0007ReverseInteger.e0007 as m


class TestSolution(unittest.TestCase):

    def test1(self):
        x=123
        expect = 321

        s = m.Solution()
        output = s.reverse(x)
        self.assertEqual(output, expect)

    def test2(self):
        x = -123

        expect = -321

        s = m.Solution()
        output = s.reverse(x)
        self.assertEqual(output, expect)

    def test3(self):
        x = 120
        expect = 21

        s = m.Solution()
        output = s.reverse(x)
        self.assertEqual(output, expect)

    def test5(self):
        x = 1534236469
        expect = 0

        s = m.Solution()
        output = s.reverse(x)
        self.assertEqual(output, expect)




if __name__ == '__main__':
    unittest.main()