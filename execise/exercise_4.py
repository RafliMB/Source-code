nama_karyawan = input("Masukkan nama : ").title()

jabatan = (input("Jabatan (Design/Programmer/Resource) : ")).capitalize()
if jabatan == "Design":
    jabatan = 5000000
elif jabatan == "Programmer":
    jabatan = 10000000
else:
    jabatan = 5000000

status_kawin = input("Status perkawinan [Y/T] : ").upper()
if status_kawin == "Y":
    tunjangan = (20/100) * jabatan 
    gaji_kotor = jabatan + tunjangan
else:
    tunjangan = 0
    gaji_kotor = jabatan

pajak = (10/100) * gaji_kotor
total = gaji_kotor - pajak
print(" ")
print('Nama : ' + nama_karyawan)
if jabatan == 5000000:
    jabatan = "Design"
elif jabatan == 10000000:
    jabatan = "Programmer"
else:
    jabatan = "Resource"
print('Jabatan : ' + jabatan)
if jabatan == 'Design':
    jabatan = 5000000
elif jabatan == 'Programmer':
    jabatan = 10000000
else:
    jabatan = 5000000
print(f'[Gaji Pokok : Rp {jabatan:,.0f}]')
print(f'[Tunjangan : Rp {tunjangan:,.0f}]')
print(f'[Gaji Kotor : Rp {gaji_kotor:,.0f}]')
print(f'[Pajak : Rp {pajak:,.0f}]')
print(f'[Total Gaji : Rp {total:,.0f}]')