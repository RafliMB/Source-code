import modul as BMI

berat_badan = float(input("Masukkan berat badan (Kg)  : "))
tinggi_badan = float(input("Masukkan tinggi badan (m)  : "))

print(f"Berat badan     : {int(berat_badan)} kg")
print(f"Tinggi badan    : {tinggi_badan} m")
print(f"Nilai BMI Anda  : {BMI.bmi(berat_badan,tinggi_badan):.1f}")
BMI.rekomendasi(BMI.bmi(berat_badan,tinggi_badan))