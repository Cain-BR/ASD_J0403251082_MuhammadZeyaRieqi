#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Studi Kasus: Sistem Antrian Layanan Akademis
#Implementasi Queue =>
#Enqueue: memindahkan pointer rear (nambah data baru dari belakang)
#Dequeue: memindahkan pointer front (menghapus data dari depan)
#Front -> A-> B > C ->Rear

#1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim
        self.nama = nama
        self.next = None

#2) Mendefinisikan queue, terdiri dari front dan rear
class queueakademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self,nim,nama):
        nodebaru = Node(nim,nama)
        if self.is_empty():
            self.front = nodebaru
            self.rear = nodebaru
        else:
            self.rear.next = nodebaru
            self.rear = nodebaru

    def dequeue(self):
        if self.front is None:
            print("Antrian kosong")
            return None
        nim_terdepan = self.front.nim
        nama_terdepan = self.front.nama
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Data yang didequeue: NIM {nim_terdepan}, Nama {nama_terdepan}")
        return (nim_terdepan, nama_terdepan)
    
    def tampilkan(self):
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. NIM: {current.nim}, Nama: {current.nama}")
            current = current.next
            no += 1

#Program utama
q = queueakademik()
def main():
    while True:
        print("Sistem Antrian Akademik")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ").strip()
        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()
            q.enqueue(nim,nama)
            print("Mahasiswa berhasil ditambahkan ke antrian")
        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani:
                print(f"Mahasiswa dilayani: {dilayani[0]} - {dilayani[1]}")
        elif pilihan == "3":
            q.tampilkan()
        elif pilihan == "4":
            break

if __name__ == "__main__":
    main()