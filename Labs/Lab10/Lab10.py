#Start Code, ripped and modified from files provided by Stephen Chiong

import pymongo
import json

db = dbconnection["MyDB_100336212"]
dbcollection = db["MyFriends_100336212"]
#end of ripped code

#Menu Consts
ADD_DOC = 1
DISPLAY_DOCS = 2
EXIT = 3

def menuDisp():
    print('MongoDB Manager')
    print('1) Add a Document to the Collection')
    print('2) Display your Documents')
    print('3) Exit')

def menuLogic():
    userInp = 0
    while userInp != EXIT:
        menuDisp()
        try:
            userInp = int(input('Enter your choice: '))
        except:
            print("This is an invalid integer")

        # Perform the selected action.
        if userInp == ADD_DOC:
            addDoc()
        elif userInp == DISPLAY_DOCS:
            dumpContents()
        elif userInp == EXIT:
            print("Quitting program")
        else:
            print('Invalid Integer')

def importJSON():
    with open('Mydata.json') as file:
        data = json.load(file)
    for i in range(len(data)):
        dbContents = list(dbcollection.find({"id" : data[i]["id"]}))
        if len(dbContents) == 0:
            dbcollection.insert_one(data[i])

def dumpContents():
    dbContents = dbcollection.find({})
    print('{:7s}{:20s}{:20s}{:40s}'.format("ID", "First Name", "Last Name", "Cars"),end='')
    print("\n")
    for doc in dbContents:
        print('{:<7d}{:20s}{:20s}'.format(doc["id"], doc["first_name"], doc["last_name"]),end='')
        cars = 0
        for j in doc["cars"]:
            if cars == len(doc["cars"]) -1:
                print(j["make"], end='\n')
            else:
                print(j["make"], end=", ")
                cars += 1
    print("")

def getHighestID():
    dbContents = list(dbcollection.find({}))
    highest = dbContents[0]["id"]
    for i in dbContents:
        if dbContents[i]["id"] > highest:
            highest = dbContents[i]["id"]
    return highest

def addDoc():
    newID = getHighestID() + 1
    fName = str(input("What is your first name?"))
    lName = str(input("What is your last name?"))
    carArr = [None] #use loop to get makes
    #db.insert_one()


def main():
    importJSON() #imports initial JSON file
    menuLogic()
    print("=======================")

if __name__ == '__main__':
    main()
