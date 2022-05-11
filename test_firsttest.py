import pytest


@pytest.mark.smoke
def test_demomethod():
    print("hello")


@pytest.mark.skip
def test_demofucker():
    print("fuckyou")
