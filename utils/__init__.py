#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 22:50
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :   

"""
****************************************************************
Utility Module - Comprehensive Toolkit
----------------------------------------------------------------
This module provides a comprehensive suite of utility functions
and classes designed for general data processing tasks.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .apis import verify_api_key, OpenAIEmbedder, OpenAITextCompleter, DeepSeekCompleter
from .config import CONFIGURATION
from .decorator import beautifier, timer
from .helper import (Beautifier, Timer,
                     RandomSeed,
                     load_file, load_files)
from .highlighter import (black, red, green, yellow, blue, purple, cyan, white,
                          bold, underline, invert, strikethrough,
                          stars, lines, sharps)
from .stats import (NumpyRandomSeed,
                    load_csv,
                    check_labels_distribution, encode_labels,
                    split_data,
                    create_features_transformer, fit_features_transformer, transform_features,
                    compute_labels_weights, )

__all__ = [
    "verify_api_key",
    "OpenAIEmbedder",
    "OpenAITextCompleter",
    "DeepSeekCompleter",

    "CONFIGURATION",

    "beautifier",
    "timer",

    "Beautifier",
    "Timer",
    "RandomSeed",
    "load_file",
    "load_files",

    "black", "red", "green", "yellow", "blue", "purple", "cyan", "white",
    "bold", "underline", "invert", "strikethrough",
    "stars", "lines", "sharps",

    "NumpyRandomSeed",
    "load_csv",
    "check_labels_distribution", "encode_labels",
    "split_data",
    "create_features_transformer", "fit_features_transformer", "transform_features",
    "compute_labels_weights",
]
