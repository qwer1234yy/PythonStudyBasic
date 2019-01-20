import unittest


class MyTestCase(unittest.TestCase):
    def test_range(self):
        for i in range(1, 5):
            print(i)

    def test_equal(self):
        print(10 == 10)

    def test_dictionary(self):
        dic = {'q': '1', 'w': '2', 'e': '3', 'r': '4'}
        keys = list(dic.keys())
        for i in range(keys.__len__()):
            print(keys[i])


if __name__ == '__main__':
    unittest.main()
