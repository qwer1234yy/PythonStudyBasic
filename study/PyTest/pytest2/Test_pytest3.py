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