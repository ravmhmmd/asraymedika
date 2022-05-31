from .Dokter import Dokter
from .fileIO import *
class ListOfDokter:
    listDokter = []

    def __init__(self):
        Dokter1 = Dokter(1,"S2","Sutrisno")
        self.listDokter.append(Dokter1)
        Dokter2 = Dokter(2,"S2","Terawan")
        self.listDokter.append(Dokter2)
        Dokter3 = Dokter(3,"S2","Karyadi")
        self.listDokter.append(Dokter3)
    
    def printListDokter(self):
        for i in range (len(self.listDokter)):
            self.listDokter[i].printDetailDokter()
    
    def printDokterbyID(self,id):
        for i in range (len(self.listDokter)):
            if (id==self.listDokter[i].getIdDokter()):
                self.listDokter[i].printDetailDokter()
                
    def printJadwalbyID(self,id):
        for i in range (len(self.listDokter)):
            if (id==self.listDokter[i].getIdDokter()):
                self.listDokter[i].printListJadwal()

    def SearchDokter(self,name):
        found = False
        idxTarget = -1
        for i in range (len(self.listDokter)):
            if (name==self.listDokter[i].getNamaDokter()):
                found = True
                idxTarget = i
        
        if (found):
            self.listDokter[idxTarget].printDetailDokter()
        else:
            print("Dokter tidak tersedia")

    def Checkout(self, idDokter, idJadwal):
        self.listDokter[idDokter].listJadwal[idJadwal]._indikatorBooked = str(0)
        updateDBJadwal(idDokter, self.listDokter[idDokter].listJadwal)

