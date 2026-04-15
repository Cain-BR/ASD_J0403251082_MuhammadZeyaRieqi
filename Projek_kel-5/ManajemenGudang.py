#Projek kelompok 5
#Manajemen Tumpukan Gudang Barang Berat Menggunakan Struktur Data Stack
#Muhammad Danish Rahmanu Ghaisan (J0403251124)
#Muhammad Zeya Rieqi (J0403251082)
#Nelson Arsel Warae (J0403251061)
#Algoritma dan Struktur Data
#Teknologi Rekayasa Perangkat Lunak
#Tahun Akademik 2025/2026

#1. Program stack
#2. Program menu

class barang:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, nama, berat):
        barang_baru = barang(nama, berat)
        barang_baru.next = self.top
        self.top = barang_baru

    def pop(self):
        if self.is_empty():
            print("Stack kosong")
            return None
        nama_teratas = self.top.nama
        berat_teratas = self.top.berat
        self.top = self.top.next
        print(f"Barang yang di-pop: {nama_teratas}, Berat: {berat_teratas}")
        return (nama_teratas, berat_teratas)

    def tampilkan(self):
        current = self.top
        no = 1
        while current is not None:
            print(f"{no}. Nama: {current.nama}, Berat: {current.berat}")
            current = current.next
            no += 1

def main():
    stack = Stack()
    while True:
        print("Manajemen Tumpukan Gudang Barang Berat")
        print("1. Tambah Barang (Push)")
        print("2. Hapus Barang Teratas (Pop)")
        print("3. Lihat Tumpukan Barang")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama barang: ")
            berat = float(input("Masukkan berat barang: "))
            stack.push(nama, berat)
        elif pilihan == "2":
            stack.pop()
        elif pilihan == "3":
            stack.tampilkan()
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")    

if __name__ == "__main__":
    main()