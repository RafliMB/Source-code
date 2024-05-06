string1 = 'Hello'
string2 = 'World!'
int1 = 1
print(string1 + " " + string2)
print((string1 + " ") * 10)
print(string1 + str(int1))

daftar_kalimat = ['aku', 'seorang', 'kapiten']
kalimat = " ".join(daftar_kalimat)
print(kalimat)

daftar_kalimat1 = 'aku seorang programer'
pisah_kata = daftar_kalimat1.split()
print(pisah_kata)

daftar_kalimat2 = "aku programer handal, dan dia handal juga"
substring = daftar_kalimat2.replace('handal', 'hebat')
print(substring)

nama = 'ambatukam ambasing'
print(nama.lower())
print(nama.upper())
print(nama.capitalize())
print(nama.title())

kota = input('Nama Kota : ').title()
print(kota)

uang = 9999999999999999
print('{:,}'.format(uang))
print('{:.2f}'.format(uang))
print('{:,.2f}'.format(uang))

print(f'Rp. {uang:,}')