# =====================================================
# 1. Membuat Node dan SinglyLinkedList
# =====================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


    # =================================================
    # Fungsi append()
    # =================================================

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node


    # =================================================
    # Fungsi insert_beginning()
    # =================================================

    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node


    # =================================================
    # Fungsi insert_after()
    # =================================================

    def insert_after(self, target, data):
        current = self.head

        while current is not None:
            if current.data == target:
                new_node = Node(data)

                new_node.next = current.next
                current.next = new_node

                return

            current = current.next


    # =================================================
    # Fungsi display()
    # =================================================

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


    # =================================================
    # Fungsi count()
    # =================================================

    # Fungsi count() digunakan untuk menghitung jumlah
    # node yang terdapat di dalam linked list.

    def count(self):
        current = self.head
        jumlah = 0

        while current is not None:
            jumlah += 1
            current = current.next

        return jumlah


    # =================================================
    # Fungsi delete()
    # =================================================

    # Fungsi delete() digunakan untuk menghapus node
    # berdasarkan nilai yang diberikan.

    def delete(self, data):

        # Jika list kosong
        if self.head is None:
            print("List kosong, tidak ada data yang dihapus.")
            return

        # Jika node yang ingin dihapus adalah head
        if self.head.data == data:
            self.head = self.head.next
            print("Data", data, "berhasil dihapus.")
            return

        # Mencari node yang akan dihapus
        current = self.head
        previous = None

        while current is not None:

            if current.data == data:
                previous.next = current.next
                print("Data", data, "berhasil dihapus.")
                return

            previous = current
            current = current.next

        # Jika data tidak ditemukan
        print("Data", data, "tidak ditemukan.")


# =====================================================
# 1. Uji delete pada list kosong
# =====================================================

print("1. DELETE PADA LIST KOSONG")

list_kosong = SinglyLinkedList()

list_kosong.delete(5)

print("Isi list:")
list_kosong.display()

print("Jumlah node:", list_kosong.count())


# =====================================================
# 2. List hanya berisi satu node
# =====================================================

print("\n2. DELETE LIST DENGAN SATU NODE")

list_satu = SinglyLinkedList()

# Menggunakan data yang sudah ada
list_satu.append(45)

print("Sebelum dihapus:")
list_satu.display()
print("Jumlah node:", list_satu.count())

list_satu.delete(45)

print("Setelah dihapus:")
list_satu.display()
print("Jumlah node:", list_satu.count())


# =====================================================
# 3. Menghapus head, node tengah, dan node terakhir
# =====================================================

print("\n3. DELETE HEAD, NODE TENGAH, DAN NODE TERAKHIR")

linked_list = SinglyLinkedList()

# Menggunakan data yang sudah ada
linked_list.append(5)
linked_list.append(15)
linked_list.append(25)
linked_list.append(30)
linked_list.append(35)
linked_list.append(45)

print("\nList awal:")
linked_list.display()
print("Jumlah node:", linked_list.count())


# Menghapus head
print("\nMenghapus head (5):")
linked_list.delete(5)

linked_list.display()
print("Jumlah node:", linked_list.count())


# Menghapus node tengah
print("\nMenghapus node tengah (30):")
linked_list.delete(30)

linked_list.display()
print("Jumlah node:", linked_list.count())


# Menghapus node terakhir
print("\nMenghapus node terakhir (45):")
linked_list.delete(45)

linked_list.display()
print("Jumlah node:", linked_list.count())


# =====================================================
# 4. Menghapus nilai yang tidak ada
# =====================================================

print("\n4. MENGHAPUS DATA YANG TIDAK ADA")

# Nilai 99 belum pernah digunakan pada list
linked_list.delete(99)

print("Isi list:")
linked_list.display()

print("Jumlah node:", linked_list.count())


# =====================================================
# 5. Menampilkan list dan jumlah node
# =====================================================

# Setelah setiap operasi delete, program menampilkan
# isi linked list dan jumlah node.
#
# Hal ini digunakan untuk memastikan bahwa proses delete
# berjalan dengan benar dan jumlah node ikut berubah.


# =====================================================
# 6. Peran previous saat menghapus node bukan head
# =====================================================

# previous digunakan untuk menyimpan node yang berada
# tepat sebelum node yang akan dihapus.
#
# Contohnya:
#
# 15 -> 25 -> 35
#
# Jika ingin menghapus 25:
#
# previous = 15
# current  = 25
#
# Maka:
#
# previous.next = current.next
#
# Hasilnya menjadi:
#
# 15 -> 35
#
# Node 25 dilewati sehingga tidak lagi terhubung
# dengan linked list.


# =====================================================
# 7. Pengujian tambahan
# =====================================================

print("\n7. PENGUJIAN TAMBAHAN")

# Pengujian tambahan:
# Menghapus data yang sama dua kali.

print("\nMenghapus 35:")
linked_list.delete(35)

print("Isi list:")
linked_list.display()
print("Jumlah node:", linked_list.count())


print("\nMencoba menghapus 35 lagi:")
linked_list.delete(35)

print("Isi list:")
linked_list.display()
print("Jumlah node:", linked_list.count())