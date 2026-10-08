# Pertemuan 06 Nested Loop Python
Nama: Aulia Rahma Ramadhani
NIM: 2225250001
Kelas: 3A

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan dalam program Python.

## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
1. Baca dan validasi nilai n.
2. Set total_semua = 0 dan count_genap = 0.
3. Ulangi i dari 1 sampai n.
4. Set total_baris = 0 untuk setiap baris.
5. Ulangi j dari 1 sampai n.
6. Hitung hasil = i * j.
7. Tambahkan hasil ke total_baris dan total_semua.
8. Jika hasil genap, tambahkan count_genap.
9. Setelah loop dalam selesai, tampilkan total_baris.
10. Setelah loop luar selesai, tampilkan total_semua dan count_genap.


## Hasil Pengujian

| Input | Hasil yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| n = 1 | Total seluruh hasil = 1, banyak hasil genap = 0 | Total seluruh hasil = 1, banyak hasil genap = 0 | Lulus |
| n = 2 | Total seluruh hasil = 9, banyak hasil genap = 3 | Total seluruh hasil = 9, banyak hasil genap = 3 | Lulus |
| n = 3 | Total seluruh hasil = 36, banyak hasil genap = 5 | Total seluruh hasil = 36, banyak hasil genap = 5 | Lulus |
| n = 0 | Meminta input kembali | Meminta input kembali | Lulus |

## Analisis Efisiensi

Untuk input n, loop luar berjalan sebanyak n kali dan loop dalam juga berjalan sebanyak n kali.

Jumlah pasangan yang diproses adalah:
n × n = n²

Sehingga jumlah iterasi nested loop bertambah secara kuadrat terhadap nilai n.

## Refleksi

Salah satu kesalahan yang dapat terjadi pada nested loop adalah kesalahan indentasi. Kesalahan indentasi dapat menyebabkan perintah berada pada loop yang salah sehingga hasil program tidak sesuai.

Perbaikannya adalah memastikan loop luar, loop dalam, kondisi, akumulator, counter, dan output memiliki indentasi yang sesuai.

## Refleksi Teknis

1. `total_baris` direset di setiap iterasi loop luar karena variabel tersebut digunakan untuk menghitung jumlah pada satu baris saja.
2. `total_semua` tidak direset di setiap baris karena digunakan untuk menghitung jumlah seluruh hasil perkalian dari semua baris.
3. Untuk input n, pernyataan `hasil = i * j` dieksekusi sebanyak n² kali karena terdapat n iterasi pada loop luar dan n iterasi pada loop dalam.
4. `count_genap` dapat dibuktikan benar dengan menghitung setiap hasil yang memenuhi kondisi `hasil % 2 == 0`. Untuk n = 3, terdapat 5 hasil genap.
5. Bagian yang paling banyak melakukan operasi ketika n membesar adalah nested loop karena jumlah iterasinya bertambah menjadi n².