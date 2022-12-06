#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Item:
    """
    种类 名字 价格
    """
    __kinds = None
    __name = None
    __price = 0
    __use_name = None

    def __init__(self, name: str, kinds: str = None, price: int = None, use_name: str = None) -> None:
        self.__type = kinds
        self.__name = name
        self.__price = price
        self.__use_name = use_name

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name


if __name__ == '__main__':
    pass
