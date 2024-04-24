with open("file1.txt", "w") as file1:
    file1.write("Halo, ini file1.txt\n")
    file1.write("Baris kedua dari file1\n")
    file1.write("Ini baris ketiga\n")

with open("file2.txt", "w") as file2:
    file2.write("Halo, ini file2.txt\n")
    file2.write("Baris kedua file2 yang berbeda\n")
    file2.write("Baris ketiga sama\n")
    file2.write("Baris keempat hanya di file2\n")

with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    isi_file1 = file1.readlines()
    isi_file2 = file2.readlines()

for i, (baris1, baris2) in enumerate(zip(isi_file1, isi_file2), start=1):
    if baris1 != baris2:
        print(f"Baris {i}:")
        print(f"File 1: {baris1.rstrip()}")
        print(f"File 2: {baris2.rstrip()}")
        print()

if len(isi_file1) < len(isi_file2):
    for i, baris in enumerate(isi_file2[len(isi_file1):], start=len(isi_file1)+1):
        print(f"Baris {i}:")
        print(f"File 2: {baris.rstrip()}")
        print()
elif len(isi_file2) < len(isi_file1):
    for i, baris in enumerate(isi_file1[len(isi_file2):], start=len(isi_file2)+1):
        print(f"Baris {i}:")
        print(f"File 1: {baris.rstrip()}")
        print()

if isi_file1 == isi_file2:
    print("Tidak ada perbedaan antara kedua file.")