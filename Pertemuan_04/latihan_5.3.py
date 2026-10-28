from collections import deque
import string

def is_palindrome(text):
    # 3. Normalisasi: Ubah ke lowercase dan hapus spasi serta tanda baca
    normalized = ''.join(char.lower() for char in text if char.isalnum())
    
    # Masukkan karakter ke dalam deque
    d = deque(normalized)
    
    print(f"\n--- Pengujian Kata/Kalimat: '{text}' (Normal: '{normalized}') ---")
    
    match = True
    iteration = 1
    
    # Melakukan perbandingan dari kedua ujung secara bersamaan
    while len(d) > 1:
        left = d.popleft()   # Ambil dari depan (kiri)
        right = d.pop()      # Ambil dari belakang (kanan)
        
        # 5. Menampilkan pasangan kiri-kanan pada setiap iterasi
        print(f"  Iterasi {iteration}: Bandingkan kiri '{left}' dengan kanan '{right}'")
        
        if left != right:
            match = False
            break
        iteration += 1
        
    return match

# --- 2. Uji kata: level, katak, radar, python, algoritma ---
kata_list = ["level", "katak", "radar", "python", "algoritma"]
print("=== 2. Pengujian Kata ===")
for kata in kata_list:
    hasil = is_palindrome(kata)
    print(f"Hasil '{kata}' adalah Palindrome? {hasil}\n")

# --- 3. Uji kalimat yang mengandung spasi atau tanda baca setelah normalisasi ---
kalimat_list = [
    "Kasur ini rusak",
    "A nut for a jar of tuna",
    "Bukan palindrom loh!"
]
print("=== 3. Pengujian Kalimat dengan Spasi/Tanda Baca ===")
for kalimat in kalimat_list:
    hasil = is_palindrome(kalimat)
    print(f"Hasil '{kalimat}' adalah Palindrome? {hasil}\n")