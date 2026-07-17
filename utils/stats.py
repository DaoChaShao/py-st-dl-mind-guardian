#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 22:57
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   stats.py
# @Desc     :   

from numpy import random as np_random
from pandas import DataFrame, Series, read_csv
from pathlib import Path
from random import seed as rnd_seed, getstate, setstate
from time import perf_counter

from utils.decorator import timer

WIDTH: int = 64


class RandomSeedForNumpy:
    """ Setting numpy random seed for reproducibility """

    def __init__(self, description: str, seed: int = 27, tick_tock: bool = False):
        """
        Initialise the RandomSeed class
        :param description: the description of a random seed
        :param seed: the seed value to be set
        :param tick_tock: whether to measure elapsed time
        """
        self._description: str = description
        self._seed: int = seed
        self._previous_py_seed = None
        self._previous_np_seed = None

        self._tick: bool = tick_tock
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        """ Set the random seed """
        if self._tick:
            self._start = perf_counter()

        # Save the previous random seed state
        self._previous_py_seed = getstate()
        self._previous_np_seed = np_random.get_state()

        # Set the new random seed
        rnd_seed(self._seed)
        np_random.seed(self._seed)

        print("*" * WIDTH)
        print(f"{self._description} has been set to {self._seed}.")
        print("-" * WIDTH)

        return self

    def __exit__(self, *args):
        """ Exit the random seed context manager """
        # Restore the previous random seed state
        if self._previous_py_seed is not None:
            setstate(self._previous_py_seed)
        if self._previous_np_seed is not None:
            np_random.set_state(self._previous_np_seed)

        # Calculate elapsed time if measuring
        if self._tick:
            self._end = perf_counter()
            self._elapsed = self._end - self._start

        print("-" * WIDTH)
        print(f"{self._description} has been restored to previous randomness.")
        if self._tick:
            elapsed_time: str = self._format_time(self._elapsed)
            print(f"{self._description} took {elapsed_time}.")
        print("*" * WIDTH)
        print()

        # Return False to propagate exceptions, True to suppress them
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

        days: int = int(seconds // 86400)
        hours: int = int((seconds % 86400) // 3600)
        minutes: int = int((seconds % 3600) // 60)
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
        base: str = f"NumpyRandomSeed(description={self._description}, seed={self._seed})"
        if self._tick and self._elapsed > 0:
            base += f", Elapsed Time: {self._elapsed:.2f} s"

        return base


@timer
def load_csv(csv_path: str | Path, *, dis_content: bool = True, dis_summary: bool = False) -> DataFrame:
    """
    Read data from a dataset file
    :param csv_path: Target path to the file.
    :param dis_content: Toggle for printing the first few rows.
    :param dis_summary: Toggle for basic statistics and quality checks.
    :return: Loaded Pandas DataFrame.
    """
    dataset: DataFrame = read_csv(str(csv_path))

    if dis_content:
        print(dataset.head())

    if dis_summary:
        print(dataset.describe())

        dup_rows: int = dataset.duplicated().sum()
        miss_values: int = dataset.isnull().sum().sum()
        miss_details: Series = dataset.isnull().sum()[dataset.isnull().sum() > 0]
        print(f"Duplicated Rows: {dup_rows}")
        print(f"Missing Values: {miss_values}")
        print(f"Missing Values Details: \n{miss_details}")

    return dataset


if __name__ == "__main__":
    pass
