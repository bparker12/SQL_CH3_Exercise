CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL UNIQUE
);

CREATE TABLE Instructor (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name   TEXT NOT NULL unique,
    last_name	TEXT NOT NULL unique,
    slack_handle	TEXT NOT NULL unique,
    speciality TEXT NOT NULL UNIQUE,
    CohortId INTEGER,
    FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Student (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name   TEXT NOT NULL unique,
    last_name	TEXT NOT NULL unique,
    slack_handle	TEXT NOT NULL unique,
    CohortId INTEGER,
    FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Exercise (
	Id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	dev_language TEXT NOT NULL ,
	name TEXT NOT NULL unique
);

CREATE TABLE Student_Exercises (
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	studentID int,
	exerciseID int,
	FOREIGN KEY(studentID) REFERENCES Student(Id),
	FOREIGN KEY(exerciseID) REFERENCES Exercise(Id)
);

INSERT INTO Cohort 
VALUES (null, "33");

INSERT INTO Cohort
VALUES (null, "34");

INSERT INTO Cohort
VALUES (null, "35");

INSERT INTO Exercise
VALUES (null, "python", "flowers");

INSERT INTO Exercise
VALUES (null, "javascript", "daily journal");

INSERT INTO Exercise
VALUES (null, "python", "arboretum");

Insert INTO Exercise
VALUES (null, "python", "sql");

INSERT INTO Exercise
VALUES (null, "javascript", "nutshell");

INSERT INTO Student
VALUES (null, "Carson", "Wentz", "WentzDay11", 1);

INSERt INTO Student
VALUES (null, "Fletcher", "Cox", "BIGMAN91", 2);

INSERT INTO Student
VALUES (null, "Miles", "Sander", "Sandin26", 3);

INSERT INTO Student
VALUES (null, "Nelson", "Angohlor", "WRQuickness", 1);

INSERT INTO Student
VALUES (null, "Zach", "Ertz", "ErtzTE", 2);

INSERT INTO Student
VALUES (null, "Jason", "Peters", "4evaEagle", 3);

INSERT INTO Student
VALUES (null, "Malcom", "Jenkins", "MalcXEagle", 1);

INSERT INTO Instructor
VALUES (null, "Joe", "Shepherd", "joeshep", "comdey", 33);

INSERT INTO Instructor
VALUES (null, "Steve", "Brownlee", "thebrownmachine", "answering questions with a question", 33);

INSERT INTO Instructor
VALUES (null, "Madison", "Peper", "peps", "calmness in all the calamity", 33);

INSERT INTO Student_Exercises
VALUES (null, 7, 3);

SELECT * FROM Student_Exercises;