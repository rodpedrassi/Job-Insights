from src.pre_built.counter import count_ocurrences
import pytest
from unittest.mock import mock_open, patch


@pytest.fixture
def file():
    return """
    teste
    teste
    teste
    """


def test_words_counter(file):
    with patch("builtins.open", mock_open(read_data=file)):
        assert count_ocurrences("path_mock", "teste") == 3
