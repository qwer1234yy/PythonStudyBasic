import unittest


class MyTestCase(unittest.TestCase):
    def test_IO_first(self):
        try:
            f = open('../resources_collect/note.txt', 'r')
            print("fffffffffffffffffffff")
            print(f.read())
        finally:
            if f:
              f.close()


if __name__ == '__main__':
    unittest.main()
