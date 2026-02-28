#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 3: Mencari Nilai Maksimum

def cari_maks(data, indeks=0):
    if indeks == len(data) - 1:
        return data[indeks]
    maks_sisa = cari_maks(data, indeks + 1)
    if data[indeks] > maks_sisa:
        return data[indeks]
    else:
        return maks_sisa
    
angka = [3, 9, 2, 7, 5]
print("Nilai maksimum: ", cari_maks(angka))