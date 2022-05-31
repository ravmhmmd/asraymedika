import csv
import re
from .Jadwal import Jadwal
from datetime import datetime
from .fileIO import *

class Dokter:
    def __init__(self, idDokter, gelar, name):
        self._id = idDokter
        self._gelar = gelar
        self._name = name
        self.listJadwal = parseJadwal(idDokter)     #List berisi object jadwal

    def getIdDokter(self):
        return self._id
    
    def getNamaDokter(self):
        return self._name
    
    def printDetailDokter(self):
        print("ID Dokter: ", self._id)
        print("Nama Dokter:", self._name)
        print("Gelar/Pendidikan: ",self._gelar)

    def addJadwal(self,Jadwal):
        self.listJadwal.append(Jadwal)
    
    def popJadwal(self, indekslistJadwal):
        if (len(self.listJadwal)==0):
            print("Delete jadwal gagal, list jadwal kosong")
        else:
            return self.listJadwal.pop(indekslistJadwal)
    
    def printListJadwal(self):
        print("Jadwal Praktik Dokter",self._name)
        for i in range (len(self.listJadwal)):
            print("id Jadwal: ",end=" ")
            print(self.listJadwal[i].getIdJadwal())
            print("id Dokter:", end=" ")
            print(self.listJadwal[i].getIdDokter())
            print("Jadwal:", end=" ")
            print(datetime.fromtimestamp(self.listJadwal[i].getJadwal()))
            print("Tersedia:", end=" ")
            print(int(self.listJadwal[i].getIndikatorBooked())==1)
            print()
    




