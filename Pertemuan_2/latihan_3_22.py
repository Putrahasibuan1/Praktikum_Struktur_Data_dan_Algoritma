# 1. Membuat class Kotak (pengganti class Node)
class Kotak:

  def __init__(self, data):
    self.data = data
    self.next = None


# 2. Membuat tiga node/kotak berisi 100, 200, dan 300
node1 = Kotak(100)
node2 = Kotak(200)
node3 = Kotak(300)

# 3. Menghubungkan node pertama ke kedua, lalu kedua ke ketiga
node1.next = node2
node2.next = node3

# 4. Menampilkan data dengan menelusuri dari node pertama
print("Penelusuran awal:")
current = node1
while current:
  print(current.data)
  current = current.next

# 6. Mengubah next node pertama agar langsung menunjuk ke node ketiga
node1.next = node3

print("\nPenelusuran setelah pemotongan jalur:")
current = node1
while current:
  print(current.data)
  current = current.next