#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/17 22:52
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   apis.py
# @Desc     :   

from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam
from typing import Literal


def verify_api_key(api_key: str, category: str | Literal["openai", "deepseek"] = "openai") -> bool:
    """
    Check the API key format
    - The length of an OpenAI API key is 164-digit key
    - The length of a DeepSeek API key is 35-digit key
    :param api_key: enter the API key of the deepseek
    :param category: the category of the API key
    :return: True if the API key is valid
    """
    if api_key.startswith("sk-"):
        if category.lower() == "openai" and len(api_key) == 164:
            return True
        elif category.lower() == "deepseek" and len(api_key) == 35:
            return True

    return False


class OpenAIEmbedder(object):

    def __init__(self, api_key: str) -> None:
        """
        Initialize the OpenAI Embeddings API
        :param api_key: str: The API key for the OpenAI API
        :return: None
        """
        self._api_key = api_key

    def client(self, prompt: list, model: str, dimensions: int | Literal[256, 512, 1024] = 1024) -> list:
        """
        Initialize the OpenAI Embeddings API
        - dimensions: 256、512、1024、1536、2048
        :param dimensions: int: The number of dimensions for the embedding
        :param model: str: The model to use for the embedding
        :param prompt: list: The input text to be embedded
        :return: list: The embeddings for the input text
        """
        client = OpenAI(api_key=self._api_key, base_url="https://api.openai.com/v1")

        response = client.embeddings.create(
            input=prompt,
            model=model,
            dimensions=dimensions,
            encoding_format="float",
            timeout=3,
        )

        return [item.embedding for item in response.data]


class OpenAITextCompleter(object):
    """ OpenAI Completer API Wrapper """

    def __init__(self, api_key: str, temperature: float = 1.0, top_p: float = 1.0) -> None:
        """
        Initialise the OpenAI Hyperparameter Tuning API
        :param api_key: str: The API key for the OpenAI API
        :param temperature: float: The temperature for the completion
        :param top_p: float: The top-p for the completion
        :return: None
        """
        self._api_key = api_key
        self._temperature = temperature
        self._top_p = top_p

    def client(
            self,
            *,
            role: str,
            prompt: str,
            model: str | Literal["gpt-4.1-mini", "gpt-5.4-mini"] = "gpt-4.1-mini"
    ) -> str:
        """
        Initialise the OpenAI Completion API
        :param role: str: The input text to be completed
        :param prompt: str: The prompt to complete the input text
        :param model: str: The model to use for the completion
        :return: str: The completed text
        """
        client = OpenAI(api_key=self._api_key, base_url="https://api.openai.com/v1")

        messages = [
            ChatCompletionSystemMessageParam(
                role="system",
                content=role
            ),
            ChatCompletionUserMessageParam(
                role="user",
                content=prompt
            )
        ]
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=False,
            temperature=self._temperature,
            top_p=self._top_p,
        )

        return completion.choices[0].message.content


class DeepSeekCompleter(object):
    """ DeepSeek Completer API Wrapper """

    def __init__(self, api_key: str, *, temperature: float = 0.7) -> None:
        """
        Initialise the DeepSeek Completer API
        :param api_key: str: The API key for the DeepSeek API
        :param temperature: float: The temperature for the completion
        :return: None
        """
        self._api_key = api_key
        self._temperature = temperature

    def client(
            self,
            *,
            role: str,
            prompt: str,
            model: str | Literal["deepseek-v4-flash",] = "deepseek-v4-flash"
    ) -> str:
        """
        Initialise the DeepSeek Completion API
        :param role: str: The input text to be completed
        :param prompt: str: The prompt to complete the input text
        :param model: str: The model to use for the completion, default is "deepseek-chat"
        :return: str: The completed text
        """
        client = OpenAI(api_key=self._api_key, base_url="https://api.deepseek.com")

        messages = [
            ChatCompletionSystemMessageParam(
                role="system",
                content=role
            ),
            ChatCompletionUserMessageParam(
                role="user",
                content=prompt
            )
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=self._temperature,
            stream=False
        )

        return response.choices[0].message.content


if __name__ == "__main__":
    pass
