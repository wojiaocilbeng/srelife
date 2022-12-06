#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Build:
    """
    建筑
    """
    __name = None
    __address = None
    __area = None

    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address

    def set_area(self, x: int, y: int):
        if x < 0 or y < 0:
            self.__area = 0
        else:
            self.__area = x * y

    def get_area(self) -> int:
        return self.__area


if __name__ == '__main__':
    pass
