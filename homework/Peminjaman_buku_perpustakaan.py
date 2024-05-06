user = str(input("Masukkan Nama atau NIM : "))
terdaftar = ['Rafli Miftahul Bachtiar', '23090117']
if user not in terdaftar:
    print("Daftarkan diri anda terlebih dahulu")
    str(input("Masukkan nama : "))
    str(input("Masukkan NIM : "))

judul_buku = str(input("Masukkan judul buku : "))
pengarang = str(input("Masukkan nama pengarang : "))
tahun_terbit = str(input("Masukkan tahun terbit : "))

buku = ["Dilan, Dia adalah dilanku tahun 1990", "Pidi Baiq", "2018"]
if judul_buku and pengarang and tahun_terbit in buku:
    print([f"Judul : " + buku[0]])
    print([f"Pengarang : " + buku[1]])
    print([f"Tahun terbit : " + buku[2]])
    print(f"Silahkan kembalikan buku dalam 14 Hari")
else:
    print("Anda salah memasukkan data")