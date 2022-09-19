/*
==============================
; Title: wolff-assignment6.2
; Author: Patrick Wolff
; Date: 18 September 2022
; Description: Mongosh queries used for the houses.js file
==============================
*/

// Query to show list of documents in the houses collection
db.houses.find();

// Query to show list of documents in the student's collection
db.students.find();

// Query to add document to student's collection
db.students.insertOne({ "firstName": 'Patrick', "lastName": 'Wolff', "studentId": 's1019', "houseId": 'h1009'});
// Query to show new document in student's collection
db.students.find({ "lastName": "Wolff" });

// Query to delete document
db.students.deleteOne({ "studentId": "s1019" });
// Query to show new document was deleted
db.students.find({ "studentId": "s1019" });

// Query to show list of students by house
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "student"}}]);

// Query to show a list of students for house Gryffindor 
db.houses.aggregate([
  {
    $lookup:{
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"}},
  {$match:{houseId: "h1007"}}]);

// Query to show list of students for the Eagle mascot
db.houses.aggregate([
  { $match: { houseId: "h1009" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"}}]);