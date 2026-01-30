# definisikan class Namaclass
class Cat:
    #kosongan
    #__init__ = yang pertama kali di akses
    # definisikan atribut didalam konstruktor
    def __init__(self, color, height, weight):
        self.color = color
        self.height = height
        self.weight = weight
        

# buat object dari class cat
garfield = Cat("Orange", 25, 10)
persia = Cat("White", 20, 11)
# debug obje di memory kita
print("Obj Garfield: ", garfield)
print("Obj Persia: ", persia)

# panggil nama atribut dari objek
print(f"Warna persia: {persia.color}")
print(f"tinggi Garfield: {garfield.height}")