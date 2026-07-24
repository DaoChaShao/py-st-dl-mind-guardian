#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/24 15:23
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   tensors.py
# @Desc     :   

from numbers import Number
from numpy import ndarray, array
from pandas import DataFrame, Series
from typing import Literal

from torch import Tensor, tensor, long, float32


def item2tensor(
        data: DataFrame | Series | ndarray | list | Number,
        *,
        is_long: bool = False,
        is_grad: bool = False,
        accelerator: str | Literal["cpu", "cuda", "mps"] = "cpu",
        display: bool = True
) -> Tensor:
    """
    Convert data to a PyTorch tensor
    :param data: data to be converted
    :param is_long: whether the tensor dtype is long
    :param is_grad: whether the tensor requires gradient computation
    :param accelerator: the target device string ("cpu", "cuda", "mps")
    :param display: whether to display the tensor shape and dtype
    :return: the converted PyTorch tensor
    """
    # Convert DataFrame, Series or list to ndarray
    if isinstance(data, (DataFrame, Series)):
        arr = data.to_numpy()
    elif isinstance(data, ndarray):
        arr = data
    elif isinstance(data, list):
        arr = array(data, dtype=float)
    elif isinstance(data, Number):
        arr = array([data], dtype=float)
    else:
        raise TypeError(f"Unsupported data type: {type(data)}")

    # Convert to tensor with appropriate dtype
    if is_long:
        t = tensor(arr, dtype=long, device=accelerator)
    else:
        t = tensor(arr, dtype=float32, device=accelerator, requires_grad=is_grad)

    if display: print(f"The tensor shape is {t.shape}, and its dtype is {t.dtype}.")

    return t
