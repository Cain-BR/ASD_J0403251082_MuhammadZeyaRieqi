#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Materi Rekursif: Backtracking dengan Pruning

def biner_batas(n, batas, hasil="", jumlah_1=0):
    if jumlah_1 > batas:
        return
    if len(hasil) == n:
        print(hasil)
        return
    biner_batas(n, batas, hasil + "0", jumlah_1)
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

biner_batas(4, 2)