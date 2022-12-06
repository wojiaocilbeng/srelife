#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from box import Box
from bread import Bread
from car import Car
from fruit import Fruit
from item import Item
from person import Person


def application():
    bob = Person(name="Bob", ethnic="British")
    alice = Person(name="alice", ethnic="American")
    alice_dad = Person(name="alice_dad", ethnic="French")
    salesmen = Person(name="salesmen", ethnic="Chinese")

    apple = Fruit(name="apple", kinds="fruit")
    orange = Fruit(name="orange", kinds="fruit")
    hot_dog = Bread(name="hot_dog", kinds="bread")

    apple.set_buy_name(name=alice)
    orange.set_buy_name(name=alice)
    hot_dog.set_buy_name(buy_name=alice)

    apple.set_use_name(name=bob)
    orange.set_use_name(name=bob)

    apple.set_patient(name=alice_dad)
    orange.set_patient(name=alice_dad)

    fruit_box = Box(name="fruit_box", kinds="basket")
    bread_box = Box(name="bread_box", kinds="basket")

    fruit_box.set_use_name(use_name=salesmen)
    bread_box.set_use_name(use_name=salesmen)

    wuling = Car(brand="wuling", seat=7)

    wuling.set_driver(n=bob)

    apple.run()
    orange.go()
    fruit_box.run()
    hot_dog.run()
    bread_box.go()
    wuling.run()
    orange.running()
    apple.going()


if __name__ == '__main__':
    application()
