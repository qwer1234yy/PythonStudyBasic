import unittest


class MyTestCase(unittest.TestCase):
    def test_math(self):
        print(2**6)
    def test_range(self):
        for i in range(0, 1):
            print(i)

    def test_equal(self):
        print(10 == 10)

    def test_dictionary(self):
        dic = {'q': '1', 'w': '2', 'e': '3', 'r': '4'}
        keys = list(dic.keys())
        for i in range(keys.__len__()):
            print(keys[i])

    def test_list(self):
        list_ = [1, 2, 5, 6]
        list_.insert(2, 3)
        list_.insert(3, 4)
        print(list_.__len__())
        for i in list_:
            if i == 2:
                list_.insert(2, 3)
            if i == 3:
                list_.insert(3, 4)




if __name__ == '__main__':
    unittest.main()
