DROP TABLE IF EXISTS Cohort;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Instructor;
DROP TABLE IF EXISTS ProgrammingLanguage;
DROP TABLE IF EXISTS Exercise;
DROP TABLE IF EXISTS StudentToExercise;

CREATE TABLE Cohort (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstName TEXT NOT NULL,
  lastName TEXT NOT NULL,
  slack TEXT UNIQUE,
  cohortId INTEGER,
  FOREIGN KEY (cohortId) REFERENCES Cohort(id)
);

CREATE TABLE Instructor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstName TEXT NOT NULL,
  lastName TEXT NOT NULL,
  cohortId INTEGER,
  slack TEXT UNIQUE,
  specialty TEXT,
  FOREIGN KEY (cohortId) REFERENCES Cohort(id)
);

CREATE TABLE ProgrammingLanguage (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE Exercise (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  languageId INTEGER,
  FOREIGN KEY (languageId) REFERENCES ProgrammingLanguage(id)
);

CREATE TABLE StudentToExercise (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  studentId INTEGER,
  exerciseId INTEGER,
  FOREIGN KEY (studentId) REFERENCES Student(id),
  FOREIGN KEY (exerciseId) REFERENCES Exercise(id)
);

INSERT INTO Cohort (Name) VALUES ('Evening 6');

INSERT INTO Cohort (Name) VALUES ('Day 36');

INSERT INTO Cohort (Name) VALUES ('Day 35');

INSERT INTO ProgrammingLanguage (Name) VALUES ('Javascript');

INSERT INTO ProgrammingLanguage (Name) VALUES ('Python');

INSERT INTO Exercise (Name, languageId) VALUES ('Chicken Monkey', 1);

INSERT INTO Exercise (Name, languageId) VALUES ('Chicken Monkey', 2);

INSERT INTO Exercise (Name, languageId) VALUES ('Businesses', 1);

INSERT INTO Exercise (Name, languageId) VALUES ('Cars', 2);

INSERT INTO Exercise (Name, languageId) VALUES ('Animals', 1);

INSERT INTO Instructor VALUES (NULL, 'Jisie', 'David', 2, 'jisie.david', 'databases');

INSERT INTO Instructor VALUES (NULL, 'Steve', 'Brownlee', 1, 'steve.brownlee', 'code');

INSERT INTO Instructor VALUES (NULL, 'Joe', 'Sheperd', 3, 'joe.sheperd', 'theatre');

INSERT INTO Student VALUES (NULL, 'Manila', 'Bui', 'manila.bui', 1);

INSERT INTO Student VALUES (NULL, 'Matt', 'Blagg', 'matt.blagg', 2);

INSERT INTO Student VALUES (NULL, 'Corri', 'Golden', 'corri.golden', 3);

INSERT INTO Student VALUES (NULL, 'Ryan', 'Cunningham', 'ryan.cun', 1);

INSERT INTO Student VALUES (NULL, 'Lauren', 'Riddle', 'lauren.r', 2);

INSERT INTO Student VALUES (NULL, 'Sully', 'P', 'sully.p', 3);

INSERT INTO Student VALUES (NULL, 'Cassie', 'Boyd', 'c.boyd', 1);

INSERT INTO StudentToExercise VALUES (NULL, 1, 1);

INSERT INTO StudentToExercise VALUES (NULL, 1, 2);

INSERT INTO StudentToExercise VALUES (NULL, 2, 2);

INSERT INTO StudentToExercise VALUES (NULL, 2, 3);

INSERT INTO StudentToExercise VALUES (NULL, 3, 3);

INSERT INTO StudentToExercise VALUES (NULL, 3, 4);

INSERT INTO StudentToExercise VALUES (NULL, 4, 4);

INSERT INTO StudentToExercise VALUES (NULL, 4, 5);

INSERT INTO StudentToExercise VALUES (NULL, 5, 1);

INSERT INTO StudentToExercise VALUES (NULL, 5, 3);

INSERT INTO StudentToExercise VALUES (NULL, 6, 1);

INSERT INTO StudentToExercise VALUES (NULL, 6, 4);

INSERT INTO StudentToExercise VALUES (NULL, 7, 1);

INSERT INTO StudentToExercise VALUES (NULL, 7, 5);