import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    BooksCollector()
    return BooksCollector()
