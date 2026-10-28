class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            print(f"  -> [Overflow] Gagal enqueue '{item}': Queue penuh!")
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.count += 1
        print(f"  -> Enqueue '{item}' berhasil.")
        self.status()
        return True

    def dequeue(self):
        if self.is_empty():
            print("  -> [Underflow] Gagal dequeue: Queue kosong!")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None  # Kosongkan slot secara visual
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"  -> Dequeue berhasil. Keluar: '{item}'")
        self.status()
        return item

    def status(self):
        print(f"     [Status] Items: {self.queue} | front: {self.front} | rear: {self.rear} | count: {self.count}")


# --- Menjalankan Praktik Mandiri 5.2 ---

print("=== 1. Buat CircularQueue dengan kapasitas 4 ===")
cq = CircularQueue(4)
cq.status()

print("\n=== 2. Enqueue A, B, C, D dan Cek Kondisi Penuh ===")
for item in ['A', 'B', 'C', 'D']:
    cq.enqueue(item)
print(f"Apakah queue penuh? {cq.is_full()}")

print("\n=== 3. Coba Enqueue E Ketika Penuh ===")
cq.enqueue('E')

print("\n=== 4. Dequeue Dua Elemen ===")
cq.dequeue()
cq.dequeue()

print("\n=== 5. Enqueue E dan F (Wrap-around) ===")
cq.enqueue('E')
cq.enqueue('F')

print("\n=== 6. Status Akhir Items, Front, Rear, dan Count ===")
cq.status()