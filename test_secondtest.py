import pytest


@pytest.mark.smoke
def test_motherfucker():
    message = "go to hell"
    assert message == "bitch", "son of a bitch"


@pytest.mark.xfail
def test_predealshorterm():
    message = "Shortterm"
    assert message == "Shortterm", "son of a bitch"
