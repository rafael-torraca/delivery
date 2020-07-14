import pytest
from delivery.app import create_app

@pytest.fixture(scope="module") #ou function se precisar de testart tudo.
def app():
    """Instance of Main flask app"""
    return create_app()

