#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/24 21:23
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :   

"""
****************************************************************
Neural Network Module - PyTorch Toolkit
----------------------------------------------------------------
This module provides a collection of neural network architectures
and base classes built with PyTorch, including abstract network
interfaces, model initialisation, forward propagation, model
saving, and model loading utilities.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .abcs import Net

__all__ = [
    "Net",
]
