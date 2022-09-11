/*
==============================
; Title: wolff-assignment5.2
; Author: Patrick Wolff
; Date: 11 September 2022
; Description: Mongosh queries used for the users.js file
==============================
*/

// Add new user to user's collection
user = {"firstName": "John", "lastName": "Wick", "employeeId": "1013", "email": "jwick@me.com", "dateCreated": new Date()}

// Insert new user into user's collection
db.users.insertOne(user)

// Query to update email address by_id
db.users.updateOne({"_id": ObjectId("63101fc02bb0ac8a24cc6311")}, {$set: {"email": "mozart@me.com"}})

// Query to list all documents in collection showing FirstName, LastName, email
db.users.find({}, {_id: 0, "firstName": 1, "lastName": 1, "email": 1})

