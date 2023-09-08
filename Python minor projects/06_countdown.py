import time

user_input = int(input("Enter Number of Seconds for countdown : "))

for i in range(1, user_input + 1):
    print(user_input - i +1)
    time.sleep(0.5)