import pytest

def setup_module():
    print('\n *** 初始化-模块 ***')

def teardown_module():
    print('\n *** 清除-模块 ***')


class Test_demo1:

    @classmethod
    def setup_class(cls):
        print('\n === 初始化 - 类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')

    def setup_method(self):
        print('\n ... 初始化 - 方法 ...')

    def teardown_method(self):
        print('\n ... 清除 - 方法 ...')

    def test_c001(self):
        print('\n用例c001')
        assert 1 == 1

    def test_c002(self):
        print('\n用例c002')
        assert 2 == 2

    @pytest.mark.jevons
    def test_c003(self):
        print('\n用例c003')
        assert 3 == 3


class Test_demo2:

    def test_c011(self):
        print('\n用例c011')
        assert 11 == 11

    def test_c012(self):
        print('\n用例c012')
        assert 12 == 12
