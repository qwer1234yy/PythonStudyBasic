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
    def test_file_write(self):
        try:
            f = open('../SMART/Smart_commons/cs_operators.txt', 'a')
            # f.writelines('testsetstst')
            print(f.read(100))
        finally:
            if f:
              f.close()


if __name__ == '__main__':
    unittest.main()
