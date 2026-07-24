#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/24 20:48
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   abcs.py
# @Desc     :   

from abc import ABC, abstractmethod
from pathlib import Path
from torch import nn, save, load, Tensor
from typing import final


class Net(ABC, nn.Module):
    """ Abstract Base Class for Neural Networks """

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def _init_weights(self) -> None:
        """
        Initialise the weights of the network
        :return: None
        """
        pass

    @abstractmethod
    def forward(self, x) -> Tensor:
        """
        Forward pass of the network
        :param x: input tensor
        :return: output of the network
        """
        pass

    @abstractmethod
    def summary(self) -> None:
        """
        Print a summary of the network
        :return: None
        """
        pass

    @final
    def save_model(self, path: str | Path) -> None:
        """
        Save the model
        :param path: path to save the model
        """
        save(self.state_dict(), str(path))
        print("The model has been saved successfully.")

    @final
    def load_model(self, path: str | Path, strict: bool = True) -> None:
        """
        Load the model - all networks share the same method
        :param path: path to load the model from
        :param strict: whether to strictly enforce that the keys in state_dict match the keys returned by this module's state_dict function
        """
        self.load_state_dict(load(str(path)), strict=strict)
        print("The model has been loaded successfully.")
