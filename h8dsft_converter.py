# Define fungsi untuk konversi dengan 3 argument
# awal sebagai satuan temperature saat ini
# akhir sebagai satuan temperatur tujuan
# temp adalah besaran temperature
def konversi(awal,akhir,temp):
    # konversi dari satuan celcius
    if awal == 1:
        # konversi untuk celcius ke kelvin
        if akhir == 2:
            x = temp - 273.15
            print(f"{temp} C = {x} K")
        # konversi untuk celcius ke fahrenheit
        elif akhir == 3 :
            x = ((9/5)*temp) + 32
            print(f"{temp} C = {x} F")
        else:
            print("Anda Mengkonversi dari celcius ke celcius. Pilih satuan lain")
    # konversi dari satuan kelvin
    if awal == 2:
        # konversi untuk kelvin ke celcius
        if akhir == 1:
            x = temp + 273.15
            print(f"{temp} K = {x} C")
        # konversi untuk kelvin ke fahrenheit
        elif akhir == 3:
            x = ((9/5)*temp)-459.67
            print(f"{temp} K = {x} F")
        else:
            print("Anda Mengkonversi dari kelvin ke kelvin. Pilih satuan lain")
    # konversi dari satuan fahrenheit
    if awal == 3:
        # konversi untuk fahrenheit ke celcius
        if akhir == 1:
            x = (5/9)*(temp-32)
            print(f"{temp} F = {x} C")
        # konversi untuk fahrenheit ke kelvin
        elif akhir == 2:
            x = (5/9)*(temp+459.67)
            print(f"{temp} F = {x} K")
        else:
            print("Anda Mengkonversi dari fahrenheit ke fahrenheit. Pilih satuan lain")

# while loop untuk pengulangan konversi
ulang = 0
while ulang == 0:
    # Judul Program
    print("Konversi Temperature\n")
    # while loop untuk memastikan inputan sesuai dengan format
    step = 0
    while step == 0:
        # input satuan awal dan satuan tujuan dengan input bilangan integer
        try:
            awal = int(input("Pilih Satuan Awal :\n1.Celcius     2.Kelvin     3.Fahrenheit\n"))
            akhir = int(input("Ingin Konversi ke :\n1.Celcius     2.Kelvin     3.Fahrenheit\n"))
            if awal in [1,2,3,] and akhir in [1,2,3,]:
                break
        # perulangan apabila inputan tidak berupa integer
        except:
            print("\nHarus Berupa Angka !!!\n")
        # perulangan apabila inputan integer namun tidak ada pada pilihan
        else:
            print("\nPilih Sesuai Pilihan !!!")
            continue
    
    # while loop untuk inputan angka temperatur
    while True:
        try:
            temp = float(input("Masukkan Nilai Temperature\n"))
        # while loop apabila inputan temperatur bukan merupakan angka
        except:
            print("Harus Berupa Angka !!!")
        else:
            break
    # pemanggilan fungsi untuk perhitungan
    konversi(awal,akhir,temp)
    # pemilihan untuk mengulang konversi atau tidak
    print("\nTerimakasih\nIngin Konversi Kembali ?")
    lagi = input("Ya[1]     Tidak[Tekan Apapun]\n")
    if lagi == '1':
        ulang = 0
    else:
        ulang = 1