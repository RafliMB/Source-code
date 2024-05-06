jumlah_siswa = int(input('Masukkan jumlah siswa : '))
total_nilai = 0
for x in range(jumlah_siswa):
    nilai = float(input('Masukkan nilai : '))
    total_nilai += nilai

rata_rata = total_nilai / jumlah_siswa
print(f'Rata-rata nilai ujian siswa adalah {rata_rata:.2f}')