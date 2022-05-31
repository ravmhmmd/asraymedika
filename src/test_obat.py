import pytest
from classes.obat import Obat

test = Obat("AM001","TEST","20","75000","10 Kapsul/Strip","https://d2qjkwm11akmwu.cloudfront.net/products/28fa98fa-4d2e-4015-8047-12d88b1c95f6_product_image_url.webp")

@pytest.mark.parametrize("id_obat,nama_obat,stok,harga,desc,url_image",[("AM001","TEST","20","75000","10 Kapsul/Strip","https://d2qjkwm11akmwu.cloudfront.net/products/28fa98fa-4d2e-4015-8047-12d88b1c95f6_product_image_url.webp")])
def test_construct(id_obat,nama_obat,stok,harga,desc,url_image):
    o = Obat(id_obat,nama_obat,stok,harga,desc,url_image)
    assert (o._nama_obat) == 'TEST'
    assert (o._id_obat) == 'AM001'
    assert (o._stok) == 20
    assert (o._harga) == 75000

def test_increasestock():
    test.addStok(3)
    assert test._stok == 23

def test_decreasestok():
    test.decreaseStok(3)
    assert test._stok == 20

def test_setstok():
    test.setStok(10)
    assert test._stok == 10

def test_setharga():
    test.setHargaObat(10000)
    assert test._harga != 75000
    assert test._harga == 10000


def test_printInfo():
    test.printInfo()
    assert test.printInfo() == print(test._nama_obat)
