# ================================================
# Title: wolff_usersp2.py
# Author: Patrick Wolff
# Date: 18 September 2022
# Description: Connect Python to web335DB database
#              & use Python with MondoDB.
# ================================================

# Import MongoClient
from pymongo import MongoClient
import datetime

# Building connection string to connect to web335DB
client = MongoClient("mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.tq1o4.mongodb.net/web335DBretryWrites=true&w=majority")
db = client.test

# Configure variable to access the web335DB database
db = client['web335DB']

# Create new user document and add to users collection
hayden = {
    "firstName": "Joseph",
    "lastName": "Hayden",
    "employeeId": "1014",
    "email": "jhayden@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert document into the users collection
hayden_user_id = db.users.insert_one(hayden).inserted_id
print(hayden_user_id)

# Search to prove new document was inserted into users collection
print(db.users.find_one({"employeeId": "1014"}))

# Create an update query to change a user's email address
db.users.update_one(
    {"employeeId": "1014"},
    {
        "$set": {
            "email": "joseph.hayden@me.com"
        }
    }
)

# Search to prove update worked by searching the collection for the user by employeeId
print(db.users.find_one({"employeeId": "1014"}))

# Create query to remove a user document
result = db.users.delete_one({
    "employeeId": "1014"
})

# Display the results of the query
print(result)

# Query to prove the removal of document
#print(db.users.find_one({"employeeId": "1014"}))