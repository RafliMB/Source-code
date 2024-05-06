nilai = int(input("Masukkan Nilai (Range : 0-100) : "))
if nilai <= 0 or nilai >= 100:
    print('Error : Range 0 - 100')
    exit() # Digunakan untuk mengakhiri eksekusi 
print('Benar')

if nilai > 85:
    print('Index A')
elif nilai >= 65 and nilai < 85:
    print('Index B')
else:
    print('Index C')

umur = int(input("Masukkan Umur : "))
if umur >= 17:
    undangan = input('Punya undangan [Y/T] : ').upper()
    if undangan == "Y":
        print('Boleh nyoblos')
    else:
        print('Daftar pemilu')
else:
    print('Umur tidak memenuhi syarat')