#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 22:56
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :   

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from random import seed as rnd_seed, getstate, setstate
from time import perf_counter

WIDTH: int = 64


class Beautifier(object):
    """ beautifying code blocks using a context manager """

    def __init__(self, description: str = None):
        """
        Initialise the Beautifier class
        :param description: the description of a beautifier
        """
        self._description: str = description

    def __enter__(self):
        """ Start the beautifier """
        print("*" * WIDTH)
        print(f"The block named {self._description} is starting:")
        print("-" * WIDTH)
        return self

    def __exit__(self, *args):
        """ Stop the beautifier """
        print("-" * WIDTH)
        print(f"The block named {self._description} has completed.")
        print("*" * WIDTH)
        print()


class Timer(object):
    """ timing code blocks using a context manager """

    def __init__(self, description: str = None, precision: int = 5):
        """
        Initialise the Timer class
        :param description: the description of a timer
        :param precision: the number of decimal places to round the elapsed time
        """
        self._description: str = description
        self._precision: int = precision
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        """ Start the timer """
        self._start = perf_counter()
        print("*" * WIDTH)
        print(f"{self._description} has started.")
        print("-" * WIDTH)
        return self

    def __exit__(self, *args):
        """ Stop the timer and calculate the elapsed time """
        self._end = perf_counter()
        self._elapsed = self._end - self._start

        print("-" * WIDTH)
        print(f"{self._description} took {self._elapsed:.{self._precision}f} seconds.")
        print("*" * WIDTH)

    def __repr__(self):
        """ Return a string representation of the timer """
        if self._elapsed != 0.0:
            return f"{self._description} took {self._elapsed:.{self._precision}f} seconds."

        return f"{self._description} has NOT started."


class RandomSeedForGeneral:
    """ Setting random seed for reproducibility """

    def __init__(self, description: str, seed: int = 27, tick_tock: bool = False) -> None:
        """
        Initialise the RandomSeed class
        :param description: the description of a random seed
        :param seed: the seed value to be set
        :param tick_tock: whether to time the random seed setting
        """
        self._description: str = description
        self._current_seed: int = seed
        self._previous_seed = None

        self._tick: bool = tick_tock
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        """ Set the random seed """
        if self._tick:
            self._start = perf_counter()

        # Save the previous random seed state
        self._previous_seed = getstate()

        # Set the new random seed
        rnd_seed(self._current_seed)

        print("*" * WIDTH)
        print(f"{self._description} has been set to {self._current_seed}.")
        print("-" * WIDTH)

        return self

    def __exit__(self, *args):
        """ Exit the random seed context manager """
        # Restore the previous random seed state
        if self._previous_seed is not None:
            setstate(self._previous_seed)

        # Calculate elapsed time if measuring
        if self._tick:
            self._end = perf_counter()
            self._elapsed = self._end - self._start

        print("-" * WIDTH)
        print(f"{self._description!r} has been restored to previous randomness.")
        if self._tick:
            elapsed_time: str = self._format_time(self._elapsed)
            print(f"{self._description} took {elapsed_time}.")
        print("*" * WIDTH)
        print()

        return False

    @staticmethod
    def _format_time(seconds: float) -> str:
        """
        Format time breakdown from seconds to days, hours, minutes, and seconds
        :param seconds: time in seconds
        :return: formatted time breakdown string
        """
        if seconds < 1.0:
            return f"{seconds * 1000:.1f} ms"

        days: int = int(seconds // 86_400)
        hours: int = int((seconds % 86_400) // 3_600)
        minutes: int = int((seconds % 3_600) // 60)
        secs: float = seconds % 60

        parts: list[str] = []
        if days > 0:
            parts.append(f"{days} days")
        if hours > 0:
            parts.append(f"{hours} hours")
        if minutes > 0:
            parts.append(f"{minutes} minutes")
        if secs > 0 or not parts:
            parts.append(f"{secs:.2f} seconds")

        return " ".join(parts)

    def __repr__(self):
        """ Return a string representation of the random seed """
        base: str = f"PythonRandomSeed({self._description}, seed={self._current_seed})"
        if self._tick and self._elapsed > 0.0:
            base += f", Elapsed Time: {self._elapsed:.2f}s"

        return base


def load_file(file_path: str | Path, *, mode: str = "r", encoding: str = "utf-8", show_content: bool = False) -> str:
    """
    Read content from a file
    :param file_path: Path to the target file.
    :param mode: File opening mode (e.g., 'r').
    :param encoding: Character encoding (e.g., 'utf-8').
    :param show_content: Whether to print the content to console.
    :return: The complete string content of the file.
    """
    with open(str(file_path), mode, encoding=encoding) as file:
        content = file.read()

        if show_content:
            print(f"The content as follows:\n{content}")

    return content


def load_files(file_paths: list[str | Path], *, workers: int = 10) -> list[str]:
    """
    Read multiple files in parallel
    :param file_paths: list of file paths
    :param workers: number of parallel workers
    :return: list of texts extracted from these targets
    """
    with ThreadPoolExecutor(max_workers=workers) as executor:
        contents = list(executor.map(load_file, file_paths))

    return contents


if __name__ == "__main__":
    pass
