#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from hospital import Hospital
from person import Person


class Car:
    """
    汽车品牌 驾驶员 乘客
    """
    __brand = None
    __seat = 0
    __driver = None
    __passengers = []

    def __init__(self, brand: str, seat: int, driver: Person = None, ) -> None:
        self.__brand = brand
        self.__driver = driver
        self.__seat = seat

    def set_brand(self, brand: str):
        self.__brand = brand

    def get_brand(self) -> str:
        return self.__brand

    def set_seat(self, seat: int):
        self.__seat = seat

    def get_seat(self) -> int:
        return self.__seat

    def set_driver(self, n: Person):
        self.__driver = n

    def get_driver(self) -> Person:
        return self.__driver

    def remove_passengers(self, p: Person):
        self.__passengers.remove(p)

    def add_passengers(self, p: Person):
        self.__passengers.append(p)

    Hospital = Hospital

    def run(self):
        if self.__driver is not None:
            print("{driver_name} 正在驾驶 {brand} 车去 {addr} 看望".format(
                driver_name=self.__driver.get_name(),
                brand=self.__brand,
                addr=Hospital))


if __name__ == '__main__':
    pass
