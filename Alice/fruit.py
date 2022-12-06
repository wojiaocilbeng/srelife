#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from item import Item
from person import Person


class Fruit(Item):
    """
    购买人名 拿走名字 病人名字
    """
    __buy_name = None
    __take_name = None
    __patient = None

    def __init__(self, name: str, kinds: str = None, size: str = None, price: int = None, buy_name: Person = None,
                 take_name: Person = None, patient: Person = None) -> None:
        super().__init__(kinds, name, price)
        self.__size = size
        self.__kinds = kinds
        self.__name = name
        self.__price = price
        self.__buy_name = buy_name
        self.__take_name = take_name
        self.__patient = patient

    def set_buy_name(self, name: Person):
        self.__buy_name = name

    def get_buy_name(self) -> Person:
        return self.__buy_name

    def set_use_name(self, name: Person):
        self.__use_name = name

    def get_use_name(self) -> Person:
        return self.__use_name

    def set_patient(self, name: Person):
        self.__patient = name

    def get_patient(self) -> Person:
        return self.__patient

    def run(self):
        if self.__buy_name is not None:
            print("{shopper} 收到消息后，在水果店购买了9个 {fruit_name} ，".format(
                shopper=self.__buy_name.get_name(),
                fruit_name=self.__name))

    def go(self):
        if self.__buy_name is not None:
            print("接着还在水果店购买了6个 {fruit_name} ".format(
                shopper=self.__buy_name.get_name(),
                fruit_name=self.__name))

    def running(self):
        if self.__use_name is not None:
            print("{user} 不仅拿走了所有的 {fruit_name} ，".format(
                user=self.__use_name.get_name(),
                fruit_name=self.__name))

    def going(self):
        if self.__use_name or self.__buy_name or self.__patient is not None:
            print("还顺便还拿走了所有的 {fruit_name} , {shopper} 给 {patient} 拿了一个 {fruit}".format(
                user=self.__use_name.get_name(),
                fruit_name=self.__name,
                shopper=self.__buy_name.get_name(),
                patient=self.__patient.get_name(),
                fruit=self.__name))


if __name__ == '__main__':
    pass
