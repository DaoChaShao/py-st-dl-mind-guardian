#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 23:08
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preparation.py
# @Desc     :   

from pandas import DataFrame
from streamlit import (empty, session_state,
                       selectbox, data_editor,
                       columns, metric,
                       sidebar)

from utils import BASE_CONFIG, load_csv

NOTIFICATIONS = empty()
DISPLAYER = empty()

if "RAW" not in session_state:
    NOTIFICATIONS.error("Data not loaded yet. Please load the data first.")
else:
    if session_state["RAW"] is None:
        NOTIFICATIONS.warning("No data loaded. Please load the data first.")
    else:
        COLS: list[str] = [
            "TARGET",
            "DEMOGRAPHY",
            "ENVIRONMENT",
            "ACADEMIC",
            "LIFESTYLE",
            "PHYSICAL",
            "PSYCHOLOGY",
            "BEHAVIOUR"
        ]

        left, right = columns([3, 1])
        with left:
            col: str = selectbox(
                "Select a column:",
                COLS,
                index=0, width="stretch",
                help="Select a column to view its data."
            )

        cols: list[str] = [*BASE_CONFIG.FEATURES.ID, *getattr(BASE_CONFIG.FEATURES, col)]
        COLUMNS: list[str] = session_state["RAW"].columns.tolist()
        columns: list[str] = [
            *BASE_CONFIG.FEATURES.ID,
            *BASE_CONFIG.FEATURES.TARGET,
            *BASE_CONFIG.FEATURES.DEMOGRAPHY,
            *BASE_CONFIG.FEATURES.ENVIRONMENT,
            *BASE_CONFIG.FEATURES.ACADEMIC,
            *BASE_CONFIG.FEATURES.LIFESTYLE,
            *BASE_CONFIG.FEATURES.PHYSICAL,
            *BASE_CONFIG.FEATURES.PSYCHOLOGY,
            *BASE_CONFIG.FEATURES.BEHAVIOUR

        ]

        with right:
            metric(
                "Selected Column Number",
                value=len(set(cols)),
                delta=f"{len(set(columns)) - len(set(cols))} left",
                delta_color="blue",
                help="The number of columns selected and the number of columns left to select."
            )

        data_editor(
            session_state["RAW"][cols],
            height=560, width="stretch",
            hide_index=True, disabled=True, placeholder="Data Preview"
        )

        NOTIFICATIONS.success(f"{col.upper()} columns has been selected. Data preview loaded successfully!")
