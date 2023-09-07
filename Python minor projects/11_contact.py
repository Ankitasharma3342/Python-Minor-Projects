import json


def add_con():

    file= open("11_log_book.json" , "r")
    cont = list(json.load(file))

    cont_name = input("Enter contact name : ")
    cont_num = input("Enter contact number : ")
    cont_addr = input("Enter contact address : ")

    temp = {"name" : cont_name,
    "number" : cont_num,
    "address" : cont_addr}

    cont.append(temp)

    writefile = open("11_log_book.json" , "w")
    writefile.write(json.dumps(cont))


def show_con():

    file = open("11_log_book.json", "r")
    cont = json.load(file)

    for i in range(0, len(cont)):
        print(cont[i]['name'] + "\t" + cont[i]['number'] + "\t" + cont[i]['address'])

        file.close()

while 0==0:
        print(''' Select your choice:
        1. Add Contact
        2. Show Contact
        3. Exit ''')

        requ = int(input("Enter Your Choice :  "))

        if requ == 1:

            add_con()
        elif requ == 2:
            
            show_con()
        elif requ == 3:
            exit(0)
        else:
            print(" Enter a valid choice...   ")