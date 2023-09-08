input1= int(input("Enter your first number :  "))
inp=input("Enter the action you want to perform :  ")
input2= int(input("Enter your second number :  "))


if(inp=="+"):
    print(input1+input2)
elif(inp=="_"):
    print(input1-input2)  
elif(inp=="*"):
    print(input1*input2)  
elif(inp=="/"):
    print(input1/input2)          
elif(inp=="%"):
    print(input1%input2) 
elif(inp=="^"):
    print(input1**input2) 

else:
    print("Cannot calculated")          
