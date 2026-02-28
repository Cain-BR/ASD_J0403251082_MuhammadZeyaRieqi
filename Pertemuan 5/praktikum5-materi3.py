#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Materi Rekursif: Penjumlahan elemen list

def jumlah_list(data,index=0):
    if index == len(data):
        return 0
    return data[index] + jumlah_list(data,index+1)

print("Program Jumlah Data")
print(jumlah_list([2,4,5]))