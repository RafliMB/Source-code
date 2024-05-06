import modul as math

print("Pilih operasi matematika :")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print(" ")

operasi = input(str("Masukkan pilihan anda : "))

if operasi == "1":
    while True:
        num_1 = int(input("Masukkan bilangan pertama : "))
        num_2 = int(input("Masukkan bilangan kedua : "))
        print(f"Hasil penjumlahan :", math.tambah(num_1,num_2))
        print(" ")
elif operasi == "2":
    while True:
        num_1 = int(input("Masukkan bilangan pertama : "))
        num_2 = int(input("Masukkan bilangan kedua : "))
        print(f"Hasil pengurangan :", math.kurang(num_1,num_2))
        print(" ")
elif operasi == "3":
    while True:
        num_1 = int(input("Masukkan bilangan pertama : "))
        num_2 = int(input("Masukkan bilangan kedua : "))
        print(f"Hasil perkalian :", math.kali(num_1,num_2))
        print(" ")