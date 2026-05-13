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
    def __init__(self, max_size=100, nama_file="gudang.txt"):
        self.top = None
        self.max_size = max_size
        self.nama_file = nama_file

        # Muat data dari file saat program dimulai
        self._muat_dari_file()

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
    # HITUNG TOTAL BERAT (internal, return nilai)
    # ======================================
    def _hitung_total_berat(self):
        total = 0
        current = self.top
        while current:
            total += current.berat
            current = current.next
        return total

    # ======================================
    # SIMPAN KE FILE TXT
    # Format tiap baris: nama|berat
    # Urutan disimpan dari bawah ke atas
    # agar saat dimuat ulang, top tetap benar
    # ======================================
    def _simpan_ke_file(self):
        try:
            # Kumpulkan semua barang dari top ke bawah
            barang_list = []
            current = self.top
            while current:
                barang_list.append(current)
                current = current.next

            # Tulis ke file dari bawah ke atas
            with open(self.nama_file, "w") as f:
                for barang in reversed(barang_list):
                    f.write(f"{barang.nama}|{barang.berat}\n")

        except IOError as e:
            print(f"\n[ERROR] Gagal menyimpan ke file: {e}")

    # ======================================
    # MUAT DARI FILE TXT
    # ======================================
    def _muat_dari_file(self):
        try:
            with open(self.nama_file, "r") as f:
                lines = f.readlines()

            # Push satu per satu (baris terakhir = top)
            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 2:
                        nama = parts[0]
                        berat = float(parts[1])
                        barang_baru = Barang(nama, berat)
                        barang_baru.next = self.top
                        self.top = barang_baru

            if not self.is_empty():
                print(f"[INFO] Data berhasil dimuat dari '{self.nama_file}'.")
                print(f"       {self.jumlah_barang()} barang | {self._hitung_total_berat()} kg")

        except FileNotFoundError:
            # File belum ada, mulai dari kosong
            pass
        except (IOError, ValueError) as e:
            print(f"\n[ERROR] Gagal membaca file: {e}")

    # ======================================
    # PUSH -> Menambahkan barang
    # ======================================
    def push(self, nama, berat):

        # Cek kapasitas
        berat_sekarang = self._hitung_total_berat()
        if berat_sekarang + berat >= self.max_size:
            sisa = self.max_size - berat_sekarang
            print(f"\nMuatan terlalu berat! Barang tidak bisa ditambahkan.")
            print(f"Berat saat ini  : {berat_sekarang} kg")
            print(f"Sisa kapasitas  : {sisa} kg")
            print(f"Batas maksimum  : {self.max_size} kg")
            return

        # Buat node baru
        barang_baru = Barang(nama, berat)
        barang_baru.next = self.top
        self.top = barang_baru

        # Simpan ke file
        self._simpan_ke_file()

        print(f"\nBarang '{nama}' berhasil ditambahkan!")
        print(f"Total berat sekarang: {self._hitung_total_berat()} kg / {self.max_size} kg")
        print(f"Data tersimpan ke '{self.nama_file}'.")

    # ======================================
    # POP -> Menghapus barang teratas
    # ======================================
    def pop(self):

        if self.is_empty():
            print("Stack kosong! Tidak ada barang.")
            return

        nama  = self.top.nama
        berat = self.top.berat
        self.top = self.top.next

        # Simpan ke file
        self._simpan_ke_file()

        print(f"\nBarang '{nama}' berhasil dihapus.")
        print(f"Berat barang: {berat} kg")
        print(f"Data tersimpan ke '{self.nama_file}'.")

    # ======================================
    # MENAMPILKAN SEMUA BARANG
    # ======================================
    def tampilkan(self):

        if self.is_empty():
            print("\nTumpukan barang kosong.")
            return

        print("\n===== DAFTAR TUMPUKAN BARANG =====")
        print("-" * 35)

        current = self.top
        nomor = 1

        while current is not None:
            print(f"{nomor}. Nama Barang : {current.nama}")
            print(f"   Berat        : {current.berat} kg")
            print("-" * 35)
            current = current.next
            nomor += 1

        print(f"Total berat: {self._hitung_total_berat()} kg / {self.max_size} kg")

    # ======================================
    # TOTAL BERAT BARANG
    # ======================================
    def total_berat(self):

        if self.is_empty():
            print("Tidak ada barang dalam stack.")
            return

        total = self._hitung_total_berat()
        print(f"\nTotal berat seluruh barang : {total} kg")
        print(f"Kapasitas maksimum          : {self.max_size} kg")
        print(f"Sisa kapasitas              : {self.max_size - total} kg")

    # ======================================
    # UBAH INFORMASI BARANG
    # ======================================
    def ubah_informasi(self, nama_lama, nama_baru, berat_baru):
        if self.is_empty():
            print("Stack kosong! Tidak ada barang.")
            return

        current = self.top
        found = False

        while current:
            if current.nama == nama_lama:
                current.nama = nama_baru
                current.berat = berat_baru
                found = True
                break
            current = current.next

        if found:
            # Simpan ke file
            self._simpan_ke_file()
            print(f"\nInformasi barang '{nama_lama}' berhasil diubah!")
            print(f"Data tersimpan ke '{self.nama_file}'.")
        else:
            print(f"\nBarang dengan nama '{nama_lama}' tidak ditemukan.")


# ==========================================
# PROGRAM UTAMA
# ==========================================
def main():

    stack = Stack()

    while True:

        print("\n" + "=" * 45)
        print(" MANAJEMEN TUMPUKAN GUDANG BARANG ")
        print("=" * 45)

        print("1. Masukkan Barang")
        print("2. Keluarkan Barang")
        print("3. Lihat Semua Barang")
        print("4. Jumlah Barang")
        print("5. Total Berat Barang")
        print("6. Ubah Informasi Barang")
        print("0. Keluar")

        pilihan = input("\nPilih menu (0-6): ")

        # ==================================
        # MENU 1 -> TAMBAH BARANG
        # ==================================
        if pilihan == "1":
            nama = input("Masukkan nama barang: ")
            try:
                berat = float(input("Masukkan berat barang (kg): "))
                if berat <= 0:
                    print("Masukkan berat yang valid (lebih dari 0 kg)!")
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
        # MENU 4 -> JUMLAH BARANG
        # ==================================
        elif pilihan == "4":
            jumlah = stack.jumlah_barang()
            print(f"\nJumlah barang dalam stack: {jumlah}")

        # ==================================
        # MENU 5 -> TOTAL BERAT
        # ==================================
        elif pilihan == "5":
            stack.total_berat()

        # ==================================
        # MENU 6 -> UBAH INFORMASI BARANG
        # ==================================
        elif pilihan == "6":
            nama_lama = input("Masukkan nama barang yang ingin diubah: ")
            nama_baru = input("Masukkan nama baru: ")
            try:
                berat_baru = float(input("Masukkan berat baru (kg): "))
                if berat_baru <= 0:
                    print("Masukkan berat yang valid (lebih dari 0 kg)!")
                else:
                    stack.ubah_informasi(nama_lama, nama_baru, berat_baru)
            except ValueError:
                print("Input berat harus berupa angka!")

        # ==================================
        # MENU 0 -> KELUAR
        # ==================================
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan program.")
            print("Program selesai.")
            break

        # ==================================
        # INPUT MENU SALAH
        # ==================================
        else:
            print("\nPilihan tidak valid!")
            print("Silakan pilih menu 0 - 6.")


# ==========================================
# MENJALANKAN PROGRAM
# ==========================================
if __name__ == "__main__":
    main()