# input suhu dalam Celcius dari pengguna
Celcius = "c"
Fahrenheit = "f"

Celcius = float(input("masukkan suhu dalam Celcius: "))

# konversi Celcius ke Fahrenheit
Fahrenheit =(Celcius * 9/5 ) + 32

# tampilkan hasil konversi 
print(f"suhu dalam Fahrenheit: {Fahrenheit}derajat Fahrenheit")

print()
print()

# input suhu dalam Fahrenheit
Fahrenheit = "f"
Celcius = "c"

Fahrenheit = float(input("masukkan suhu dalam Fahrenheit"))

# konversi Fahrenheit ke Celcius
celsius = (fahrenheit - 32) * 5/9

 # Tampilkan hasil konversi
print(f"Suhu dalam Celsius adalah: {celsius} derajat Celsius")

print()
print()

# Input suhu dalam Kelvin 
Kelvin = "k"
Celcius = "c"

kelvin = float(input("Masukkan suhu dalam Kelvin: "))

# Konversi Kelvin ke Celsius
celsius = kelvin - 273.15

# Tampilkan hasil konversi
print(f"Suhu dalam Celsius adalah: {celsius} derajat Celsius")