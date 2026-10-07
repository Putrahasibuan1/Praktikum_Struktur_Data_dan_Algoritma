# 1. Membuat SinglyLinkedList kosong
#
# SinglyLinkedList digunakan untuk menyimpan data dalam
# bentuk node yang saling terhubung.
#
# Setiap node memiliki:
# - data : menyimpan nilai
# - next : menunjuk ke node berikutnya

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


# =====================================================
# 2. Menambahkan data menggunakan append()
# =====================================================

# Fungsi append() digunakan untuk menambahkan data
# pada bagian akhir linked list.

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node


# =====================================================
# 3. Menambahkan data menggunakan insert_beginning()
# =====================================================

# Fungsi insert_beginning() digunakan untuk menambahkan
# data pada bagian awal linked list.

    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node


# =====================================================
# 4. Menyisipkan data setelah nilai tertentu
# =====================================================

# Fungsi insert_after() digunakan untuk menyisipkan data
# setelah node yang memiliki nilai tertentu.

    def insert_after(self, target, data):
        current = self.head

        while current is not None:
            if current.data == target:
                new_node = Node(data)

                new_node.next = current.next
                current.next = new_node

                return

            current = current.next


# =====================================================
# 5. Menampilkan linked list
# =====================================================

# Fungsi display() digunakan untuk menampilkan seluruh
# data yang terdapat di dalam linked list.

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# =====================================================
# 6. Mencari data
# =====================================================

# Fungsi search() digunakan untuk mencari nilai tertentu
# di dalam linked list.
#
# Jika data ditemukan, fungsi mengembalikan True.
# Jika data tidak ditemukan, fungsi mengembalikan False.

    def search(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False


# =====================================================
# 7. Dry run pencarian nilai 45
# =====================================================

# Dry run digunakan untuk melihat proses pencarian
# menggunakan current dan position.

    def search_dry_run(self, data):
        current = self.head
        position = 0

        while current is not None:

            print(
                "Position:", position,
                "| Current:", current.data
            )

            if current.data == data:
                print("Data", data, "ditemukan!")
                return

            current = current.next
            position += 1

        print("Data", data, "tidak ditemukan!")

# PROGRAM UTAMA

# 1. Membuat SinglyLinkedList kosong
linked_list = SinglyLinkedList()


# 2. Menambahkan data 15, 25, 35, 45 menggunakan append()
linked_list.append(15)
linked_list.append(25)
linked_list.append(35)
linked_list.append(45)


# 3. Menambahkan 5 menggunakan insert_beginning()
linked_list.insert_beginning(5)


# 4. Menyisipkan 30 setelah nilai 25
linked_list.insert_after(25, 30)


# 5. Menampilkan linked list
print("Isi Linked List:")
linked_list.display()


# 6. Mencari nilai 30 dan 99
print("\nHasil Pencarian:")
print("30:", linked_list.search(30))
print("99:", linked_list.search(99))


# 7. Dry run pencarian nilai 45
print("\nDry Run pencarian nilai 45:")
linked_list.search_dry_run(45)


# 8. Kompleksitas search adalah O(n)
#
# Search memiliki kompleksitas O(n) karena data dicari
# dengan memeriksa node satu per satu mulai dari node pertama.
#
# Jika data berada di node terakhir atau tidak ditemukan,
# seluruh node harus diperiksa.
#
# Semakin banyak jumlah node, semakin banyak pula
# pemeriksaan yang harus dilakukan.
#
# Oleh karena itu, kompleksitas waktu search adalah O(n).

print("\nKompleksitas search adalah O(n)")
print("Setiap node diperiksa satu per satu.")