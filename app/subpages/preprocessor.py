#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/18 14:20
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preprocessor.py
# @Desc     :   

from pandas import DataFrame
from streamlit import (empty, session_state,
                       write,
                       sidebar, data_editor)

from app.tools import check_data_dtypes
from utils import CONFIGURATION, check_labels_distribution, compute_labels_weights

NOTIFICATIONS = empty()
DISPLAYER = empty()

if "RAW" not in session_state:
    NOTIFICATIONS.error("Data not loaded yet. Please load the data first.")
else:
    if session_state["RAW"] is None:
        NOTIFICATIONS.warning("No data loaded. Please load the data first.")
    else:
        session_state["DATA"] = session_state["RAW"].copy()

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

        col: str = sidebar.selectbox(
            "Select a column:",
            COLS,
            index=0, width="stretch",
            help="Select a column to view its data."
        )

        if sidebar.button("View Data Type", type="primary", width="stretch"):
            write(check_data_dtypes(session_state["DATA"][getattr(CONFIGURATION.FEATURES, col)]))
            write(check_labels_distribution(session_state["DATA"]["Psychological_Risk_Level"]))
            write(compute_labels_weights(session_state["DATA"]["Psychological_Risk_Level"]))
