#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 23:07
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preview.py
# @Desc     :   

from pandas import DataFrame, Series
from streamlit import (empty, session_state,
                       sidebar, data_editor,
                       columns, metric)

from utils import BASE_CONFIG, load_csv

NOTIFICATIONS = empty()
DISPLAYER = empty()

if "RAW" not in session_state:
    session_state["RAW"] = None

if sidebar.button("Load the Psychological Data", type="primary", width="stretch"):
    session_state["RAW"]: DataFrame = load_csv(BASE_CONFIG.FILE_PATHS.DATA, dis_summary=True)

if sidebar.button("Clear the Data", type="secondary", width="stretch"):
    session_state["RAW"] = None

if session_state["RAW"] is None:
    NOTIFICATIONS.warning("Data not loaded yet. Please load the data first.")
else:
    dup_rows: int = session_state["RAW"].duplicated().sum()
    miss_values: int = session_state["RAW"].isnull().sum().sum()
    left, right = columns(2)
    with left:
        metric("Duplicate Rows", dup_rows, help="Number of duplicate rows in the dataset")
    with right:
        metric("Missing Values", miss_values, help="Number of missing values in the dataset")

    data_editor(
        session_state["RAW"],
        height=600, width="stretch",
        hide_index=True, disabled=True, placeholder="Data Preview"
    )

    NOTIFICATIONS.success("Data preview loaded successfully!")
