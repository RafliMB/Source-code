nama = str(input('Masukkan nama : '))
jam_kerja = int(input('Masukkan jam kerja : '))
tarif = int(input('Masukkan tarif : '))

gaji_perbulan = jam_kerja * tarif
gaji_perbulan *= 20
print([nama,f'Rp{gaji_perbulan}'])
if (gaji_perbulan < 3000000):
    print('Gaji anda dibawah UMR')