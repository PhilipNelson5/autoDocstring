from __future__ import annotations


def function(
    arg1: int,
    arg2: list[str] | dict[str, int] | Thing,
    kwarg1: int | float = 1
) -> list[str] | dict[str, int] | Thing:
    """_summary_

    :param arg1: _description_
    :type arg1: int
    :param arg2: _description_
    :type arg2: list[str] | dict[str, int] | Thing
    :param kwarg1: _description_, defaults to 1
    :type kwarg1: int | float, optional
    :return: _description_
    :rtype: list[str] | dict[str, int] | Thing
    """
    return arg2