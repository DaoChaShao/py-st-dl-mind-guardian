#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 23:04
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   layout.py
# @Desc     :   


from streamlit import set_page_config, Page, navigation


def config_page() -> None:
    """ Set the window
    :return: None
    """
    set_page_config(
        page_title="Fitness Monitoring & Injury Prevention",
        page_icon=":material/globe:",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def set_pages() -> None:
    """ Set the subpages on the sidebar (https://fonts.google.com/icons)
    :return: None
    """
    pages: dict = {
        "page": [
            "app/subpages/home.py",
            "app/subpages/preview.py",
            "app/subpages/preparation.py",
            "app/subpages/preprocessor.py"
        ],
        "title": [
            "Home",
            "Data Preview",
            "Data Preparation",
            "Data Preprocessing"
        ],
        "icon": [
            ":material/home:",
            ":material/dashboard:",
            ":material/dashboard_2_gear:",
            ":material/database:"
        ],
    }

    structure: dict = {
        "Introduction": [
            Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
        ],
        "Core Functions": [
            Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
            Page(page=pages["page"][2], title=pages["title"][2], icon=pages["icon"][2]),
            Page(page=pages["page"][3], title=pages["title"][3], icon=pages["icon"][3]),
        ],
    }
    pg = navigation(structure, position="sidebar", expanded=True)
    pg.run()
