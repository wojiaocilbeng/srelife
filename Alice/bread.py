#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from item import Item
from person import Person


class Bread(Item):
    """
    面包大小 购买人名字
    """
    __size = None
    __buy_name = None

    def __init__(self, name: str, kinds: str, size: str = None, buy_name: Person = None):
        super().__init__(kinds, name)
        self.__size = size
        self.__kinds = kinds
        self.__buy_name = buy_name
        self.__name = name

    def set_size(self, size: str):
        self.__size = size

    def get_size(self) -> str:
        return self.__size

    def set_buy_name(self, buy_name: Person):
        self.__buy_name = buy_name

    def get_buy_name(self) -> Person:
        return self.__buy_name

    def run(self):
        if self.__buy_name is not None:
            print("接着 {shopper} 去面包店购买了3个 {bread_name}".format(
                shopper=self.__buy_name.get_name(),
                bread_name=self.__name))


if __name__ == '__main__':
    pass
