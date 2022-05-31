import csv
import re
from .Jadwal import *
from datetime import datetime

source =""
target =""

def setSourceTarget(src,trgt):
    global source
    source = src

    global target
    target = trgt

def parseJadwal(idDokter):
    container = []
    with open ("./database/Jadwal"+str(idDokter)+".csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            jadwal_timestamp = datetime.strptime(row['jadwal'], '%Y-%m-%d %H:%M:%S')
            jadwal_timestamp = datetime.timestamp(jadwal_timestamp)
            jadwal = Jadwal(row['id_jadwal'], idDokter, jadwal_timestamp, row['ketersediaan'])
            container.append(jadwal)
    return container

def updateDBJadwal(idDokter,container):
    newval = toList(container)
    with open ("./database/Jadwal"+str(idDokter)+".csv","w", newline="") as f:
        writer = csv.writer(f)
        for row in newval:
            writer.writerow(row)

def toList(container):
    headers = ["id_jadwal","jadwal","ketersediaan"]
    result = []
    result.append(headers)
    for i in range(len(container)):
    #for jadwal in container:
        jadwal = container[i]
        dt = datetime.fromtimestamp(jadwal.getJadwal())
        dt_str = str(dt.date()) + " " + str(dt.time())
        val = [str(jadwal._idJadwal), dt_str, str(jadwal._indikatorBooked)]
        result.append(val)
    return result

'''
# test purposes
c = parseObat()
c[1].setStok(100)
toListDict(c)
updateObat(c)
'''
