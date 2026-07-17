#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 23:03
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :   

from streamlit import title, expander, caption, empty

empty_message = empty()
empty_message.info("Please check the details at the different pages of core functions.")

title("Mind Guardian")
with expander("**INTRODUCTION (CN)**", expanded=False):
    caption("+ ")

with expander("**INTRODUCTION (EN)**", expanded=True):
    caption("+ ")
