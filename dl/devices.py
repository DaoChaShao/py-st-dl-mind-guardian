#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/24 14:33
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   devices.py
# @Desc     :   

from typing import Literal

from torch import cuda, backends


def get_device(
        accelerator: str | Literal["auto", "cpu", "cuda", "mps"] = "auto",
        *,
        cuda_mode: int = 0, display: bool = True
) -> str:
    """Get the appropriate device based on the target device string.
    :param accelerator: the target device string ("auto", "cuda", "mps", "cpu")
    :param cuda_mode: the CUDA device index to use (if applicable)
    :param display: whether to display the device information
    :return: the appropriate device string
    """
    match accelerator:
        case "auto":
            # CUDA (NVIDIA GPU)
            if cuda.is_available():
                count = cuda.device_count()
                if cuda_mode >= count:
                    if display: print(f"CUDA device index {cuda_mode} is out of range. Using 'cuda:0' instead.")
                    cuda_mode = 0
                if display:
                    print(f"Detected {count} CUDA GPU(s):")
                    for i in range(count):
                        print(f"GPU {i}: {cuda.get_device_name(i)}")
                        print(f"- Allocated: {cuda.memory_allocated(i) / 1024 ** 3:.1f} GB")
                        print(f"- Reserved:  {cuda.memory_reserved(i) / 1024 ** 3:.1f} GB")
                    print(f"Using cuda:{cuda_mode}")
                return f"cuda:{cuda_mode}"

            # MPS (Apple Silicon GPU)
            if backends.mps.is_available():
                if display: print("Apple MPS device detected.")
                return "mps"

            # Fallback: CPU
            if display: print("GPU and MPS unavailable. Using CPU.")
            return "cpu"

        case "cuda":
            if cuda.is_available():
                count: int = cuda.device_count()
                if cuda_mode >= count:
                    if display: print(f"CUDA device index {cuda_mode} is out of range. Using 'cuda:0' instead.")
                    cuda_mode = 0
                if display:
                    print(f"Detected {count} CUDA GPU(s):")
                    for i in range(count):
                        print(f"GPU {i}: {cuda.get_device_name(i)}")
                        print(f"- Allocated: {cuda.memory_allocated(i) / 1024 ** 3:.1f} GB")
                        print(f"- Reserved:  {cuda.memory_reserved(i) / 1024 ** 3:.1f} GB")
                    print(f"Using cuda:{cuda_mode}")
                return f"cuda:{cuda_mode}"

            if display: print("GPU and MPS unavailable. Using CPU.")
            return "cpu"

        case "mps":
            if backends.mps.is_available():
                if display: print("Apple MPS device detected.")
                return "mps"

            if display: print("GPU and MPS unavailable. Using CPU.")
            return "cpu"

        case "cpu":
            if display: print("Using CPU as target device.")
            return "cpu"

        case _:
            raise ValueError(f"Unsupported accelerator: {accelerator}")
