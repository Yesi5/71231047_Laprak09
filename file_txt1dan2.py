# # file1.txt
# with open("file1.txt", "w") as file1:
#     file1.write("Halo, ini file1.txt\n")
#     file1.write("Baris kedua dari file1\n")
#     file1.write("Ini baris ketiga\n")

# # file2.txt
# with open("file2.txt", "w") as file2:
#     file2.write("Halo, ini file2.txt\n")
#     file2.write("Baris kedua file2 yang berbeda\n")
#     file2.write("Baris ketiga sama\n")
#     file2.write("Baris keempat hanya di file2\n")

# # Membuka file1.txt dan file2.txt dalam mode baca
# with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
#     isi_file1 = file1.readlines()
#     isi_file2 = file2.readlines()

# # Membandingkan setiap baris dari kedua file
# for i, (baris1, baris2) in enumerate(zip(isi_file1, isi_file2), start=1):
#     if baris1 != baris2:
#         print(f"Baris {i}:")
#         print(f"File 1: {baris1.rstrip()}")
#         print(f"File 2: {baris2.rstrip()}")
#         print()s
#     elif len(isi_file1) < len(isi_file2) and i > len(isi_file1):
#         print(f"Baris {i}:")
#         print(f"File 2: {baris2.rstrip()}")
#         print()

# # Jika isi kedua file sama persis
# if isi_file1 == isi_file2:
#     print("Tidak ada perbedaan antara kedua file.")