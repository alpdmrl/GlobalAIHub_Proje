# Alperen Demirel
# Pizza Sipariş Sistemi Projesi
#######################################

#Gerekli kitaplıkların içe aktarılması 
import csv 
from datetime import datetime
import datetime 
     

#Menüyü göstermek için menu.txt dosyasının okutulması
def readMenu():
    with open('Menu.txt', 'r') as f:
        for line in f:
            print(line, end='')
     

# "Pizza" üst sınıfının tanımlanması ve gerekli methodların eklenmesi
class Pizza:
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description 
    def get_description(self):
        return self.description
    def get_cost(self):
        return self.cost
     
#"Pizza" üst sınıfının alt sınıflarını tanımlama. 
class Klasik(Pizza):
      def __init__(self):
        self.description = 'İçindekiler: Mantar, Kaşar Peyniri, Domates, Sucuk, Salam ve Sosis '
        self.cost = 95.00

class Margarita(Pizza):
     def __init__(self):
        self.description = 'İçindekiler: Domates, Mozzarella Peyniri, Taze Fesleğen Yaprakları, Zeytinyağı, Sarımsak '
        self.cost = 100.00

class Turk(Pizza):
    def __init__(self):
        self.description = 'İçindekiler: Kıyma, Sucuk, Domates, Biber, Soğan ve Kaşar '
        self.cost = 120.00

class Dominos(Pizza):
    def __init__(self):
        self.description = 'İçindekiler: Domates, Cheddar Peyniri ve Zeytin '
        self.cost = 85.00
     

#Tüm sos sınıflarının süper sınıfı olan Decorator üst sınıfının oluşturulması 
class Decorator(Pizza):
  def __init__(self, sos):
          self.sos = sos

  def get_description(self):
          return self.sos.get_description() + ', ' + Pizza.get_description(self)

  def get_cost(self):
           return self.sos.get_cost() + Pizza.get_cost(self)
     

#Decorator üst sınıfının alt sınıfları olan sosların oluşturulması.

class Zeytin(Decorator):
    def __init__(self, sos):
       super().__init__(sos)
       self.description = 'Zeytin'
       self.cost = 1.50

class Mantar(Decorator):
   def __init__(self, sos):
       super().__init__(sos)
       self.description = 'Mantar'
       self.cost = 2.00

class KeciPeyniri(Decorator):
    def __init__(self, sos):
       super().__init__(sos)
       self.description = 'Keçi Peyniri'
       self.cost = 3.00

class Et(Decorator):
    def __init__(self, sos):
       super().__init__(sos)
       self.description = 'Et'
       self.cost = 5.00

class Sogan(Decorator):
    def __init__(self, sos):
       super().__init__(sos)
       self.description = 'Soğan'
       self.cost = 3.50

class Misir(Decorator):
    def __init__(self, sos):
       super().__init__(sos)
       self.description = 'Misir'
       self.cost = 6.00
     

# Menünün ekrana yazdırılması

def main():
    with open("Menu.txt", "r") as menu:
        for i in menu:
            print(i, end="")

    class_dict = {1: Klasik,
                  2: Margarita,
                  3: Turk,
                  4: Dominos,
                  11: Zeytin,
                  12: Mantar,
                  13: KeciPeyniri,
                  14: Et,
                  15: Sogan,
                  16: Misir}

    button = input("Lütfen Pizzanızı Seçiniz: ")
    while button not in ["1", "2", "3", "4"]:
        button = input("Lütfen geçerli bir sayı girin: ")

    order = class_dict[int(button)]()

    while button != "x":
        button = input(
            "Fazladan malzeme almak istiyorsanız lütfen numara giriniz. Almak istemezseniz siparişinizi Onaylamak için 'x' tuşuna basınız: ")
        if button in ["11", "12", "13", "14", "15", "16"]:
            order = class_dict[int(button)](order)

    print("\n" + order.get_description().strip() + " - Ödenmesi gereken toplam tutar: " + str(order.get_cost()) + ' TL')
    print("\n")
     

# Kullanıcının veritabanına kaydedilmesi

    print("KULLANICI BİLGİLERİ\n")
    name = input("İsim: ")
    TC = input("TC Kimlik Numarası: ")
    cc_no = input("Kredi Kartı Numarası: ")
    cc_pass = input("Kredi Kartı Şifresi: ")
    time = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([name, TC, cc_no, cc_pass, order.get_description(), time])
    print("\nSiparişiniz Onaylandı.\n\nBizi Tercih Ettiğiniz İçin Teşekkür ederiz!")


main()
     