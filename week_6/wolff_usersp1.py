# =============================
# Title: wolff_usersp1.py
# Author: Patrick Wolff
# Date: 18 September 2022
# Description: Connect Python to web335DB database
# =============================

# Import MongoClient
from pymongo import MongoClient

# Building connection string to connect to web335DB
client = MongoClient("mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.tq1o4.mongodb.net/web335DBretryWrites=true&w=majority")
db = client.test

# Configure variable to access the web335DB database
db = client['web335DB']

# Call the find() function to display all documents in user's collection by firstName and lastName
for user in db.users.find({}, {"firstName": 1, "lastName":1 }):
    print(user)

print()

# Call the find_one function to display user document by employeeId
print(db.users.find_one({"employeeId": "1011"}))

print()

# Call the find_one function to display user document by lastName
print(db.users.find_one({"lastName": "Mozart"}))