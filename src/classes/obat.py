class Obat:
    def __init__(self, idobat, nama, stokobat, hargaobat, description, url):
        self._id_obat = idobat
        self._nama_obat = nama
        self._stok = int(stokobat)
        self._harga = int(hargaobat)
        self._desc = description
        self._img = url
    
    def getIdObat(self):
        return self._id_obat
    
    def getNamaObat(self):
        return self._nama_obat

    def getStok(self):
        return self._stok
    
    def getHargaObat(self):
        return self._harga
    
    def getDescObat(self):
        return self._desc
        
    def getImgObat(self):
        return self._img
    
    def setIdObat(self, newid):
        self._id_obat = newid
    
    def setNamaObat(self, newname):
        self._nama_obat = newname

    def setStok(self, newstok):
        self._stok = newstok
    
    def setHargaObat(self, newprice):
        self._harga = newprice
    
    def setImgObat(self, newurl):
        self._img = newurl

    def decreaseStok(self, amount):
        self._stok -= amount
    
    def addStok(self, amount):
        self._stok += amount
    
    def printInfo(self):
        print(self._nama_obat)

    
    

    

