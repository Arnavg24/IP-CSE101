f = open("./q7.txt", "r")

addrbook=eval(f.read())

f.close()

def printRecord(record):

    print(f"Name: {record['name']}")
    print(f"Phone: {record['phone']}")
    print(f"Address: {record['address']}")
    print(f"Email: {record['email']}")
    print()

while(True):
    print("1. Insert a new entry")
    print("2. Delete an entry")
    print("3. Find all entries with partial name")
    print("4. Find entry by phone number or email")
    print("5. Exit")

    choice=int(input())

    if(choice==5):
        w=open("./q7.txt", "w+")
        w.write(str(addrbook))
        break
    elif(choice==1):
        person_dict={}
        name=input("Enter name: ")
        address=input("Address: ")
        phone=input("Phone: ")
        email=input("Email: ")
        person_dict['address']=address
        person_dict['phone']=phone
        person_dict['email']=email
        if(name in addrbook):
            addrbook[name].append(person_dict)
        else:
            addrbook[name]=[person_dict]
    elif(choice==2):
        name=input("Enter name that you want to delete: ")
        if(name in addrbook):
            if(len(addrbook[name])>1):
                phone=input("Phone number of the person: ")
                for i in range(len(addrbook[name])):
                    if(addrbook[name][i]['phone']==phone):
                        print("The record has been deleted.")
                        del addrbook[name][i]
                        break
                    else:
                        print("Phone number not found")
            else:
                del addrbook[name]
        else:
            print("Name not found in address book")
    elif(choice==3):
        partial_name=input("Enter partial name: ")
        search=[]
        for record in addrbook:
            if(partial_name in record):
                for person in addrbook[record]:
                    temp_dict=person
                    temp_dict['name']=record
                    search.append(temp_dict)
        for i in range(len(search)):
            print("Record {i}")
            printRecord(search[i])
    elif(choice==4):
        print("1. Search by phone")
        print("2. Search by email")
        choice_2=int(input("Enter choice: "))
        if(choice_2==1):
            phone=input("Enter Phone to search: ")
            for record in addrbook:
                for person in addrbook[record]:
                    if(person['phone']==phone):
                        temp_dict=person
                        temp_dict['name']=record
                        print()
                        print("Found phone number")
                        print()
                        printRecord(temp_dict)
        else:
            email=input("Enter Email to search: ")
            for record in addrbook:
                for person in addrbook[record]:
                    if(person['email']==email):
                        temp_dict=person
                        temp_dict['name']=record
                        print()
                        print("Found Email")
                        print()
                        printRecord(temp_dict)