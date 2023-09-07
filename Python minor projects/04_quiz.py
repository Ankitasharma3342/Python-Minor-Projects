# print("Welcome to the Quiz Competition !")
# print("Note: if your answer is wrong you will  be out of the quiz!")

# question_no = 0
# playing = input("Do you want to play? y/n").lower()
# if (playing== "y"):
#     question_no += 1
#     ques= input( str(question_no) + "Who invented the Computer? ")
#     if(ques== "Charles Babbage"):
#         print("Correct answer")
#     else:
#         print("Incorrect")
        

#     question_no += 1
#     ques= input( str(question_no) + "Who invented the Python ?  ")
#     if(ques== "Guido Van Rossum"):
#         print("Correct answer")
#     else:
#         print("Incorrect")
        
        
#     question_no += 1
#     ques= input( str(question_no) + "In which year python is invented ? ")
#     if(ques== "1991"):
#         print("Correct answer")
#     else:
#         print("Incorrect")
        
    
# else: 
#     print("You are not a part of quiz compition. ")

print("Welcome to the Quiz Competition!")
print("Note: If your answer is wrong, you will be out of the quiz!")

question_no = 0
score = 0

questions = [
    {"question": "Who invented the Computer?", "answer": "Charles Babbage"},
    {"question": "Who invented Python?", "answer": "Guido Van Rossum"},
    {"question": "In which year was Python invented?", "answer": "1991"}
]

playing = input("Do you want to play? (y/n)").lower()

if playing == "y":
    for question in questions:
        question_no += 1
        ques = input(f"{question_no}. {question['question']} ")
        if ques.lower() == question['answer'].lower():
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect! You are out of the quiz.")
            break

    print(f"Your score is {score}/{len(questions)}.")
else:
    print("You are not a part of the quiz competition.")
