def bmi(berat,tinggi):
    return berat/(2**tinggi)

def rekomendasi(bmi):
    if bmi < 18.5:
        print("Kategori BMI    : Berat badan kurang")
        return bmi
    elif bmi >= 18.5 and bmi < 24.9:
        print("Kategori BMI    : Berat badan normal")
        return bmi
    elif bmi >= 25 and bmi < 29.9:
        print("Kategori BMI    : Kelebihan berat badan")
        return bmi
    elif bmi >= 30:
        print("Kategori BMI    : Obesitas") 
        return bmi