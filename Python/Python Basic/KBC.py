questions = {
    "What is the national animal of India?": 
        ["A) Tiger", "B) Lion", "C) Elephant", "D) Leopard", "A"],

    "Who is known as the Father of the Indian Constitution?": 
        ["A) Mahatma Gandhi", "B) Jawaharlal Nehru", "C) B. R. Ambedkar", "D) Sardar Patel", "C"],

    "Which planet is known as the Red Planet?": 
        ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn", "B"],

    "What is the square root of 144?": 
        ["A) 10", "B) 11", "C) 12", "D) 13", "C"],

    "Who wrote the epic Ramayana?": 
        ["A) Tulsidas", "B) Kalidas", "C) Valmiki", "D) Ved Vyas", "C"]
}
amount=0
for question,data in questions.items():
    print(question)
    for option in data[:4]:
        print(option)
        
    answer = input("Enter Your Option: ").upper()
    
    if answer==data[4]:
        print("Your Option Is correct")
        amount = amount + 10000
        print(f"Your Current Balance Amount is {amount}")
    else:
        print("Your Option is Wrong | You Lose")
        print(f"Your Total Wining Amount is {amount}")
        break

