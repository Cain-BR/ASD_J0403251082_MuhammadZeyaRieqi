#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Buat program dengan menggunakan algoritma Insertion Sort Tracing dengan data = [5, 2, 4, 6, 1, 3]

def insertion_sort(data):
    print("Data awal: ", data)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        print("Iterasi ke- ", i)
        print("Key: ", key)
        print("Bagian kiri(terurut): ", data[:i])
        print("Bagian kanan(belum terurut): ", data[i:])
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        print("Setelah disisipkan: ", data)
    return data

data = [5, 2, 4, 6, 1, 3]
print("Hasil Insertion Sort: ", insertion_sort(data))

'''
1. Tuliskan isi list setelah iterasi i = 1
    - [2, 5, 4, 6, 1, 3]
2. Tuliskan isi list setelah iterasi i = 3
    - [2, 4, 5, 6, 1, 3]
3. Berapa kali pergeseran terjadi pada iterasi i = 4?
    - 4 kali (6, 5, 4, 2)
'''