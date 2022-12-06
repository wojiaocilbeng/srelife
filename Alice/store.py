#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from build import Build
from item import Item


class Store(Build):
    """
    品牌 店铺种类 物品数量
    """
    __brand = None
    __kind = None
    __num = []

    def __init__(self, brand: str, kind: str, name: str, address: str) -> None:
        super().__init__(name, address)
        self.__brand = brand
        self.__kind = kind

    def remove_num(self, n: Item):
        self.__num.remove(n)

    def add_num(self, n: Item):
        self.__num.append(n)


if __name__ == '__main__':
    pass
