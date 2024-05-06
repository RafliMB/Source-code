i = 1
while i <= 10:
    print("Mari berhitung",i)
    if i == 5:
        break
    i += 1

perulangan = 0
while True:
    main = input("Apa anda ingin keluar [ya/tidak] : ").lower()
    if main == 'ya':
        break
    perulangan += 1
print("Total perulangan : ",perulangan)

angka = 0
while True:
    angka = int(input("Masukkan angka : "))

    if angka % 2 == 0:
        print(angka,"adalah bilangan genap")
    else:
        print(angka,"adalah bilangan ganjil")