#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Person:
    """
    人名 民族 性别
    """
    __name = None
    __ethnic = None
    __sex = None

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_ethnic(self, ethnic: str):
        self.__ethnic = ethnic

    def get_ethnic(self) -> str:
        return self.__ethnic

    def __init__(self, name: str, ethnic: str, sex: str = None) -> None:
        self.__name = name
        self.__ethnic = ethnic
        self.__sex = sex

    def set_sex(self, s: int, w: str, m: str):
        if s == 0:
            self.__sex = w
        else:
            self.__sex = m

    def get_sex(self) -> str:
        return self.__sex


if __name__ == '__main__':
    pass
