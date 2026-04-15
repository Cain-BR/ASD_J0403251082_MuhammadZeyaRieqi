# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Muhammad Zeya Rieqi
# NIM     : J0403251082
# Kelas   : TPL B1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    with open(nama_file, 'r') as file: #Membuka file
        database_buku = {}
        for baris in file:
            kode_buku, judul, harga = baris.strip().split(',') #Memisahkan data
            database_buku[kode_buku] = {"judul": judul, "harga": int(harga)} #Memasukkan data ke dictionary
        return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul): #Inisialisasi judul
        self.judul = judul
        self.next = None

class LinkedListPromosi:
    def __init__(self): #Inisialisasi head dan tail
         self.head = None
         self.tail = None

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        new_node = Node(judul) #Membuat node baru
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        current = self.head #Memulai dari head
        num = 1
        while current is not None:
            print(f"{num}. {current.judul}") #Menampilkan judul buku
            current = current.next #Melanjutkan ke node berikutnya
            num += 1
        print("None")

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self): #Inisialisasi front dan rear
        self.front = None
        self.rear = None

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        new_node = Node(nama_pelanggan) #Membuat node baru untuk pelanggan
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        if self.front is not None:
            nama = self.front.judul #Mengambil nama pelanggan dari front
            self.front = self.front.next #Memindahkan front ke node berikutnya
            if self.front is None:
                self.rear = None #Jika antrean kosong, rear juga diatur ke None
            return nama
        return None

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """
    #Implementasikan algoritma sorting secara manual
    for i in range(1, len(list_harga)):
        key = list_harga[i]
        j = i - 1
        while j >= 0 and key < list_harga[j]:
            list_harga[j + 1] = list_harga[j] #Memindahkan elemen yang lebih besar ke kanan
            j -= 1
        list_harga[j + 1] = key #Memindahkan key ke posisi yang benar
    return list_harga

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nKatalog Buku:", data_buku)
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            pilih = input("1. Tambah Antrean\n2. Layani Pelanggan\nPilih (1/2): ") #Menambahkan opsi
            if pilih == '1':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama) #Menambah pelanggan ke antrean
            elif pilih == '2':
                nama = antrean_toko.layani_pelanggan() #Melayani pelanggan dari antrean
                if nama:
                    print(f"Melayani pelanggan: {nama}")
                else:
                    print("Tidak ada pelanggan dalam antrean.")

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()