#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Tugas Hands-On: Sistem Antrian Bengkel Motor

class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None

class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, no, nama, servis):
        nodebaru = Node(no, nama, servis)
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
        no_terdepan = self.front.no
        nama_terdepan = self.front.nama
        servis_terdepan = self.front.servis
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Data yang didequeue: No {no_terdepan}, Nama {nama_terdepan}, Servis {servis_terdepan}")
        return (no_terdepan, nama_terdepan, servis_terdepan)
    
    def tampilkan(self):
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. No: {current.no}, Nama: {current.nama}, Servis: {current.servis}")
            current = current.next
            no += 1

def main():
    q = QueueBengkel()
    while True:
        print("Sistem Antrian Bengkel Motor")
        print("1. Tambah Antrian")
        print("2. Layani Antrian")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            no = input("Masukkan nomor antrian: ")
            nama = input("Masukkan nama pelanggan: ")
            servis = input("Masukkan jenis servis: ")
            q.enqueue(no, nama, servis)
        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani:
                print(f"Pelangan dilayani: No {dilayani[0]} - {dilayani[1]} - {dilayani[2]}")
        elif pilihan == "3":
            q.tampilkan()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem antrian bengkel motor.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()