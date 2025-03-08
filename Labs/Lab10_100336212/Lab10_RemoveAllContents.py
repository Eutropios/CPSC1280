import pymongo
import json

dbconnection = pymongo.MongoClient("mongodb+srv://NoahJ:EwYTva12oS@cluster0.4kwrg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = dbconnection["MyDB_100336212"]
dbcollection = db["MyFriends_100336212"]

def main():
    itemsDeleted = dbcollection.delete_many({})
    print(f"{itemsDeleted.deleted_count} items deleted")
    
    
if __name__ == '__main__':
    main()