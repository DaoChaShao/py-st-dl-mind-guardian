#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/23 14:51
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :   

"""
****************************************************************
Data Processing Module - Deep Learning Workflow
----------------------------------------------------------------
This package provides utility modules for processing and preparing
datasets for machine learning, NLP, CV, and general data tasks.

Main Categories:
+ preprocess_data : functions and classes for preprocessing data
+ process_data : functions and classes for processing data
+ prepare_data : functions and classes for preparing datasets for training and validation dataloaders
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .preprocessor import preprocess_data
from .prepper import prepare_data

__all__ = [
    "preprocess_data",
    "prepare_data",
]
