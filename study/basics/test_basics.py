import unittest


class MyTestCase(unittest.TestCase):
    def test_range(self):
        for i in range(1,5):
            print(i)
    def test_equal(self):
        print(10 == 10)


if __name__ == '__main__':
    unittest.main()
