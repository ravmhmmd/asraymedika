from operator import itemgetter

class BagObat:
  def __init__(self):
    # isi container berupa tuple
    # (id:int, sum:int)
    self._container = []
    self._iterator = -1
  
  # iterator
  # ref: https://towardsdatascience.com/how-to-loop-through-your-own-objects-in-python-1609c81e11ff

  def __iter__(self):
    return self
  
  def __next__(self):
    self._iterator += 1
    if self._iterator >= self.total():
      self._iterator = -1
      raise StopIteration
    else:
      return self._container[self._iterator]
  
  def __reversed__(self):
    return self._container[::-1]

  def __sorted__(self):
    return sorted(self._container, key=itemgetter(0))
  
  def sortById(self, desc = False):
    self._container = self.sortedById(desc)
    return self

  def sortByCount(self, desc = False):
    self._container = self.sortedByCount(desc)
    return self

  def sortedById(self, desc = False):
    if desc:
      return sorted(self._container, key=itemgetter(0))[::-1]
    else:
      return sorted(self._container, key=itemgetter(0))
  
  def sortedByCount(self, desc = False):
    if desc:
      return sorted(self._container, key=itemgetter(1))[::-1]
    else:
      return sorted(self._container, key=itemgetter(1))
  
  def findObatById(self, id):
    index = [idx for idx, tuple in enumerate(self._container) if tuple[0] == id]

    if len(index) == 0:
      return -1
    else:
      return index[0]
  
  def totalObat(self, id):
    idx = self.findObatById(id)

    if idx != -1:
      return self._container[idx][1]
    else:
      return 0

  def total(self):
    return len(self._container)
  
  '''
  param: id = id obat, n = jumlah
  '''
  def add(self, id):    
    idxout = -1
    idx = self.findObatById(id)

    if idx != -1:
      self.increase(id)
      idxout = idx
    else:
      self._container.append((id,1))
      idxout = self.total()-1
    
    return idxout
  
  '''
  param: id = id obat
  '''
  def remove(self, id):
    idx = self.findObatById(id)

    if idx != -1:
      out = self._container[idx]
      self._container.pop(idx)

      return out
    else:
      raise Exception("id tidak ditemukan")
  
  def decrease(self, id, n=1):
    idx = self.findObatById(id)

    if idx != -1:
      if n > self._container[idx][1]:
        raise Exception("n tidak valid")
      
      data = self._container[idx]
      newtuple = (data[0], data[1]-n)
      self._container[idx] = newtuple

      if self._container[idx][1] == 0:
        self.remove(id)
      
      return self
    else:
      raise Exception("id tidak ditemukan")
    
  def increase(self, id, n=1):
    idx = self.findObatById(id)

    if idx != -1:
      if n <= 0:
        raise Exception("n harus lebih dari nol")
      
      data = self._container[idx]
      newtuple = (data[0], data[1]+n)
      self._container[idx] = newtuple

      return self
    else:
      raise Exception("id tidak ditemukan")

  def printBag(self,db):
    if self.total() <= 0:
      print("Bag kosong")
    else:
      for idobat, jumlah in self:
        print("Obat", db.findObat(idobat).getNamaObat(), "berjumlah", jumlah)

  def checkout(self, db):
    if self.total() <= 0:
      print("Bag kosong")
    else:
      for idobat, jumlah in self:
        db.findObat(idobat).decreaseStok(int(jumlah))
      db.save(target="database/obat.csv")
      self._container.clear()

  def addFromReceipt(self, db, source):
    with open(source, "r") as file:
      lines = file.readlines()
      for line in lines:
        args = line.strip().split(" : ")
        namaobat = args[0]
        qty = int(args[1])
        
        search_res = db.searchObat(namaobat)
        if not search_res:
          print(str(namaobat)+" tidak ditemukan.")
          continue
        else:
          obj_obat = search_res[0]
          self.add(obj_obat.getIdObat())
          if qty > 1:
            self.increase(obj_obat.getIdObat(),qty-1)

