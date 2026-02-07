#Praktikum 1: Konsep ADT dan file reading
#Latihan Dasar 1A: Membaca seluruh isi file

#Membuka file dengan mode read ("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    Isi_file = file.read()
print(Isi_file) 

print("Tipe Data: ", type(Isi_file))
print("Jumlah Karakter: ", len(Isi_file))
print("Jumlah Baris: ", Isi_file.count("\n")+1)

#Membuka file per baris
Jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        Jumlah_baris += 1
        Baris = baris.strip()
        print("Baris ke- ", Jumlah_baris)
        print("Isi Baris: ", Baris)

#Latihan Dasar 2: Parsing baris menjadi kolom data

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        Baris = baris.strip()
        nim, nama, nilai = Baris.split(",")
        print("NIM: ", nim, "| Nama: ", nama, "\t", "| Nilai: ", nilai)

#Latihan Dasar 3: Struktur Data List

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    data_list = []
    for baris in file:
        Baris = baris.strip()
        nim, nama, nilai = Baris.split(",")
        mahasiswa = [nim, nama, int(nilai)]
        data_list.append(mahasiswa)

print("Data Mahasiswa dalam List: ", data_list)
print("Jumlah Record dalam List: ", len(data_list))
print("Contoh Record pertama: ", data_list[0])

#Latihan Dasar 4: Membaca File dan Menyimpan ke Dictionary

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    data_dict = {}
    for baris in file:
        Baris = baris.strip()
        nim, nama, nilai = Baris.split(",")
        data_dict[nim] = {"nama": nama, "nilai": int(nilai)}
        
print("Data Mahasiswa dalam Dictionary: ", data_dict)