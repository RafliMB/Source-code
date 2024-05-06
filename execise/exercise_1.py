buku = []
judul_buku = str(input('Masukkan judul buku : '))
tahun_terbit = int(input('Masukkan tahun terbit : '))
harga = float(input('Masukkan harga : '))
penulis = str(input('Masukkan penulis : '))
stock = bool(input('Masukkan ketersediaan buku (kosongkan jika tidak ada) : '))

buku.append(judul_buku)
buku.append(tahun_terbit)
buku.append(harga)
buku.append(penulis)

print(buku)

if (stock == True):
    print('Sedia')
else:
    print('Stock buku kosong')