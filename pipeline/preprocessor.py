#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/23 14:54
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preprocessor.py
# @Desc     :   

from pandas import DataFrame, Series

from utils import (load_csv, CONFIGURATION,
                   check_labels_distribution,
                   encode_labels,
                   split_data,
                   create_features_transformer, fit_features_transformer, transform_features)


def preprocess_data() -> tuple:
    """
    Preprocess the data by loading, splitting, encoding labels, and transforming features.
    :return: A tuple containing train, validation, and test sets along with the train, validation, and test labels.
    """
    # Load the raw data
    raw: DataFrame = load_csv(CONFIGURATION.FILE_PATHS.DATA)
    print(f"Raw Data Shape: {raw.shape}")

    # Get the features from the raw data without id and target columns
    X: DataFrame = raw.drop(CONFIGURATION.FEATURES.ID + CONFIGURATION.FEATURES.TARGET, axis=1)
    print(f"X Shape: {X.shape}")
    # Get the target variable from the raw data
    y: Series = raw[CONFIGURATION.FEATURES.TARGET].squeeze()
    print(f"y Shape: {y.shape}")

    # Check the labels distribution
    check_labels_distribution(y)

    # Encode the labels
    y, encoder = encode_labels(y)

    # Split the data into training validation and testing sets
    X_train, X_valid, X_test, y_train, y_valid, y_test = split_data(X, y)

    # Create a feature transformer
    transformer = create_features_transformer(X_train)
    # Fit ONLY on train feature with the transformer
    processor = fit_features_transformer(X_train, transformer=transformer)
    # Transform the train, validation and test sets
    fitted_X_train = processor.transform(X_train)
    fitted_X_valid = processor.transform(X_valid)
    fitted_X_test = processor.transform(X_test)

    # Transform the features
    transformed_X_train = transform_features(fitted_X_train, transformer=processor, index=X_train.index)
    transformed_X_valid = transform_features(fitted_X_valid, transformer=processor, index=X_valid.index)
    transformed_X_test = transform_features(fitted_X_test, transformer=processor, index=X_test.index)
    print(transformed_X_train.head())
    print(f"X_train_transformed Shape: {transformed_X_train.shape}")
    print(transformed_X_valid.head())
    print(f"X_val_transformed Shape: {transformed_X_valid.shape}")
    print(transformed_X_test.head())
    print(f"X_test_transformed Shape: {transformed_X_test.shape}")

    return encoder, processor, transformed_X_train, transformed_X_valid, transformed_X_test, y_train, y_valid, y_test


if __name__ == "__main__":
    preprocess_data()
