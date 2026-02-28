#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 1: Rekursi Pangkat

def pangkat(a, n):
    if n == 0:
        return 1
    else:
        return a * pangkat(a, n-1)
    
print(pangkat(2, 4))