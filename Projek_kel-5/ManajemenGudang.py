# =====================================================
# Projek Kelompok 5
# Manajemen Tumpukan Gudang Barang Berat
# Menggunakan Struktur Data Stack
#
# Muhammad Danish Rahmanu Ghaisan (J0403251124)
# Muhammad Zeya Rieqi (J0403251082)
# Nelson Arsel Warae (J0403251061)
#
# Mata Kuliah : Algoritma dan Struktur Data
# Program Studi : Teknologi Rekayasa Perangkat Lunak
# Tahun Akademik 2025/2026
# =====================================================


# ==========================================
# CLASS BARANG
# ==========================================
class Barang:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat
        self.next = None


# ==========================================
# CLASS STACK
# ==========================================
class Stack:
    def __init__(self, max_size=5):
        self.top = None
        self.max_size = max_size

    # Mengecek apakah stack kosong
    def is_empty(self):
        return self.top is None

    # Menghitung jumlah barang
    def jumlah_barang(self):
        count = 0
        current = self.top

        while current:
            count += 1
            current = current.next

        return count

    # ======================================
    # PUSH -> Menambahkan barang
    # ======================================
    def push(self, nama, berat):

        # Mengecek apakah stack penuh
        if self.jumlah_barang() >= self.max_size:
            print("Stack penuh! Barang tidak bisa ditambahkan.")
            return

        # Membuat node baru
        barang_baru = Barang(nama, berat)

        # Node baru menunjuk top lama
        barang_baru.next = self.top

        # Top dipindahkan ke node baru
        self.top = barang_baru

        print(f"\nBarang '{nama}' berhasil ditambahkan!")

    # ======================================
    # POP -> Menghapus barang teratas
    # ======================================
    def pop(self):

        if self.is_empty():
            print("Stack kosong! Tidak ada barang.")
            return

        # Menyimpan data barang teratas
        nama = self.top.nama
        berat = self.top.berat

        # Memindahkan top ke node berikutnya
        self.top = self.top.next

        print(f"\nBarang '{nama}' berhasil dihapus.")
        print(f"Berat barang: {berat} kg")

    # ======================================
    # PEEK -> Melihat barang teratas
    # ======================================
    def peek(self):

        if self.is_empty():
            print("Stack kosong!")
            return

        print("\n===== BARANG TERATAS =====")
        print(f"Nama Barang : {self.top.nama}")
        print(f"Berat       : {self.top.berat} kg")

    # ======================================
    # MENAMPILKAN SEMUA BARANG
    # ======================================
    def tampilkan(self):

        if self.is_empty():
            print("\nTumpukan barang kosong.")
            return

        print("\n===== DAFTAR TUMPUKAN BARANG =====")
        print("TOP STACK")
        print("-" * 35)

        current = self.top
        nomor = 1

        while current is not None:

            print(f"{nomor}. Nama Barang : {current.nama}")
            print(f"   Berat        : {current.berat} kg")
            print("-" * 35)

            current = current.next
            nomor += 1

    # ======================================
    # TOTAL BERAT BARANG
    # ======================================
    def total_berat(self):

        if self.is_empty():
            print("Tidak ada barang dalam stack.")
            return

        total = 0
        current = self.top

        while current:
            total += current.berat
            current = current.next

        print(f"\nTotal berat seluruh barang: {total} kg")


# ==========================================
# PROGRAM UTAMA
# ==========================================
def main():

    # Membuat objek stack
    stack = Stack()

    while True:

        print("\n" + "=" * 45)
        print(" MANAJEMEN TUMPUKAN GUDANG BARANG ")
        print("=" * 45)

        print("1. Tambah Barang (Push)")
        print("2. Hapus Barang Teratas (Pop)")
        print("3. Lihat Semua Barang")
        print("4. Lihat Barang Teratas (Peek)")
        print("5. Jumlah Barang")
        print("6. Total Berat Barang")
        print("7. Keluar")

        pilihan = input("\nPilih menu (1-7): ")

        # ==================================
        # MENU 1 -> TAMBAH BARANG
        # ==================================
        if pilihan == "1":

            nama = input("Masukkan nama barang: ")

            try:
                berat = float(input("Masukkan berat barang (kg): "))

                # Validasi berat
                if berat <= 0:
                    print("Berat harus lebih dari 0!")

                else:
                    stack.push(nama, berat)

            except ValueError:
                print("Input berat harus berupa angka!")

        # ==================================
        # MENU 2 -> HAPUS BARANG
        # ==================================
        elif pilihan == "2":
            stack.pop()

        # ==================================
        # MENU 3 -> TAMPILKAN BARANG
        # ==================================
        elif pilihan == "3":
            stack.tampilkan()

        # ==================================
        # MENU 4 -> PEEK
        # ==================================
        elif pilihan == "4":
            stack.peek()

        # ==================================
        # MENU 5 -> JUMLAH BARANG
        # ==================================
        elif pilihan == "5":

            jumlah = stack.jumlah_barang()

            print(f"\nJumlah barang dalam stack: {jumlah}")

        # ==================================
        # MENU 6 -> TOTAL BERAT
        # ==================================
        elif pilihan == "6":
            stack.total_berat()

        # ==================================
        # MENU 7 -> KELUAR
        # ==================================
        elif pilihan == "7":

            print("\nTerima kasih telah menggunakan program.")
            print("Program selesai.")

            break

        # ==================================
        # INPUT MENU SALAH
        # ==================================
        else:
            print("\nPilihan tidak valid!")
            print("Silakan pilih menu 1 - 7.")


# ==========================================
# MENJALANKAN PROGRAM
# ==========================================
if __name__ == "__main__":
    main()