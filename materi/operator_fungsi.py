# tanpa parameter
def cetak_string():
    print('Ini fungsi cetak string')
cetak_string()

# dengan parameter
def salam(ucapan):
    print(ucapan)
salam('Selamat Pagi')

def penjumlahan(a,b):
    hasil = a + b
    print(hasil)
penjumlahan(5,10)

def luas_persegi_panjang(panjang,lebar):
    return panjang*lebar
print(luas_persegi_panjang(5,8))


def penjumlahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def perkalian(a,b):
    return a * b

def pangkat(a,b):
    return a ** b


import matematika as math

print(math.penjumlahan(1,6))
print(math.pengurangan(19,7))
print(math.perkalian(2,8))