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
class Features:
    ID: list[str] = field(default_factory=lambda: ["Student_ID", ])
    TARGET: list[str] = field(default_factory=lambda: ["Psychological_Risk_Level", ])
    DEMOGRAPHY: list[str] = field(default_factory=lambda: ["Age", "Gender", "Socioeconomic_Status"])
    ENVIRONMENT: list[str] = field(default_factory=lambda: [
        "Family_Cohesion",
        "Social_Support",
        "Bullying_Victimization",
        "Romantic_Relationship_Status",
        "Teacher_Student_Support",
        "Family_Income",
        "Parental_Occupation_Stability",
        "Financial_Stress",
        "Scholarship_Status",
        "Housing_Quality",
    ])
    ACADEMIC: list[str] = field(default_factory=lambda: [
        "GPA",
        "Test_Score",
        "Course_Load",
        "Class_Attendance",
        "Academic_Pressure",
        "Study_Hours",
        "Homework_Completion",
        "Teacher_Feedback_Score",
    ])
    LIFESTYLE: list[str] = field(default_factory=lambda: [
        "Social_Media_Usage_Hours",
        "Social_Interaction_Hours",
        "Sleep_Quality",
        "Sleep_Duration",
        "Physical_Activity_Hours",
        "Diet_Quality",
        "Screen_Time_Hours",
        "Phone_Unlock_Frequency",
        "App_Switch_Frequency",
    ])
    PHYSICAL: list[str] = field(default_factory=lambda: [
        "Chronic_Health_Issues",
        "BMI",
        "Energy_Level",
        "Medical_Consultations",
        "Resting_Heart_Rate",
        "Heart_Rate_Variability",
    ])
    PSYCHOLOGY: list[str] = field(default_factory=lambda: [
        "Stress_Score",
        "Anxiety_Score",
        "Depression_Score",
        "Loneliness_Score",
        "Negative_Sentiment_Score",
    ])
    BEHAVIOUR: list[str] = field(default_factory=lambda: [
        "Social_Media_Usage_Hours",
        "Social_Interaction_Hours",
        "Study_Hours",
        "Homework_Completion",
        "Class_Attendance",
        "Sleep_Duration",
        "Sleep_Quality",
        "Physical_Activity_Hours",
        "Diet_Quality",
        "Screen_Time_Hours",
        "Phone_Unlock_Frequency",
        "App_Switch_Frequency",
    ])


@dataclass
class Configuration:
    DATABASE: Database = field(default_factory=Database)
    FILE_PATHS: FilePaths = field(default_factory=FilePaths)
    PUNCTUATIONS: Punctuations = field(default_factory=Punctuations)

    FEATURES: Features = field(default_factory=Features)


CONFIGURATION = Configuration()
