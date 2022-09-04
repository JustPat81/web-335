/*
==============================
; Title: wolff-assignment4.2
; Author: Patrick Wolff
; Date: 04 September 2022
; Description: Mongosh queries used for the users.js file
==============================
*/

// Query to display all of the documents in the user's collection
db.users.find( {} )

// Query to find a user by email address
db.users.find({"jbach@me.com"})