Tugas Praktikum Minggu 3: Operasi Manual pada Array dan String
 
Fungsi yang Dibuat
 
1.  manual_delete(arr, index) 
 
- Fungsi: Menghapus elemen pada indeks tertentu dengan menggeser elemen kanan ke kiri, tanpa menggunakan  .pop()  atau  del .

- Contoh:
Input  [10,20,30,40,50]  dengan index 0 → Output  [20,30,40,50]  (4 pergeseran).
Input  [10,20,30,40,50]  dengan index 4 → Output  [10,20,30,40]  (0 pergeseran).

- Kompleksitas Waktu:

- Jika menghapus elemen pertama (index 0): O(n) (perlu menggeser  n-1  elemen, dengan  n  adalah panjang array).

- Jika menghapus elemen terakhir (index  n-1 ): O(1) (tidak ada pergeseran yang diperlukan).

- Analisis Pergeseran:
Jumlah operasi pergeseran sama dengan  n - 1 - index . Untuk elemen pertama, pergeseran =  n-1 ; untuk elemen terakhir, pergeseran = 0.
 
2.  string_reversal(kalimat) 
 
- Fungsi: Membalikkan kalimat secara manual tanpa menggunakan  [::-1]  atau  .reverse() .

- Contoh:
Input  "Halo Dunia"  → Output  "ainuD olaH" .

- Kompleksitas Waktu: O(n) (iterasi sebanyak  n  karakter dalam string, dengan  n  adalah panjang kalimat).
