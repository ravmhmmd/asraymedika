import csv
import re
from .obat import Obat

class ListObat:
  def __init__(self, source = None):
    self._container = []
    self._iterator = -1
    if source is not None:
      self.load(source)
  
  def __setitem__(self, idx, obat):
    self._container[idx] = obat
  
  def __getitem__(self, idx):
    return self._container[idx]
  
  # iterator
  # ref: https://towardsdatascience.com/how-to-loop-through-your-own-objects-in-python-1609c81e11ff

  def __iter__(self):
    return self
  
  def __next__(self):
    self._iterator += 1
    if self._iterator >= len(self._container):
      self._iterator = -1
      raise StopIteration
    else:
      return self._container[self._iterator]
  
  def __reversed__(self):
    return self._container[::-1]

  def load(self, source):
    self._container.clear()
    with open (source, "r") as f:
      reader = csv.DictReader(f)
      for row in reader:
          obat = Obat(row['id_obat'], row['nama_obat'], int(row['stok']), int(row['harga']), row['desc'], row['url_image'])
          self._container.append(obat)
  
  def save(self, target):
    newval = self.toList()
    with open (target, "w", newline="") as f:
      writer = csv.writer(f)
      for row in newval:
        writer.writerow(row)
            
  def toListDict(self):
    headers = ["id_obat","nama_obat","stok","harga","desc","url_image"]
    result = []
    for obat in self._container:
        val = [obat.getIdObat(), obat.getNamaObat(), obat.getStok(), obat.getHargaObat(), obat.getDescObat(), obat.getImgObat()]
        result.append(dict(zip(headers,val)))
    return result

  def toList(self):
    headers = ["id_obat","nama_obat","stok","harga","desc","url_image"]
    result = []
    result.append(headers)
    for obat in self._container:
        val = [obat.getIdObat(), obat.getNamaObat(), obat.getStok(), obat.getHargaObat(), obat.getDescObat(), obat.getImgObat()]
        result.append(val)
    return result

  def findObat(self, id):
    for obat in self._container:
      if obat.getIdObat() == id:
        return obat
    return None

  def findIdxObat(self, id):
    for i, obat in enumerate(self._container):
      if obat.getIdObat() == id:
        return i
    return -1

  def searchObat(self, query):
    out = []
    for obat in self._container:
      if re.search(query, obat.getNamaObat(), re.IGNORECASE):
        out.append(obat)
    return out
  
  def addObat(self, obat):
    self._container.append(obat)
    return len(self._container)-1
  
  def removeObat(self, id):
    idx = None
    obatout = None
    for i, obat in enumerate(self._container):
      if obat.getIdObat() == id:
        idx = i
        obatout = obat
        break
    if idx is not None:
      self._container.pop(idx)
      return obatout
    return None