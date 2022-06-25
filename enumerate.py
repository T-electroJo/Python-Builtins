def enumerate(iterable: Iterable) -> list[tuple[int, Any]]:
    _out: list[tuple[int, Any]] = []
    for _i in range(len(iterable)):
        _out.append(tuple([_i, iterable[_i]]))
    return _out
