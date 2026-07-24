#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/24 20:05
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   dataloaders.py
# @Desc     :   

from torch import Tensor, stack
from torch.utils.data import DataLoader, Dataset
from torch.nn.utils.rnn import pad_sequence
from typing import Literal


class TorchDataLoader(DataLoader):
    """ A custom PyTorch DataLoader class for handling TorchDataset """

    def __init__(
            self,
            dataset: Dataset,
            *,
            batch_size: int = 32, shuffle_state: bool = True,
            workers: int = 0,
            nlp_batch_pad: bool = False,
            features_pad_value: int = 0, labels_pad_value: int = 0,
            batch_first: bool = True, padding_direction: str | Literal["right", "left"] = "right"
    ) -> None:
        """
        Initialise the TorchDataLoader class
        :param dataset: the TorchDataset or Dataset to load data from
        :param batch_size: the number of samples per batch
        :param shuffle_state: whether to shuffle the data at every epoch
        :param workers: the number of workers to use for data loading
        :param nlp_batch_pad: whether to pad sequences in the batch
        :param features_pad_value: the padding value for sequences
        :param labels_pad_value: the padding value for labels, -100 by default for PyTorch loss functions ignore_index
        :param batch_first: whether to have batch dimension first
        :param padding_direction: side to apply padding ("right" or "left")
        """
        self._batches: int = batch_size
        self._shuffle: bool = shuffle_state
        self._nlp_pad: bool = nlp_batch_pad
        self._workers: int = workers
        self._FEATURE_PAD: int = features_pad_value
        self._LABEL_PAD: int = labels_pad_value
        self._first: bool = batch_first
        self._direction: str = padding_direction

        super().__init__(
            dataset=dataset,
            batch_size=self._batches,
            shuffle=self._shuffle,
            num_workers=self._workers,
            pin_memory=self._workers > 0,
            collate_fn=self._collate_fn if self._nlp_pad else None
        )

    def _collate_fn(self, batch: list[tuple[Tensor, Tensor]]) -> tuple[Tensor, Tensor]:
        """
        Collate function to process a batch of data
        :param batch: list of tuples (feature, label)
        :return: padded features and labels
        """
        # batch: list[tuple[Tensor, Tensor]]
        unpadded_features: list[Tensor] = [f for f, _ in batch]
        unpadded_labels: list[Tensor] = [l for _, l in batch]

        # Pad features
        features: Tensor = pad_sequence(
            unpadded_features,
            batch_first=self._first, padding_value=self._FEATURE_PAD, padding_side=self._direction
        )

        # Check labels
        label_state: int = unpadded_labels[0].dim()
        if label_state > 0:
            # Pad labels
            labels: Tensor = pad_sequence(
                unpadded_labels,
                batch_first=self._first, padding_value=self._LABEL_PAD, padding_side=self._direction
            )
        else:
            # Labels are scalars; stack them directly
            labels: Tensor = stack(unpadded_labels, dim=0)

        return features, labels

    def __repr__(self):
        """
        Return a string representation of the TorchDataLoader
        :return: string representation of the TorchDataLoader
        """
        return (f"TorchDataLoader(dataset={self.dataset}, "
                f"batch_size={self._batches}, "
                f"shuffle={self._shuffle}, "
                f"workers={self._workers}, "
                f"nlp_batch_pad={self._nlp_pad}, "
                f"features_pad_value={self._FEATURE_PAD}, "
                f"labels_pad_value={self._LABEL_PAD}, "
                f"batch_first={self._first}, "
                f"padding_side='{self._direction}')")


if __name__ == "__main__":
    pass
