import pytest

from unittest import mock

from app.main import check_password


def data_gen() -> list:
    return [
        ("Pass@word1", True),
        ("P@word1", False),
        ("Pa+ss@word1", False),
        ("ddddddddd", False),
        ("111111111", False),
        ("МММММММММ", False),
        ("Аd1ddddddd", False),
    ]


data_set = data_gen()


def gen_keys(data_set: list) -> str:
    password, expected = data_set
    return (f"if password = {password}, "
            f"result {expected}")


@pytest.mark.parametrize("dataset",
                         data_set,
                         ids=gen_keys)
def test_check_password(dataset: mock.MagicMock) -> None:
    password, expected = dataset
    assert check_password(password) == expected
