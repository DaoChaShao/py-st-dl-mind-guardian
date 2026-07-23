#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/23 17:20
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :   

"""
****************************************************************
Deep Learning Module - PyTorch Toolkit
----------------------------------------------------------------
This module provides a collection of deep learning utilities,
including dataset handling, model training, evaluation metrics,
loss functions, and other PyTorch-related components.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .common import TorchRandomSeed

__all__ = [
    "TorchRandomSeed",
]
