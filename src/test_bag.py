import pytest
from classes.bag import BagObat
from classes.ListObat import ListObat

cart = BagObat()
db = ListObat(source="./database/obat.csv")

def test_cart_add():
    cart.add(1)
    assert cart.totalObat(1) == 1

def test_cart_increase():
    cart.increase(1, 2)
    assert cart.totalObat(1) == 3

def test_cart_decrease():
    cart.decrease(1,1)
    assert cart.totalObat(1) == 2

def test_cart_remove():
    cart.remove(1)
    assert cart.totalObat(1) == 0

def test_cart_container():
    cart.add(1)
    cart.add(3)
    cart.add(2)
    len = 0
    for data in cart:
        len+=1
    assert len == 3

def test_cart_sort():
    beforesort = []
    for data in cart:
        beforesort.append(data[0])
    assert beforesort == [1,3,2]

    aftersort = []
    cart.sortById(desc=True)
    for data in cart:
        aftersort.append(data[0])
    assert aftersort == [3,2,1]

def test_cart_print():
    global cart
    cart = BagObat()
    cart.add("AM001")
    cart.add("AM002")
    cart.add("AM003")
    cart.printBag(db)