def create_question_file(file_name):
    questions = [
        "1+1 =|| 2\n",
        "Bendera Indonesia? || Merah Putih\n",
        "Kota gudeg adalah: || Yogyakarta\n",
        "Komponen PC untuk penyimpanan file adalah... || harddisk\n",
        "50 *20 = || 1000\n"
    ]

    with open(file_name, 'w') as file:
        for question in questions:
            file.write(question)

if __name__ == "__main__":
    file_name = "soal.txt"
    create_question_file(file_name)
    print(f"File '{file_name}' berhasil dibuat.")
