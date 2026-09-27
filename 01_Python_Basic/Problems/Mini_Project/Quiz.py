def Quiz():

    questions = [
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["1. Atlantic Ocean", "2. Indian Ocean", "3. Pacific Ocean", "4. Arctic Ocean"],
        "answer": "3"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["1. Alexander Graham Bell", "2. Thomas Edison", "3. Nikola Tesla", "4. James Watt"],
        "answer": "1"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["1. 6", "2. 7", "3. 8", "4. 9"],
        "answer": "3"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["1. China", "2. Japan", "3. Korea", "4. Thailand"],
        "answer": "2"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["1. Oxygen", "2. Nitrogen", "3. Carbon Dioxide", "4. Hydrogen"],
        "answer": "3"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["1. Charles Dickens", "2. William Shakespeare", "3. Mark Twain", "4. Jane Austen"],
        "answer": "2"
    },
    {
        "question": "Which is the fastest land animal?",
        "options": ["1. Lion", "2. Tiger", "3. Cheetah", "4. Horse"],
        "answer": "3"
    },
    {
        "question": "In which year did India get independence?",
        "options": ["1. 1945", "2. 1947", "3. 1950", "4. 1930"],
        "answer": "2"
    }
]
    score=0
    for que in questions:
        print(que["question"])
        for ans in que["options"]:
         print(ans)
        choice=input("Enter your choice ")
        if choice==que["answer"]:
            print("correct")
            score=score+1
        else:
            print('WORNG! correct answer is of option ',que["answer"])
    print(f"QUIZ is over your score is {score} / {len(questions)}")
Quiz()
