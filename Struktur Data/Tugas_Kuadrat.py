import math

def judul():
    print("==============================================")


def mencariAkar(a, b, c, determinan):
    # masukan rumus
    if (determinan == 0):
        x1 = (-b - math.sqrt(determinan)) / (2 * a)
        x2 = (-b + math.sqrt(determinan)) / (2 * a)
        x1 = x2
        print(f"Jika Determinan = 0, maka x1 = {x1} dan x2 = {x2}")
    elif (determinan > 0):
        x1 = (-b - math.sqrt(determinan)) / (2 * a)
        x2 = (-b + math.sqrt(determinan)) / (2 * a)
        print(f"Nilai Determinan > 0, Maka :")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif (determinan < 0):
        print("Akar Imajiner, tidak memiliki akar nyata")


def mencariDeterminan(a, b, c):
    # rumus determinan
    determinan = b ** 2 - 4 * a * c

    if (determinan == 0):
        print("Punya Akar 1 tunggal")
    elif (determinan > 0):
        print("Punya 2 Akar")
    elif (determinan < 0):
        print("Tidak Punya Akar Nyata")
    print(f"Nilai Determinanya : {determinan}")

    mencariAkar(a, b, c, determinan)


def subKalkulator():
    print("Silahkan Masukkan Nilai A, B, C ")


def main():
    judul()
    subKalkulator()
    a = int(input("Masukkan Nilai A: "))
    b = int(input("Masukkan Nilai B: "))
    c = int(input("Masukkan Nilai C: "))
    if (a == 0):
        print("Mohon Maaf Nilai A Tidak Boleh Kosong!")
        tanya = str(input("Silahkan Ulang program Dengan (Ya [Y]/Tidak [N]): "))
        if (tanya == "Y"):
            main()
        else:
            print("Terima Kasih")
    else:
        mencariDeterminan(a, b, c)
        print("Terima Kasih")
        tanya_2 = str(input("Mencoba Lagi?(Ya [Y] / Tidak [N]): "))
        if (tanya_2 == "Y"):
            main()
        else:
            print("Terima Kasih Telah Mencoba :)")

main()