import pytest

#  Put scope="class" in the fixture, then this setup method will only run before the class only one time
# Else it will run after each method

@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed after the dixturedemo")
