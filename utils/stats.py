#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 22:57
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   stats.py
# @Desc     :   

from numpy import (random as np_random,
                   unique, ndarray)
from pandas import DataFrame, Series, read_csv, Index
from pathlib import Path
from random import seed as rnd_seed, getstate, setstate
from time import perf_counter

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.utils.class_weight import compute_class_weight

from utils.decorator import timer

WIDTH: int = 64


class RandomSeedForNumpy:
    """ Setting numpy random seed for reproducibility """

    def __init__(self, description: str, seed: int = 27, tick_tock: bool = False):
        """
        Initialise the RandomSeed class
        :param description: the description of a random seed
        :param seed: the seed value to be set
        :param tick_tock: whether to measure elapsed time
        """
        self._description: str = description
        self._seed: int = seed
        self._previous_py_seed = None
        self._previous_np_seed = None

        self._tick: bool = tick_tock
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        """ Set the random seed """
        if self._tick:
            self._start = perf_counter()

        # Save the previous random seed state
        self._previous_py_seed = getstate()
        self._previous_np_seed = np_random.get_state()

        # Set the new random seed
        rnd_seed(self._seed)
        np_random.seed(self._seed)

        print("*" * WIDTH)
        print(f"{self._description} has been set to {self._seed}.")
        print("-" * WIDTH)

        return self

    def __exit__(self, *args):
        """ Exit the random seed context manager """
        # Restore the previous random seed state
        if self._previous_py_seed is not None:
            setstate(self._previous_py_seed)
        if self._previous_np_seed is not None:
            np_random.set_state(self._previous_np_seed)

        # Calculate elapsed time if measuring
        if self._tick:
            self._end = perf_counter()
            self._elapsed = self._end - self._start

        print("-" * WIDTH)
        print(f"{self._description} has been restored to previous randomness.")
        if self._tick:
            elapsed_time: str = self._format_time(self._elapsed)
            print(f"{self._description} took {elapsed_time}.")
        print("*" * WIDTH)
        print()

        # Return False to propagate exceptions, True to suppress them
        return False

    @staticmethod
    def _format_time(seconds: float) -> str:
        """
        Format time breakdown from seconds to days, hours, minutes, and seconds
        :param seconds: time in seconds
        :return: formatted time breakdown string
        """
        if seconds < 1.0:
            return f"{seconds * 1000:.1f} ms"

        days: int = int(seconds // 86400)
        hours: int = int((seconds % 86400) // 3600)
        minutes: int = int((seconds % 3600) // 60)
        secs: float = seconds % 60

        parts: list[str] = []
        if days > 0:
            parts.append(f"{days} days")
        if hours > 0:
            parts.append(f"{hours} hours")
        if minutes > 0:
            parts.append(f"{minutes} minutes")
        if secs > 0 or not parts:
            parts.append(f"{secs:.2f} seconds")

        return " ".join(parts)

    def __repr__(self):
        """ Return a string representation of the random seed """
        base: str = f"NumpyRandomSeed(description={self._description}, seed={self._seed})"
        if self._tick and self._elapsed > 0:
            base += f", Elapsed Time: {self._elapsed:.2f} s"

        return base


@timer
def load_csv(csv_path: str | Path, *, dis_content: bool = True, dis_summary: bool = True) -> DataFrame:
    """
    Read data from a dataset file
    :param csv_path: Target path to the file.
    :param dis_content: Toggle for printing the first few rows.
    :param dis_summary: Toggle for basic statistics and quality checks.
    :return: Loaded Pandas DataFrame.
    """
    dataset: DataFrame = read_csv(str(csv_path))

    if dis_content:
        print(dataset.head())

    if dis_summary:
        print(dataset.describe())

        dup_rows: int = dataset.duplicated().sum()
        miss_values: int = dataset.isnull().sum().sum()
        miss_details: Series = dataset.isnull().sum()[dataset.isnull().sum() > 0]
        print(f"Duplicated Rows: {dup_rows}")
        print(f"Missing Values: {miss_values}")
        print(f"Missing Values Details: \n{miss_details}")

    return dataset


@timer
def check_labels_distribution(labels: Series, *, dis_counts: bool = True, dis_prop: bool = True) -> tuple:
    """
    Check the distribution of the labels in the target variable.
    :param labels: the target variable
    :param dis_counts: Toggle for printing the label counts
    :param dis_prop: Toggle for printing the label proportions
    :return: the label counts and proportions
    """
    if dis_counts:
        print(labels.value_counts())
        print()
    if dis_prop:
        print(labels.value_counts(normalize=True))

    return labels.value_counts(), labels.value_counts(normalize=True)


@timer
def encode_labels(labels: Series, *, dis_encoded: bool = True) -> tuple[Series, LabelEncoder]:
    """
    Encode the labels in the target variable.
    :param labels: the target variable
    :param dis_encoded: Toggle for printing the encoded labels
    :return: the encoded labels and the label encoder
    """
    # Initialise the label encoder
    encoder: LabelEncoder = LabelEncoder()
    # Fit and transform the label encoder
    out: Series = Series(
        encoder.fit_transform(labels),
        index=labels.index,
        name=labels.name
    )

    if dis_encoded:
        print(f"Label encoder classes: {encoder.classes_}")
        print(f"5 / {len(out)} encoded labels:\n{out.head()}")

    return out, encoder


@timer
def split_data(
        features: DataFrame, labels: Series,
        *,
        randomness: int = 27, shuffle_status: bool = True, dis_split: bool = True
) -> tuple:
    """
    Split the data into training, validation, and proving sets.
    :param features: the DataFrame of features
    :param labels: the Series of labels
    :param randomness: the random seed for reproducibility
    :param shuffle_status: whether to shuffle the data before splitting
    :param dis_split: Toggle for printing the split sets
    :return: the training, validation, and proving sets
    """
    assert len(features) == len(labels), "The number of features must be equal to the number of labels."

    X_train, X_temp, y_train, y_temp = train_test_split(
        features, labels,
        test_size=0.3,
        random_state=randomness,
        shuffle=shuffle_status,
        stratify=labels,
    )
    X_valid, X_test, y_valid, y_test = train_test_split(
        X_temp, y_temp,
        test_size=0.5,
        random_state=randomness,
        shuffle=shuffle_status,
        stratify=y_temp,
    )

    if dis_split:
        print(f"Training set: {X_train.shape}, {y_train.shape}")
        print(f"Validation set: {X_valid.shape}, {y_valid.shape}")
        print(f"Proving set: {X_test.shape}, {y_test.shape}")

    return X_train, X_valid, X_test, y_train, y_valid, y_test


@timer
def create_features_transformer(features: DataFrame, *, dis_transformer: bool = True) -> ColumnTransformer:
    """
    Create a ColumnTransformer to preprocess the categorical data and scale the numerical data.
    :param features: the DataFrame to be preprocessed
    :param dis_transformer: Toggle for printing the transformer details.
    :return: the created ColumnTransformer
    """
    # Divide the columns into numerical and categorical types
    # Select numerical columns
    numerical_cols = features.select_dtypes(include="number").columns.tolist()
    # Select categorical columns
    categorical_cols = features.select_dtypes(include=["object", "category"]).columns.tolist()

    # Set a list of transformers to collect the pipelines
    transformers: list[tuple[str, Pipeline, list[str]]] = []

    # Establish a pipe to process numerical features and handle missing values only if they exist
    if numerical_cols:
        numerical_pipe = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ])
        transformers.append(("num", numerical_pipe, numerical_cols))

    # Establish a pipe to process categorical features and handle missing values only if they exist
    if categorical_cols:
        categorical_pipe = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
        ])
        transformers.append(("cat", categorical_pipe, categorical_cols))

    if dis_transformer:
        print(f"Numerical columns: {numerical_cols}")
        print(f"Categorical columns: {categorical_cols}")

    # Process numerical and categorical features
    return ColumnTransformer(transformers=transformers, remainder="drop")


def fit_features_transformer(features: DataFrame, *, transformer: ColumnTransformer) -> ColumnTransformer:
    """
    Fit the transformer on training data.
    :param features: the DataFrame to be transformed
    :param transformer: the ColumnTransformer to be fitted
    :return: the fitted ColumnTransformer
    """
    return transformer.fit(features)


def transform_features(features: ndarray, *, transformer: ColumnTransformer, index: Index | None = None) -> DataFrame:
    """
    Transform the features using the fitted transformer.
    :param features: the DataFrame to be transformed
    :param transformer: the ColumnTransformer to be used
    :param index: the index of the transformed DataFrame
    :return: the transformed DataFrame
    """
    return DataFrame(
        features,
        columns=transformer.get_feature_names_out(),
        index=index
    )


@timer
def compute_labels_weights(y_train: Series, *, dis_weights: bool = True) -> ndarray:
    """
    Compute class weights for imbalanced datasets.
    :param y_train: the target variable
    :param dis_weights: Toggle for printing the class weights
    :return:
    """
    weights: ndarray = compute_class_weight(
        class_weight="balanced",
        classes=unique(y_train),
        y=y_train,
    )

    if dis_weights:
        print(weights)

    return weights


if __name__ == "__main__":
    pass
