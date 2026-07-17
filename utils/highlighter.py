#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 22:56
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   highlighter.py
# @Desc     :   

WIDTH: int = 64


def black(text: int | float | str):
    """
    Highlight text with Black
    :param text: text to be highlighted
    :return: text is highlighted with Black
    """
    if isinstance(text, int):
        return f"\033[1;30m{text:12d}\033[0m"
    elif isinstance(text, float):
        return f"\033[1;30m{text:9.5f}\033[0m"
    else:
        return f"\033[1;30m{text}\033[0m"


def red(text: int | float | str):
    """
    Highlight text with Red
    :param text: text to be highlighted
    :return: text is highlighted with Red
    """
    if isinstance(text, int):
        return f"\033[1;31m{text:12d}\033[0m"
    elif isinstance(text, float):
        return f"\033[1;31m{text:9.5f}\033[0m"
    else:
        return f"\033[1;31m{text}\033[0m"


def green(text: int | float | str):
    """
    Highlight text with Green
    :param text: text to be highlighted
    :return: text is highlighted with Green
    """
    if isinstance(text, int):
        return f"\033[1;32m{text:12d}\033[0m"
    elif isinstance(text, float):
        return f"\033[1;32m{text:9.5f}\033[0m"
    else:
        return f"\033[1;32m{text}\033[0m"


def yellow(text: int | float | str):
    """
    Highlight text with Yellow
    :param text: text to be highlighted
    :return: text is highlighted with Yellow
    """
    if isinstance(text, int):
        return f"\033[1;33m{text:12d}\033[0m"
    elif isinstance(text, float):
        return f"\033[1;33m{text:9.5f}\033[0m"
    else:
        return f"\033[1;33m{text}\033[0m"


def blue(text: int | float | str):
    """
    Highlight text with Blue
    :param text: text to be highlighted
    :return: text is highlighted with Blue
    """
    if isinstance(text, int):
        return f"\033[1;34m{text:12d}\033[0m"
    elif isinstance(text, float):
        return f"\033[1;34m{text:9.5f}\033[0m"
    else:
        return f"\033[1;34m{text}\033[0m"


def purple(text: int | float | str):
    """
    Highlight text with Purple
    :param text: text to be highlighted
    :return: text is highlighted with Purple
    """
    if isinstance(text, int):
        return f"\033[1;35m{text:12d}\033[0m"
    elif isinstance(text, float):
        return f"\033[1;35m{text:9.5f}\033[0m"
    else:
        return f"\033[1;35m{text}\033[0m"


def cyan(text: int | float | str):
    """
    Highlight text with Cyan
    :param text: text to be highlighted
    :return: text is highlighted with Cyan
    """
    if isinstance(text, int):
        return f"\033[1;36m{text:12d}\033[0m"
    elif isinstance(text, float):
        return f"\033[1;36m{text:9.5f}\033[0m"
    else:
        return f"\033[1;36m{text}\033[0m"


def white(text: int | float | str):
    """
    Highlight text with White
    :param text: text to be highlighted
    :return: text is highlighted with White
    """
    if isinstance(text, int):
        return f"\033[1;37m{text:12d}\033[0m"
    elif isinstance(text, float):
        return f"\033[1;37m{text:9.5f}\033[0m"
    else:
        return f"\033[1;37m{text}\033[0m"


def bold(text: int | float | str):
    """
    Bold text
    :param text: text to be bolded
    :return: text is bolded
    """
    return f"\033[1m{text}\033[0m"


def underline(text: int | float | str):
    """
    Underline text
    :param text: text to be underlined
    :return: text is underlined
    """
    return f"\033[4m{text}\033[0m"


def invert(text: int | float | str):
    """
    Invert text color
    :param text: text to be inverted
    :return: text color is inverted
    """
    return f"\033[7m{text}\033[0m"


def strikethrough(text: int | float | str):
    """
    Strikethrough text
    :param text: text to be strikethrough
    :return: text is strikethrough
    """
    return f"\033[9m{text}\033[0m"


def stars(text: str = "", length: int = WIDTH):
    """
    Draw stars
    :param text: text to be written down between stars
    :param length: how many stars to draw
    :return:
    """
    if text:
        left = (length - len(text)) // 2
        right = length - len(text) - left
        print("*" * left + text + "*" * right)
    else:
        print("*" * length)


def lines(text: str = "", length: int = WIDTH):
    """
    Draw lines
    :param text: text to be written down between short lines
    :param length: how many short lines to draw
    :return:
    """
    if text:
        left = (length - len(text)) // 2
        right = length - len(text) - left
        print("-" * left + text + "-" * right)
    else:
        print("-" * length)


def sharps(text: str = "", length: int = WIDTH):
    """
    Draw sharps
    :param text: text to be written down between sharps
    :param length: how many sharps to draw
    :return:
    """
    if text:
        left = (length - len(text)) // 2
        right = length - len(text) - left
        print("#" * left + text + "#" * right)
    else:
        print("#" * length)


if __name__ == "__main__":
    pass
