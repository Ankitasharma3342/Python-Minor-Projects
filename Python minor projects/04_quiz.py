print("Welcome to the Quiz Competition !")
print("Note: if your answer is wrong you will  be out of the quiz!")

question_no = 0
playing = input("Do you want to play? y/n    ").lower()
if (playing== "y"):
    question_no += 1
    ques= input( str(question_no) + " Who invented the Computer? ")
    if(ques== "Charles Babbage"):
        print("Correct answer")
    else:
        print("Incorrect")
        

    question_no += 1
    ques= input( str(question_no) + " Who invented the Python ?  ")
    if(ques== "Guido Van Rossum"):
        print("Correct answer")
    else:
        print("Incorrect")
        
        
    question_no += 1
    ques= input( str(question_no) + " In which year python is invented ? ")
    if(ques== "1991"):
        print("Correct answer")
    else:
        print("Incorrect")
        
    
else: 
    print("You are not a part of quiz compition. ")
