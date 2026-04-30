import time
import random

# Fungsi A: Nested Loop (O(n²))
def find_duplicates_nested_loop(lst):
    duplicates = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates
# 1. Fungsi manual_delete
def manual_delete(arr, index):
    # Validasi indeks
    if index < 0 or index >= len(arr):
        return arr  # Kembalikan array asli jika indeks tidak valid
    
    # Geser elemen kanan ke kiri untuk mengisi kekosongan
    shift_count = 0
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
        shift_count += 1
    
    # Potong elemen terakhir yang sudah terduplikasi
    new_arr = arr[:-1]
    return new_arr, shift_count  # Kembalikan array baru dan jumlah pergeseran


# 2. Fungsi string_reversal
def string_reversal(kalimat):
    reversed_str = ""
    # Iterasi dari akhir ke awal string
    for i in range(len(kalimat) - 1, -1, -1):
        reversed_str += kalimat[i]
    return reversed_str


# Contoh Pengujian
if __name__ == "__main__":
    # Uji manual_delete
    arr1 = [10, 20, 30, 40, 50]
    print("Array Awal:", arr1)
    
    # Hapus elemen pertama (index 0)
    new_arr_first, shift_first = manual_delete(arr1.copy(), 0)
    print("Setelah hapus index 0:", new_arr_first, "| Pergeseran:", shift_first)
    
    # Hapus elemen terakhir (index 4 pada array awal)
    new_arr_last, shift_last = manual_delete(arr1.copy(), 4)
    print("Setelah hapus index 4:", new_arr_last, "| Pergeseran:", shift_last)
    
    # Uji string_reversal
    kalimat = "Halo Dunia"
    print("\nKalimat Awal:", kalimat)
    print("Kalimat Terbalik:", string_reversal(kalimat))