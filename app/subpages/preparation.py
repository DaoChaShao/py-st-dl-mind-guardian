#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 23:08
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preparation.py
# @Desc     :   

from streamlit import (empty, session_state,
                       sidebar, data_editor)

from utils import CONFIGURATION, load_csv

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

        col: str = sidebar.selectbox(
            "Select a column:",
            COLS,
            index=0, width="stretch",
            help="Select a column to view its data."
        )

        cols: list[str] = [*CONFIGURATION.FEATURES.ID, *getattr(CONFIGURATION.FEATURES, col)]
        COLUMNS: list[str] = session_state["RAW"].columns.tolist()
        columns: list[str] = [
            *CONFIGURATION.FEATURES.ID,
            *CONFIGURATION.FEATURES.TARGET,
            *CONFIGURATION.FEATURES.DEMOGRAPHY,
            *CONFIGURATION.FEATURES.ENVIRONMENT,
            *CONFIGURATION.FEATURES.ACADEMIC,
            *CONFIGURATION.FEATURES.LIFESTYLE,
            *CONFIGURATION.FEATURES.PHYSICAL,
            *CONFIGURATION.FEATURES.PSYCHOLOGY,
            *CONFIGURATION.FEATURES.BEHAVIOUR

        ]

        sidebar.caption(
            f"Selected **{len(set(cols))}** columns, and **{len(set(columns)) - len(set(cols))}** columns left.",
            width="stretch"
        )

        data_editor(
            session_state["RAW"][cols],
            height=680, width="stretch",
            hide_index=True, disabled=True, placeholder="Data Preview"
        )

        NOTIFICATIONS.success(f"{col.upper()} columns has been selected. Data preview loaded successfully!")
