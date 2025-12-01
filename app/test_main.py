import pytest

from typing import Union

from app.main import check_password


def data_gen() -> list:
    return [
        ("Pass@wor1", True),
        ("P@word1", False),
        ("P@word1s", True),
        ("p@word1s", False),
        ("Pa+ss@word1", False),
        ("ddddddddd", False),
        ("111111111", False),
        ("МММММММММ", False),
        ("Аd1ddddddd", False),
        ("Pass@word1qweqweq", False),
        ("Aa1$aaaaasssssss", True),
        ("Pass@word1qweqweq", False),
        (None, TypeError),
        (4546535, TypeError),
        ("Valid@Pass", False)

    ]


data_for_test = data_gen()


def gen_keys(data_set: list) -> str:
    password, expected = data_set
    return (f"if password = {repr(password)}, "
            f"result {expected}")


@pytest.mark.parametrize("dataset",
                         data_for_test,
                         ids=gen_keys)
def test_check_password(dataset: tuple) -> None:
    password, expected = dataset
    if expected == TypeError:
        with pytest.raises(TypeError):
            check_password(password)
    else:
        assert check_password(password) == expected
