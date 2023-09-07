import json

def select_contact(x):

    file = open("11_log_book.json", "r")
    cont = json.load(file)

    for i in range(0, len(cont)):
        if(cont[i]['name']==x):
            result = cont[i]['name'] + "\t" + cont[i]['number'] + "\t" + cont[i]['address']
            break
        else:
            result= "This Contact doesn't exist in contacts. "

    print(result)

    file.close()

x = input("Enter contact name you want to search: ")
select_contact(x)