#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/24 18:55
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   datasets.py
# @Desc     :   

from numpy import ndarray
from pandas import DataFrame, Series
from torch import (Tensor, tensor,
                   float32, long)
from torch.utils.data import Dataset


class TorchDataset(Dataset):
    """ A custom PyTorch Dataset class for handling label features and labels """

    def __init__(
            self,
            features: DataFrame | ndarray | Tensor | list,
            labels: DataFrame | Series | ndarray | Tensor | list,
            *,
            is_var_len: bool = False,
    ) -> None:
        """
        Initialise a general TorchDataset class
        :param features: raw features (list/ndarray/DataFrame) or padded Tensor
        :param labels: raw labels (list/ndarray/DataFrame) or padded Tensor
        :param is_var_len: if True → keep raw lists, collate_fn will pad them
        """
        self._var_len: bool = is_var_len

        if self._var_len:
            self._features = self._to_list_var_len_tensor(features, is_label=False)
            self._labels = self._to_list_var_len_tensor(labels, is_label=True)
        else:
            self._features: Tensor = self._to_equal_len_tensor(features, is_label=False)
            self._labels: Tensor = self._to_equal_len_tensor(labels, is_label=True)

    @staticmethod
    def _to_equal_len_tensor(
            data: DataFrame | Series | Tensor | ndarray | list,
            *,
            is_label: bool = False
    ) -> Tensor:
        """ Convert input data to a PyTorch tensor on the specified device
        :param data: the input data (DataFrame, ndarray, list, or Tensor)
        :param is_label: if True → convert to long dtype
        :return: the converted PyTorch tensor
        """
        if isinstance(data, (DataFrame, Series)):
            out = tensor(data.to_numpy(), dtype=long if is_label else float32)
        elif isinstance(data, Tensor):
            out = data.to(dtype=long if is_label else float32)
        elif isinstance(data, (ndarray, list)):
            out = tensor(data, dtype=long if is_label else float32)
        else:
            raise TypeError(f"Unsupported data type: {type(data)}")

        return out

    @staticmethod
    def _to_list_var_len_tensor(
            data: DataFrame | Series | Tensor | ndarray | list,
            *,
            is_label: bool = False
    ) -> list[Tensor]:
        """
        Convert input data to a list of PyTorch tensors for variable-length data
        :param data: the input data (DataFrame, Series, ndarray, or list)
        :param is_label: if True → convert to long dtype
        :return: the converted list of PyTorch tensors
        """
        if isinstance(data, list):
            out: list[Tensor] = [tensor(item, dtype=long if is_label else float32) for item in data]
        elif isinstance(data, (DataFrame, Series, ndarray)):
            if isinstance(data, DataFrame):
                data = data.to_numpy()
            out: list[Tensor] = [tensor(row, dtype=long if is_label else float32) for row in data]
        elif isinstance(data, Tensor):
            out: list[Tensor] = [data[i].long() if is_label else data[i].float() for i in range(len(data))]
        else:
            raise TypeError(f"Unsupported data type: {type(data)}")

        return out

    @property
    def features(self) -> Tensor | list[Tensor]:
        """
        Return the feature tensor as a property
        :return: features
        """
        return self._features

    @property
    def labels(self) -> Tensor | list[Tensor]:
        """
        Return the label tensor as a property
        :return: labels
        """
        return self._labels

    def __len__(self) -> int:
        """
        Return the total number of samples in the dataset
        :return: total number of samples
        """
        return len(self._features)

    def __getitem__(self, index: int | slice) -> tuple[Tensor | list[Tensor], Tensor | list[Tensor]]:
        """
        Return a single (feature, label) pair or a batch via slice
        :param index: the index of the sample to retrieve
        :return: a single (feature, label) pair or a batch
        """
        return self._features[index], self._labels[index]

    def __repr__(self) -> str:
        """
        Return a string representation of the dataset
        :return: string representation of the dataset
        """
        if self._var_len:
            info4features = f"len={len(self._features)} (unpadded tensor list)"
            info4labels = f"len={len(self._labels)} (unpadded tensor list)"
        else:
            info4features = f"shape={tuple(self._features.shape)}"
            info4labels = f"shape={tuple(self._labels.shape)}"

        return f"TorchDataset(features={info4features}, labels={info4labels})"


if __name__ == "__main__":
    pass
