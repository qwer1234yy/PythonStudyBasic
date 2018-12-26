import pytest

# content of test_class.py
class TestClass:

    def func(x):
        return x + 1

    def test_answer(self):
        assert self.func(3) == 5

    def test_one(self):
        print ('one')
        x = "this"
        assert 'h' in x

    def test_two(self):
        print ('two')
        x = "hello"
        assert hasattr(x, 'check')
if __name__ == '__main__':
    pytest.main()