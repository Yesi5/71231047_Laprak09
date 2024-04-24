def load_questions(file_name):
    questions = {}
    with open(file_name, 'r') as file:
        for line in file:
            question, answer = line.strip().split("||")
            questions[question.strip()] = answer.strip()
    return questions

def main():
    file_name = "soal.txt"
    questions = load_questions(file_name)
    print("Nama file:", file_name)
    
    for question, correct_answer in questions.items():
        print(question)
        user_answer = input("Jawab: ").strip().lower()
        
        if user_answer == correct_answer.lower():
            print("Jawaban benar!")
        else:
            print("Jawaban salah!")
            print("Jawaban yang benar adalah:", correct_answer)

if __name__ == "__main__":
    main()