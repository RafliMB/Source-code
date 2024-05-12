jumlah_barang = int(input("Masukkan jumlah barang : "))

total = 0
ulang = 1
while jumlah_barang > 0:
    harga_barang = int(input(f"Masukkan harga barang ke-{ulang} : "))
    if jumlah_barang == 0:
        break
    jumlah_barang -= 1
    total += harga_barang
    ulang += 1

total 
print(f"Total Belanjaan : Rp{total:,.0f}")