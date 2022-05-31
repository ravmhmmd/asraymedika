import pytest
from classes.bag import BagObat
from classes.obat import Obat
from classes.ListObat import ListObat

cart = BagObat()
db = ListObat()
ob1 = Obat(1,'AMOXICILLIN',20,75000,'desc1','url1.img')
ob2 = Obat(2,'PARACETAMOL',20,9000,'desc2','url2.img')
ob3 = Obat(3,'ALKOHOL',20,200000,'desc3','url3.img')
db.addObat(ob1)
db.addObat(ob2)
db.addObat(ob3)

receipt = ''' amoxicillin : 3\nparacetamol : 4 '''
def addFromReceipt(cart, db, source):
    args = source.split('\n')
    for arg in args:
        subargs = arg.strip().split(" : ")
        namaobat = subargs[0]
        qty = int(subargs[1])
            
        search_res = db.searchObat(namaobat)
        if not search_res:
            print(str(namaobat)+" tidak ditemukan.")
            continue
        else:
            obj_obat = search_res[0]
            cart.add(obj_obat.getIdObat())
            if qty > 1:
                cart.increase(obj_obat.getIdObat(),qty-1)

def test_inputreceipt():
    addFromReceipt(cart,db,receipt)
    assert cart.totalObat(1) == 3
    assert cart.totalObat(2) == 4

def test_totalinbag():
    assert cart.total() == 2

def test_idobatinbag():
    assert cart._container[0] == (1,3)
    assert cart._container[1] == (2,4)

newcart1 = BagObat()
receipterror1 = ''' obatinitidakada : 3\nparacetamol : 4 '''
def test_obatnotindb():
    addFromReceipt(newcart1,db,receipterror1)
    assert newcart1.total() == 1

def test_idobatinbagfromerr1():
    assert newcart1._container[0] == (2,4)

newcart2 = BagObat()
receipterror2 = ''' obatinitidakada : 3\neeeee : 4 '''
def test_allobatnotindb():
    addFromReceipt(newcart2,db,receipterror2)
    assert newcart2.total() == 0
