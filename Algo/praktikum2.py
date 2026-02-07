#Praktikum 2: Konsep ADT dan file handling (studi kasus)
#Latihan Dasar 1A: Membuat fungsi load data

nama_file = "data_mahasiswa.txt"
def baca_data_mahasiswa(nama_file):
    with open(nama_file, "r", encoding="utf-8") as file:
        data_dict = {}
        for baris in file:
            Baris = baris.strip()
            nim, nama, nilai = Baris.split(",")
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)}
    return data_dict
buka_data = baca_data_mahasiswa(nama_file)
#print(len(buka_data))

#Latihan Dasar 2A: Membuat fungsi menampilkan data

def tampilkan_data(data_dict):
    print("Data Mahasiswa:")
    print(f"{'NIM':<10} | {'Nama':<10} | {'Nilai':>5}")
    print("_" * 38, "\n")
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<10} | {nilai:>5}")
#tampilkan_data(buka_data)

#Latihan Dasar 3A: Membuat fungsi mencari data berdasarkan NIM
def cari_data(data_dict, nim_cari):
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        print("Data Ditemukan:")
        print(f"Nilai: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("Data dengan NIM tersebut tidak ditemukan.")
#cari_data(buka_data, input("Masukkan NIM yang dicari: "))

#Latihan Dasar 4A: Membuat fungsi update nilai

def update_nilai(data_dict):
    nim = input("Masukkan NIM yang akan diupdate nilainya: ")
    if nim not in data_dict:
        print("NIM tidak ditemukan dalam data.")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru: ").strip())
    except ValueError:
        print("Nilai harus berupa angka.")
        return
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 hingga 100.")
        return
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    
    print(f"Update Berhasil. Nilai berubah dari {nilai_lama} menjadi {nilai_baru}.")

#update_nilai(buka_data)

#Latihan Dasar 5A: Membuat fungsi menyimpan data kembali ke file

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
    print("Data berhasil disimpan.")
#simpan_data(nama_file, buka_data)

#Latihan Dasar 6A: Membuat menu

def main():
    buka_data = baca_data_mahasiswa(nama_file)
    while True:
        print("\nMenu:")
        print("1. Tampilkan Semua Data")
        print("2. Cari Data berdasarkan NIM")
        print("3. Update Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            nim_cari = input("Masukkan NIM yang dicari: ").strip()
            cari_data(buka_data, nim_cari)
        elif pilihan == "3":
            update_nilai(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
        elif pilihan == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()