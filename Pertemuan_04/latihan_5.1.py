from collections import deque

class Queue:
    def __init__(self):
        # Menginisialisasi deque kosong untuk menyimpan elemen queue
        self.items = deque()
        
    def enqueue(self, item):
        # Menambahkan elemen ke bagian belakang (tail) queue
        self.items.append(item)
        
    def dequeue(self):
        # Menghapus dan mengembalikan elemen dari depan (front) queue
        if not self.is_empty():
            return self.items.popleft()
        return "Queue kosong (Underflow)"
        
    def peek(self):
        # Melihat elemen terdepan tanpa menghapusnya
        if not self.is_empty():
            return self.items[0]
        return "Queue kosong"
        
    def size(self):
        # Mengembalikan jumlah elemen dalam queue
        return len(self.items)
        
    def is_empty(self):
        # Mengecek apakah queue kosong
        return len(self.items) == 0

# --- Menjalankan Praktik Mandiri 5.1 ---

print("=== 1. & 2. Inisialisasi Queue dan Memasukkan Data ===" )
q = Queue()
data_to_enqueue = [10, 20, 30, 40, 50]
for d in data_to_enqueue:
    q.enqueue(d)
print(f"Data yang dimasukkan: {data_to_enqueue}")

print("\n=== 3. Menampilkan Front dan Size ===")
print(f"Front (Elemen terdepan): {q.peek()}")
print(f"Size (Ukuran queue): {q.size()}")

print("\n=== 4. Melakukan Dequeue Dua Kali ===")
out1 = q.dequeue()
out2 = q.dequeue()
print(f"Keluar ke-1: {out1}")
print(f"Keluar ke-2: {out2}")
print(f"Queue setelah 2x dequeue: list(q.items) -> {list(q.items)}")

print("\n=== 5. Menambahkan 60 dan 70 ===")
q.enqueue(60)
q.enqueue(70)
print(f"Setelah enqueue 60 dan 70: list(q.items) -> {list(q.items)}")

print("\n=== 6. Mengeluarkan Seluruh Elemen dengan Loop Sampai Kosong ===")
print("Elemen yang keluar secara berurutan:")
while not q.is_empty():
    print(q.dequeue(), end=" ")
print()

print("\n=== 7. Uji Dequeue dan Peek Ketika Queue Kosong ===")
print(f"Hasil peek() saat kosong: {q.peek()}")
print(f"Hasil dequeue() saat kosong: {q.dequeue()}")