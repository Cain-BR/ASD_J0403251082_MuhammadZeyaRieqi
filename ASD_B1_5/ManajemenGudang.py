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
    def __init__(self, nama, berat, indeks):
        self.nama = nama
        self.berat = berat
        self.indeks = indeks   # urutan masuk: barang pertama = 1
        self.next = None


# ==========================================
# CLASS STACK
# ==========================================
class Stack:
    def __init__(self, max_size=100, nama_file="gudang.txt"):
        self.top = None
        self.max_size = max_size
        self.nama_file = nama_file
        self.indeks_counter = 0   # cacah total barang yang pernah masuk

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
            barang_list = []
            current = self.top
            while current:
                barang_list.append(current)
                current = current.next

            # Format: indeks|nama|berat
            # Tulis dari bawah ke atas agar urutan stack tetap benar saat dimuat
            with open(self.nama_file, "w") as f:
                f.write(f"#counter:{self.indeks_counter}\n")
                for barang in reversed(barang_list):
                    f.write(f"{barang.indeks}|{barang.nama}|{barang.berat}\n")

        except IOError as e:
            print(f"\n[ERROR] Gagal menyimpan ke file: {e}")

    # ======================================
    # MUAT DARI FILE TXT
    # ======================================
    def _muat_dari_file(self):
        try:
            with open(self.nama_file, "r") as f:
                lines = f.readlines()

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                # Baca counter dari baris pertama
                if line.startswith("#counter:"):
                    self.indeks_counter = int(line.split(":")[1])
                    continue

                parts = line.split("|")
                if len(parts) == 3:
                    indeks = int(parts[0])
                    nama   = parts[1]
                    berat  = float(parts[2])
                    barang_baru = Barang(nama, berat, indeks)
                    barang_baru.next = self.top
                    self.top = barang_baru

            if not self.is_empty():
                print(f"[INFO] Data berhasil dimuat dari '{self.nama_file}'.")
                print(f"       {self.jumlah_barang()} barang | {self._hitung_total_berat()} kg")

        except FileNotFoundError:
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
            print(f"Batas maksimum  : {self.max_size - 1} kg")
            return

        # Buat node baru dengan indeks berikutnya
        self.indeks_counter += 1
        barang_baru = Barang(nama, berat, self.indeks_counter)
        barang_baru.next = self.top
        self.top = barang_baru

        # Simpan ke file
        self._simpan_ke_file()

        print(f"\nBarang '{nama}' berhasil ditambahkan!")
        print(f"Total berat sekarang: {self._hitung_total_berat()} kg / {self.max_size - 1} kg")
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
    # HELPER: ambil semua barang sebagai list
    # ======================================
    def _ke_list(self):
        hasil = []
        current = self.top
        while current:
            hasil.append(current)
            current = current.next
        return hasil

    # ======================================
    # HELPER: cetak tabel barang dari list
    # ======================================
    def _cetak_tabel(self, barang_list):
        print("-" * 50)
        print(f"{'No':<4} {'Indeks':<8} {'Nama Barang':<20} {'Berat':>8}")
        print("-" * 50)
        for no, b in enumerate(barang_list, 1):
            print(f"{no:<4} {b.indeks:<8} {b.nama:<20} {b.berat:>6} kg")
        print("-" * 50)
        print(f"Total berat: {self._hitung_total_berat()} kg / {self.max_size - 1} kg")

    # ======================================
    # MENAMPILKAN SEMUA BARANG
    # ======================================
    def tampilkan(self, mode="tumpukan", ascending=True):
        if self.is_empty():
            print("\nTumpukan barang kosong.")
            return

        barang_list = self._ke_list()

        if mode == "tumpukan":
            barang_list.sort(key=lambda b: b.berat, reverse=not ascending)
            arah  = "Ringan → Berat" if ascending else "Berat → Ringan"
            label = f"URUTAN BERAT BARANG — {arah}"

        elif mode == "indeks":
            barang_list.sort(key=lambda b: b.indeks, reverse=not ascending)
            arah  = "Ascending" if ascending else "Descending"
            label = f"URUTAN INDEKS MASUK — {arah}"

        elif mode == "alphabet":
            barang_list.sort(key=lambda b: b.nama.lower(), reverse=not ascending)
            arah  = "A → Z" if ascending else "Z → A"
            label = f"URUTAN ALPHABET — {arah}"

        else:
            print("Mode tampil tidak dikenal.")
            return

        print(f"\n===== DAFTAR BARANG: {label} =====")
        self._cetak_tabel(barang_list)

    # ======================================
    # CARI BARANG (partial match, case-insensitive)
    # ======================================
    def cari(self, kata_kunci):
        if self.is_empty():
            print("\nStack kosong! Tidak ada barang.")
            return

        kata_kunci = kata_kunci.strip().lower()

        if not kata_kunci:
            print("\nKata kunci tidak boleh kosong.")
            return

        # Kumpulkan semua barang yang cocok
        hasil = []
        current = self.top
        while current:
            if kata_kunci in current.nama.lower():
                hasil.append(current)
            current = current.next

        if not hasil:
            print(f"\nTidak ada barang yang cocok dengan '{kata_kunci}'.")
            return

        print(f"\n===== HASIL PENCARIAN: '{kata_kunci}' =====")
        print(f"Ditemukan {len(hasil)} barang:\n")
        self._cetak_tabel(hasil)

    # ======================================
    # TOTAL BERAT BARANG
    # ======================================
    def total_berat(self):

        if self.is_empty():
            print("Tidak ada barang dalam stack.")
            return

        total = self._hitung_total_berat()
        print(f"\nTotal berat seluruh barang : {total} kg")
        print(f"Kapasitas maksimum          : {self.max_size - 1} kg")
        print(f"Sisa kapasitas              : {self.max_size - 1 - total} kg")

    # ======================================
    # UBAH INFORMASI BARANG
    # ======================================
    def ubah_informasi(self, ubah_indeks, nama_baru, berat_baru):

        if self.is_empty():
            print("Stack kosong! Tidak ada barang.")
            return

        try:
            ubah_indeks = int(ubah_indeks)
        except ValueError:
            print("Indeks harus berupa angka!")
            return

        current = self.top
        while current:
            if current.indeks == ubah_indeks:
                print(f"\nBarang ditemukan: {current.nama} (Berat: {current.berat} kg)")
                current.nama = nama_baru
                current.berat = berat_baru
                self._simpan_ke_file()
                print("Informasi barang berhasil diubah.")
                return
            current = current.next

        print(f"\nBarang dengan indeks {ubah_indeks} tidak ditemukan.") 


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
        print("7. Cari Barang")
        print("0. Keluar")

        pilihan = input("\nPilih menu (0-7): ")

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
        
        # Saat user memilih menu 1, setelah memasukkan nama dan berat, program akan mencoba menambahkan barang ke stack. Jika berat yang dimasukkan melebihi kapasitas maksimum, program akan memberikan informasi tentang berat saat ini, sisa kapasitas, dan batas maksimum. Jika berhasil ditambahkan, program akan menampilkan total berat sekarang dan konfirmasi bahwa data telah disimpan ke file.

        # ==================================
        # MENU 2 -> HAPUS BARANG
        # ==================================
        elif pilihan == "2":
            stack.pop()

        # Saat user memilih menu 2, program akan mencoba menghapus barang teratas dari stack. Jika stack kosong, program akan memberitahu bahwa tidak ada barang yang bisa dihapus. Jika berhasil dihapus, program akan menampilkan nama dan berat barang yang dihapus, serta konfirmasi bahwa data telah disimpan ke file.

        # ==================================
        # MENU 3 -> TAMPILKAN BARANG
        # ==================================
        elif pilihan == "3":

            print("\n--- Urutan Tampilan ---")
            print("1. Berat Barang - Ringan → Berat")
            print("2. Berat Barang - Berat → Ringan")
            print("3. Indeks Masuk - Ascending")
            print("4. Indeks Masuk - Descending")
            print("5. Alphabet - A → Z")
            print("6. Alphabet - Z → A")

            sub = input("Pilih urutan (1-6): ")

            if sub == "1":
                stack.tampilkan(mode="tumpukan", ascending=True)
            elif sub == "2":
                stack.tampilkan(mode="tumpukan", ascending=False)
            elif sub == "3":
                stack.tampilkan(mode="indeks", ascending=True)
            elif sub == "4":
                stack.tampilkan(mode="indeks", ascending=False)
            elif sub == "5":
                stack.tampilkan(mode="alphabet", ascending=True)
            elif sub == "6":
                stack.tampilkan(mode="alphabet", ascending=False)
            else:
                print("Pilihan tidak valid, menampilkan urutan tumpukan.")
                stack.tampilkan(mode="tumpukan")

        # Saat user memilih menu 3, program akan menampilkan sub-menu untuk memilih urutan tampilan barang. User dapat memilih untuk mengurutkan berdasarkan berat (dari ringan ke berat atau sebaliknya), indeks masuk (ascending atau descending), atau nama barang (A → Z atau Z → A). Program akan menampilkan daftar barang sesuai dengan urutan yang dipilih, beserta total berat dan kapasitas maksimum.

        # ==================================
        # MENU 4 -> JUMLAH BARANG
        # ==================================
        elif pilihan == "4":
            jumlah = stack.jumlah_barang()
            print(f"\nJumlah barang dalam stack: {jumlah}")

        # Saat user memilih menu 4, program akan menghitung dan menampilkan jumlah barang yang saat ini ada dalam stack. Jika stack kosong, jumlah yang ditampilkan akan menjadi 0.

        # ==================================
        # MENU 5 -> TOTAL BERAT
        # ==================================
        elif pilihan == "5":
            stack.total_berat()

        # Saat user memilih menu 5, program akan menghitung total berat seluruh barang yang ada dalam stack dan menampilkan informasi tersebut.

        # ==================================
        # MENU 6 -> UBAH INFORMASI BARANG
        # ==================================
        elif pilihan == "6":
            ubah_indeks = input("Masukkan indeks barang yang ingin diubah: ")
            nama_baru = input("Masukkan nama baru: ")
            try:
                berat_baru = float(input("Masukkan berat baru (kg): "))
                if berat_baru <= 0:
                    print("Masukkan berat yang valid (lebih dari 0 kg)!")
                else:
                    stack.ubah_informasi(ubah_indeks, nama_baru, berat_baru)
            except ValueError:
                print("Input berat harus berupa angka!")

        # Saat user memilih menu 6, program akan meminta indeks barang yang ingin diubah, nama baru, dan berat baru. Program akan mencari barang dengan indeks tersebut dalam stack. Jika ditemukan, informasi barang akan diperbarui dengan nama dan berat baru yang dimasukkan oleh user. Jika indeks tidak ditemukan atau input berat tidak valid, program akan memberikan pesan kesalahan yang sesuai.

        # ==================================
        # MENU 7 -> CARI BARANG
        # ==================================
        elif pilihan == "7":
            kata_kunci = input("Masukkan kata kunci pencarian: ")
            stack.cari(kata_kunci)

        # Saat user memilih menu 7, program akan meminta kata kunci untuk pencarian barang. Program akan mencari semua barang dalam stack yang nama barangnya mengandung kata kunci tersebut (pencarian case-insensitive). Jika ditemukan barang yang cocok, program akan menampilkan daftar barang tersebut beserta total berat dan kapasitas maksimum. Jika tidak ada barang yang cocok, program akan memberitahu bahwa tidak ada hasil yang ditemukan.

        # ==================================
        # MENU 0 -> KELUAR
        # ==================================
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan program.")
            print("Program selesai.")
            break

        # Saat user memilih menu 0, program akan menampilkan pesan terima kasih dan mengakhiri program dengan keluar dari loop utama.

        # ==================================
        # INPUT MENU SALAH
        # ==================================
        else:
            print("\nPilihan tidak valid!")
            print("Silakan pilih menu 0 - 7.")

        # Setelah setiap operasi, program akan kembali menampilkan menu utama untuk memungkinkan user melakukan operasi lain atau keluar dari program.


# ==========================================
# MENJALANKAN PROGRAM
# ==========================================
if __name__ == "__main__":
    main()