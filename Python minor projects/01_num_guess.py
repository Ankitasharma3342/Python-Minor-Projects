
def num(x):
    savepoint= 50
    if(int(x)==savepoint):
        return True
    else:
        return False

for i in range(0,5):

    a= input("Enter your guessed Number: ")

   
    if(num(a)== True):
         print("Congratulations! you guess the right number.  ")
         break
    else:
        print("Your guessed number is wrong. Try Again. ")
