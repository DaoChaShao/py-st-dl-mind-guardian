#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/23 17:30
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   common.py
# @Desc     :   

from numpy import random as np_random
from random import seed as rnd_seed, getstate, setstate
from time import perf_counter
from torch import (manual_seed, get_rng_state, set_rng_state,
                   cuda, backends, )

WIDTH: int = 64


class TorchRandomSeed:
    """ Setting random seed for reproducibility """

    def __init__(self, description: str, *, seed: int = 27, tick_tock: bool = False) -> None:
        """ Initialise the RandomSeed class
        :param description: the description of a random seed
        :param seed: the seed value to be set
        :param tick_tock: whether to print timing information
        :return: None
        """
        self._description: str = description
        self._seed: int = seed

        # Set Python seed
        self._previous_py_seed = None
        # Set NumPy seed
        self._previous_np_seed = None
        # Set PyTorch seed
        self._previous_pt_seed = None
        # Set CUDA seed
        self._previous_cd_seed = None

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
        self._previous_pt_seed = get_rng_state()
        self._previous_np_seed = np_random.get_state()
        if cuda.is_available():
            self._previous_cd_seed = cuda.get_rng_state_all()

        # Set a random seed on CPU
        rnd_seed(self._seed)
        manual_seed(self._seed)
        np_random.seed(self._seed)

        # Set a random seed on GPU
        if cuda.is_available():
            cuda.manual_seed(self._seed)
            cuda.manual_seed_all(self._seed)
            backends.cudnn.deterministic = True
            backends.cudnn.benchmark = False

        print("*" * WIDTH)
        print(f"{self._description} has been set to {self._seed}.")
        print("-" * WIDTH)

        return self

    def __exit__(self, *args):
        """ Exit the random seed context manager """
        # Restore the previous CPU random seed state
        if self._previous_py_seed is not None:
            setstate(self._previous_py_seed)
        if self._previous_pt_seed is not None:
            set_rng_state(self._previous_pt_seed)
        if self._previous_np_seed is not None:
            np_random.set_state(self._previous_np_seed)
        # Restore the previous CUDA random seed state
        if cuda.is_available() and self._previous_cd_seed is not None:
            cuda.set_rng_state_all(self._previous_cd_seed)

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
        """ Format time breakdown from seconds to days, hours, minutes, and seconds
        :param seconds: time in seconds
        :return: formatted time breakdown string
        """
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

    def __repr__(self) -> str:
        """ Return a string representation of the random seed """
        base: str = f"TorchRandomSeed({self._description}, seed={self._seed})"
        if self._tick and self._elapsed > 0.0:
            base += f", Elapsed Time: {self._elapsed:.2f} s"

        return base
