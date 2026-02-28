#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Materi Rekursif: Call stack
#Tracing bilangan (masuk-keluar)
#Input 3
#Masuk 1-2-3
#Keluar 3-2-1

def hitung(n):
    if n == 0:
        return
    print(f"Masuk: {n}")
    hitung(n-1)
    print(f"Keluar: {n}")

print("Program Tracing")
hitung(3)