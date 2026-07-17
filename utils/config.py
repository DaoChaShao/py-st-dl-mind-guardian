#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 22:52
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   config.py
# @Desc     :   

from dataclasses import dataclass, field
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass
class Database:
    USER: str = ""
    PASSWORD: str = ""
    HOST: str = ""
    PORT: str = ""


@dataclass
class FilePaths:
    API_KEY: Path = BASE_DIR / "data" / "api_keys.yaml"
    DATA: Path = BASE_DIR / "data" / "Student_Psychological_Crisis_Dataset.csv"
    LOGS: Path = BASE_DIR / "logs"
    SQLITE: Path = BASE_DIR / "data" / "sqlite3.db"


@dataclass
class Punctuations:
    CN: tuple[str, ...] = (
        "，", "。", "？", "！", "、", "；", "：", "「", "」", "『", "』",
        "《", "》", "（", "）", "【", "】", "｛", "｝", "－", "～", "·",
        "…", "——", "〝", "〞", "＂", "＇", "＇", "‘", "’", "“", "”",
        "〈", "〉", "〖", "〗", "〔", "〕", "〘", "〙", "〚", "〛"
    )
    EN: tuple[str, ...] = (
        ",", ".", "?", "!", ";", ":", "'", '"', "(", ")", "[", "]",
        "{", "}", "-", "~", "`", "@", "#", "$", "%", "^", "&", "*",
        "_", "+", "=", "<", ">", "/", "\\", "|"
    )


@dataclass
class BaseConfig:
    DATABASE: Database = field(default_factory=Database)
    FILE_PATHS: FilePaths = field(default_factory=FilePaths)
    PUNCTUATIONS: Punctuations = field(default_factory=Punctuations)


BASE_CONFIG = BaseConfig()
