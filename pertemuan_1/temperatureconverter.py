
def celciustofahrenheittoreamur():
    print("masukkan Celcius dalam  bentuk angka untuk di konversi ke Fahrenheit, dan Reamur")
    celcius = int(input())
    fahrenheit = float(celcius * 9) / 5 + 32
    reamur = celcius * 0.8
    print("Hasil dari konversi celcius ke fahrenheit adalah")
    print(fahrenheit)
    print("Hasil dari konversi celcius ke reamur adalah")
    print(reamur)

def fahrenheittocelciustoreamur():
    print("masukkan fahrenheit dalam  bentuk angka untuk di konversi ke celcius ,dan reamur")
    fahrenheit = int(input())
    reamur = (fahrenheit - 32) / 2.25
    celcius = float(5) / 9 * (fahrenheit - 32)
    print("Hasil konversi Fahrenheit ke Celcius adalah")
    print(celcius)
    print("Hasil konversi dari fahrenheit ke reamur adalah")
    print(reamur)

def reamurtocelciustofahrenheit():
    print("masukkan reamur dalam  bentuk angka untuk di konversi ke celcius ,dan fahrenheit")
    reamur = int(input())
    fahrenheit = float(reamur * 9) / 4 + 32
    celcius = float(reamur * 5) / 4
    print("Hasil konversi Reamur ke Celcius adalah")
    print(celcius)
    print("Hasil konversi dari reamur ke fahrenheit adalah")
    print(fahrenheit)

# Main
print("pilih salah satu konversi dibawah ini: ")
print("1 Celcius ke fahrenheit dan  reamur")
print("2 Fahrenheit ke celcius dan  reamur")
print("3 Reamur ke celcius dan fahrenheit")
option = int(input())
if option == 1:
    celciustofahrenheittoreamur()
if option == 2:
    fahrenheittocelciustoreamur()
if option == 3:
    reamurtocelciustofahrenheit()
