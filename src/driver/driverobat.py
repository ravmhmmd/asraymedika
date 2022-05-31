from src.classes.bag import BagObat
from src.classes.obat import Obat
from src.classes.ListObat import ListObat

db = ListObat(source="database/obat.csv")
cart = BagObat()

print("Database")
print("Tes add and iterable")

db.addObat(Obat("AM011", "Habbatus Sauda", 1, 99999, "Obat segala penyakit", "link.img"))

for obat in db:
  print(obat.getIdObat(), obat.getNamaObat())

print("\nTes getter db")
print(db[0].getIdObat(), db[0].getNamaObat())

# print("Tes save db")
# db.save("database/obat2.csv")

print("\nCart")
print("Tes add and iterable cart")

cart.add("AM002")
cart.add("AM010")
cart.add("AM004")
cart.increase("AM010", 5)

for idobat, qty in cart:
  obat = db.findObat(idobat)
  print(idobat, obat.getNamaObat(), "berjumlah", qty)

print("tes query")
print(db.searchObat("panadol"))

cart.addFromReceipt(db, source="resep1.txt")
cart.printBag(db)
cart.checkout(db)
