#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 2: Tracing Rekursi

def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk: ", "\t", n)
    countdown(n-1)
    print("Keluar: ", "\t", n)

countdown(3)