from datetime import datetime

class Jadwal:
    def __init__(self, idJadwal, idDokter, timestamp, indikatorBooked):
        self._idJadwal = idJadwal
        self._idDokter = idDokter
        self._timestamp = timestamp #jadwal berupa timestamp
        self._indikatorBooked = indikatorBooked
    
    def setIdJadwal(self,idJadwal):
        self._idJadwal = idJadwal
    
    def setIdDokter(self,idDokter):
        self._idDokter = idDokter

    def setJadwal(self,timestamp):
        self._timestamp = timestamp

    def getIdJadwal(self):
        return self._idJadwal
    
    def getIdDokter(self):
        return self._idDokter

    def getJadwal(self):
        return self._timestamp
    
    def getJadwalAsDate(self):
        
        return str(datetime.fromtimestamp(self._timestamp))
    
    def getIndikatorBooked(self):
        return self._indikatorBooked