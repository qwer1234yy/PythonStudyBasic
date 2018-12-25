import pytest

class calculator(object):

    def add(self, a, b):
        return a+b

    def diff(self, a, b):
        return a+b

    def multible(self, a, b):
        return a+b

    def add(self, a, b):
        return a+b

class Test_pytest(object):

    cal = calculator()

    def setup_module(module):
        print("\n--------------------setup_module--------------------")

    @pytest.fixture()
    def sum(self):
        print('--------------------------smtp---------------:')
        return 1 + 2

    def test_t1(self,sum):
        result = self.cal.add(a=1, b=2)
        assert 9 == result
        print(result)
        print(sum)
        print(type(sum))
        print('test_t1-')

    def test_t2(self):
        print('test_t2-')

    def test_t3(self):
        print('test_t3-')

    def test_t4(self):
        print('test_t4-')

    def test_t5(self):
        print('test_t5-')

    def f(self):
        print('SystemExit')
        raise SystemExit(1)

    def test_mytest(self):
        with pytest.raises(SystemExit):
            self.f()
    # fixture
    def test_tmpdir(self, tmpdir):
        print(tmpdir)

    def test_tmp_path(self, tmp_path):
        print(tmp_path)

    def test_tmp_path_factory(self, tmp_path_factory):
        print(tmp_path_factory)


if __name__ == '__main__':
    pytest.main()
    print('------------')
