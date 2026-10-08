# Tugas 3 - Tabel Perkalian dan Statistik
# Loop luar: mengatur baris i dari 1 sampai n.
# Loop dalam: mengatur kolom j dari 1 sampai n.
# Akumulator total_baris: menyimpan jumlah hasil pada setiap baris.
# Akumulator total_semua: menyimpan jumlah seluruh hasil perkalian.
# Counter count_genap: menghitung banyak hasil perkalian yang genap.
# Output: menampilkan tabel, jumlah setiap baris,
#         total keseluruhan, dan banyak hasil genap.

print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

while n <= 0:
    n = int(input("n harus positif. Masukkan n: "))

total_semua = 0
count_genap = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(hasil, end=" ")

        total_baris += hasil
        total_semua += hasil

        if hasil % 2 == 0:
            count_genap += 1

    print()
    print(f"Jumlah baris {i} = {total_baris}")

print(f"Total semua = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")