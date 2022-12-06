#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from item import Item
from person import Person


class Box(Item):
    """
    篮子管理者
    """
    __use_name = None

    def __init__(self, name: str, kinds: str, use_name: Person = None):
        super().__init__(name, kinds)
        self.__use_name = use_name
        self.__name = name

    def set_use_name(self, use_name: Person):
        self.__use_name = use_name

    def get_use_name(self) -> Person:
        return self.__use_name

    def run(self):
        if self.__use_name is not None:
            print("于是 {salesmen} 用 {fruit_box} 来打包 ".format(
                salesmen=self.__use_name.get_name(),
                fruit_box=self.__name))

    def go(self):
        if self.__use_name is not None:
            print("{salesmen} 帮忙用 {bread_box} 打包 ".format(
                salesmen=self.__use_name.get_name(),
                bread_box=self.__name))


if __name__ == '__main__':
    pass
