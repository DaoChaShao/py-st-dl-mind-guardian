#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/23 14:53
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   prepper.py
# @Desc     :   

from pipeline import preprocess_data


def prepare_data():
    """
    Prepare data for training, validation and testing dataloaders for the model
    :return:
    """
    # Get preprocessed data
    encoder, processor, X_train, X_valid, X_test, y_train, y_valid, y_test = preprocess_data()


if __name__ == "__main__":
    prepare_data()
