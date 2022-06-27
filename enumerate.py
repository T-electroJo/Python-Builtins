from typing import Any, Iterable


def enumerate(iterable: Iterable) -> list:
    _out = []
    for _i in range(len(iterable)):
        _out.append(tuple([_i, iterable[_i]]))
    return _out