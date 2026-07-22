#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/18 17:26
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   lever.py
# @Desc     :   

from pandas import DataFrame


def check_data_dtypes(data: DataFrame) -> DataFrame:
    """
    Check the data types of the columns in the data.
    :param data: DataFrame to check
    :return: DataFrame containing the data types of the columns
    """
    return data.dtypes.astype(str).to_frame("dtype")
