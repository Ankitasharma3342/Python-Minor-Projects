import string
import random

length = input('Enter the length of password : ')
print('''Choose from these to set your password: 
1. Digits
2. Alphabets
3. Special Characters
4. Exit''')

list= ""

while True:
    choice= int(input("Enter your Choice: "))
    if(choice== 1):
        list+= string.digits
    elif(choice== 2):
        list+= string.ascii_letters
    elif(choice== 3):
        list+= string.punctuation
    elif(choice== 4):
        break
    else:
        print("Enter valid choice : ")

password= []
for i in range(int(length)):
    random_char = random.choice(list)
    password.append(random_char)

print("The Random password is: " + "".join(password))