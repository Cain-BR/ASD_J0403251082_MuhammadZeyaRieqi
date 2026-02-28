#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Materi Rekursif: Faktorial
#3! = 3 x 2 x 1 = 6
#Base case => 0 berhenti

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n*faktorial(n-1)
    
print("Hasil Faktorial: ", faktorial(3))