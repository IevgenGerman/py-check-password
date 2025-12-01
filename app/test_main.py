import pytest

from typing import Tuple

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
        ("Pass@word1qweqweqweqwqweqwe", False),
        ("Aa1$aaaaasssssss", True),
        ("aaaaaa1$", False),
        ("aaaaa1$", False),

    ]


data_for_test = data_gen()


def gen_keys(data_set: list) -> str:
    password, expected = data_set
    return (fr"if password = {repr(password)}, "
            f"result {expected}")


@pytest.mark.parametrize("dataset",
                         data_for_test,
                         ids=gen_keys)
def test_check_password(dataset: Tuple[str, bool]) -> None:
    password, expected = dataset
    assert check_password(password) == expected
