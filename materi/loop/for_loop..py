for x in range(5,11):
    print(x)

fruits = ["Semangka","Khuldi","Duren","Apel"]
number = [2,3,4,5,6,7,8]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index,fruit)

print("\n")
for number,fruit in zip(number,fruits):
    print(number,fruit)

print("\n")
names = "Aku Jawa"
for name in names:
    print(name)

print("\n")
biodata = {"Nama":"Rafli","NIM":23090117}
for data in biodata:
    print(data)

for value in biodata.values():
    print(value)

for label,value in biodata.items():
    print(label,":",value)

print("\n")
for i in range(1,11):
    if i % 2 == 0:
        print(i,"Adalah bilangan genap")
    else:
        print(i,"Adalah bilangan ganjil")

print("\n")
for caption in range(10):
    print("Aku jawa")