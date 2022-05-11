import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestFixtureExample(BaseClass):

    def test_fixtureDemo1(self):
        log = self.getLogger()
        log.info('testing')
        log.info("I will be executed in fixture demo")
        log.debug("this is debug")


    def test_fixtureDemo2(self):
        print("I will be executed in fixture demo")


    def test_fixtureDemo3(self):
        print("I will be executed in fixture demo")
