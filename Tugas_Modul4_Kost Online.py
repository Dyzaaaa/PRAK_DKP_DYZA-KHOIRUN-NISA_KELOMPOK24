class login_method:
    def __init__(self, list1, list2, list3, list4) :
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
        self.list4 = list4

    def awal(self):
        print("===== SELAMAT DATANG DI IBUKOST =====")
        print()
        print("         KOST YANG TERSEDIA      \n ")
        print(f'1. {self.list1} (JAKARTA)\n2. {self.list2} (SEMARANG)\n3. {self.list3} (BALI)\n4. {self.list4} (TANGGERANG)\n')
from method import *
pembuka = login_method("KOST KUTANG", "KOST MAWAR", "KOST MELATI", "KOST KAKI")
pembuka.awal()

#function 
def user ():
    print("LOGIN BERHASIL\n")
    nama = str(input('MASUKAN NAMA LENGKAP: '))
    kost = int(input("PILIH KOST: "))
    while(True):
        if (kost == 1):
            print("SELAMAT DATANG DI KOST KUTANG\nFASILITAS: KOLAM RENANG DALAM DAN KAMAR MANDI LUAR")
            harga = 1500000
            print("HARGA: 1,5 jt / bulan")
            bulan = int(input("DURASI SEWA(BULAN):"))
            ht = harga * bulan
            print("TOTAL YANG HARUS DIBAYAR: ",ht)
            print("///////////////////////")
            print("TERIMA KASIH",nama,"SUDAH MEMPERCAYAI IBU KOST")
            break;
        elif (kost == 2):
            print("SELAMAT DATANG DI KOST MAWAR\nFASILITAS: AC DAN KAMAR MANDI DALAM")
            harga = 1900000
            print("HARGA: 1,9 jt / bulan")
            bulan = int(input("DURASI SEWA(BULAN):"))
            ht = harga * bulan
            print("TOTAL YANG HARUS DIBAYAR: ",ht)
            print("///////////////////////")
            print("TERIMA KASIH",nama,"SUDAH MEMPERCAYAI IBU KOST")
            break;
