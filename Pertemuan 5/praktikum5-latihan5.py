#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Studi Kasus: Generator PIN

def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN: ", hasil)
        return
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)