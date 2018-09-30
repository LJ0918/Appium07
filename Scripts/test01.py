import allure
import pytest


class TestAllure():
    @allure.step('执行学院更新操作')
    def test001(self):
        allure.attach('开始断言','学院是否更新成功')
        print('test001被执行')
        allure.attach('断言结束','断言成功')

    @allure.step('执行学院删除操作')
    def test002(self):
        print('test002被执行')

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test003(self):
        print('test003被执行')
        assert False
    def test004(self):
        print('test004被执行')