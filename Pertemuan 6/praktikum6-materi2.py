#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Insertion Sort dengan Tracing

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

angka = [7, 8, 5, 2, 4, 6]
print("Hasil Insertion Sort: ", insertion_sort(angka))