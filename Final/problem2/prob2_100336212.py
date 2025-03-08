import pymongo
import json

dbconnection = pymongo.MongoClient("mongodb+srv://NoahJ:EwYTva12oS@cluster0.4kwrg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = dbconnection["sample_airbnb"]
dbcollection = db["listingsAndReviews"]

