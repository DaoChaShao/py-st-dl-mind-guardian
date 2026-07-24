#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/24 21:24
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   mlp.py
# @Desc     :   

from torch import nn

from .abcs import Net

WIDTH: int = 64


class MLP(Net):
    """ Multi-Layer Perceptron (MLP) """

    def __init__(
            self,
            input_dims: int, hidden_dims: int, output_dims: int,
            *,
            num_classes: int,
            dropout_rate: float = 0.2
    ) -> None:
        """
        Initialise the MLP.
        :param input_dims:
        :param hidden_dims:
        :param output_dims:
        :param num_classes:
        :param dropout_rate:
        """
        self._input: int = input_dims
        self._hidden: int = hidden_dims
        self._output: int = output_dims
        self._classes: int = num_classes
        self._drop: float = dropout_rate

        super().__init__()
        self._net = nn.Sequential(
            nn.Linear(self._input, self._hidden),
            nn.BatchNorm1d(self._hidden),
            nn.ReLU(),
            nn.Dropout(self._drop),

            nn.Linear(self._hidden, self._output),
            nn.BatchNorm1d(self._output),
            nn.ReLU(),
            nn.Dropout(self._drop),

            nn.Linear(self._output, self._classes),
        )

        self._init_weights()

    def _init_weights(self) -> None:
        """
        Initialise the weights of the network
        :return: None
        """
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)
                nn.init.zeros_(m.bias)

    def forward(self, x):
        """
        Forward pass of the network
        :param x: input tensor
        :return: output of the network
        """
        return self._net(x)

    def summary(self) -> None:
        """
        Print a summary of the model parameters
        :return: None
        """
        print("*" * WIDTH)
        print(f"Model Summary for {self.__class__.__name__}")
        print("-" * WIDTH)
        print(f"Input Dimensions:       {self._input}")
        print(f"Hidden Dimensions:      {self._hidden}")
        print(f"Output Dimensions:      {self._output}")
        print(f"Number of Classes:      {self._classes}")
        print(f"Dropout Rate:           {self._drop}")
        print("-" * WIDTH)
        # Calculate parameters
        total_params, trainable_params = self._count_parameters()
        print(f"Total parameters:         {total_params:,}")
        print(f"Trainable parameters:     {trainable_params:,}")
        print(f"Non-trainable parameters: {total_params - trainable_params:,}")
        print("*" * WIDTH)
