pekerjaanlist = ("PNS,Tentara")
nama = str(input("Masukkan Nama : "))
pekerjaan = str(input("Masukkan Pekerjaan Ortu : "))
umur = int(input("Masukkan Umur : "))
gaji_ortu = int(input("Masukkan Gaji Ortu : "))
ipk = float(input("Masukkan IPK anda : "))

if pekerjaan not in pekerjaanlist and gaji_ortu <= 1000000 and ipk >= 2.5 and umur < 25:
    print('selamat anda dpt beasiswa')
else:
    print('nice try')