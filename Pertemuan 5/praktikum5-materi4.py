#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Materi Rekursif: Backtracking Kombinasi Biner (n)

def biner(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    biner(n, hasil + "0")
    biner(n, hasil + "1")

biner(3)