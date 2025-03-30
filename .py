import random
#animal quiz 1
def animal_quiz1():
    questions = [
        {
            "question": "What is the fastest land animal?",
            "options": ["A. Cheetah", "B. Lion", "C. Horse", "D. Falcon"],
            "answer": "A"
        },
        {
            "question": "Which animal is known as the King of the Jungle?",
            "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Gorilla"],
            "answer": "C"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippo"],
            "answer": "B"
        },
        {
            "question": "Which animal can change its color to blend in with its surroundings?",
            "options": ["A. Chameleon", "B. Octopus", "C. Cuttlefish", "D. All of the above"],
            "answer": "D"
        },
        {
            "question": "Which bird is known for its ability to mimic human speech?",
            "options": ["A. Crow", "B. Parrot", "C. Owl", "D. Eagle"],
            "answer": "B"
        }
    ]
    
    score = 0
    random.shuffle(questions)  # Shuffle the questions for randomness
    
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["answer"]:
            print("Correct! 🎉\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    
    print(f"Quiz finished! Your final score is {score}/{len(questions)}.")
    if score == len(questions):
        print("Amazing! You are an animal expert! 🏆")
    elif score >= len(questions) // 2:
        print("Good job! You know a lot about animals! 🦁")
    else:
        print("Keep learning! You'll get better next time! 📚")

#running the quiz
animal_quiz1()
