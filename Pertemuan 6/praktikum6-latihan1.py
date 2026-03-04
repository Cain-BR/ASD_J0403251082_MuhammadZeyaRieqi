#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

'''
1. Mengapa perulangan dimulai dari indeks 1?
    - Karena elemen pertama (indeks 0) dianggap sudah terurut
2. Apa fungsi variabel key?
    - Menyimpan nilai elemen yang sedang diproses untuk dibandingkan dengan elemen sebelumnya
3. Mengapa digunakan while, bukan for?
    - Karena jumlah pergeseran elemen yang diperlukan tidak diketahui sebelumnya
4. Operasi apa yang terjadi di dalam while?
    - Elemen yang lebih besar dari key digeser ke kanan untuk memberi ruang bagi key
'''