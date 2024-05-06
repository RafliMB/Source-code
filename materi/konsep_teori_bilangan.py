# desimal ke biner
def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

decimal_number = int(input("Masukkan bilangan desimal: "))
binary_number = decimal_to_binary(decimal_number)
print("Bilangan biner :", binary_number)