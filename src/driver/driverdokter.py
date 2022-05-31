from Jadwal import Jadwal
from Dokter import Dokter
from fileIO import *
from datetime import datetime
from ListOfDokter import ListOfDokter

# Driver main
#Dokter1 = Dokter(1,"S3","Sutrisno")     #Buat instance Dokter1
#Dokter.printDetailDokter(Dokter1)       #Print Detail Dokter1
print()
List1 = ListOfDokter()
print(len(List1))
#List = parseJadwal(1)
#print(List[0].getJadwal())
#Dokter.printListJadwal(Dokter1)


'''now = datetime.now()
Jadwal1 = Jadwal(1,1,datetime.timestamp(1618871400000),1)   #Buat timestamp Jadwal

Dokter.addJadwal(Dokter1,Jadwal1)       # add timestamp jadwal ke list of jadwal Dokter1
#Dokter.printListJadwal(Dokter1)         #print isi list jadwal DOkter 1


now = datetime.now()
Jadwal1 = Jadwal(12,1,datetime.timestamp(now),0)   #Buat timestamp Jadwal

Dokter.addJadwal(Dokter1,Jadwal1)       # add timestamp jadwal ke list of jadwal Dokter1
Dokter.printListJadwal(Dokter1)         #print isi list jadwal DOkter 1'''