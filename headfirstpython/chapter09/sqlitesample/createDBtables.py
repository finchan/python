import sqlite3

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE [athletes](
        [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
        [name] TEXT NOT NULL, 
        [dob] DATE NOT NULL);
""")
cursor.execute("""
    CREATE TABLE [timing_data](
        [athlete_id] INTEGER NOT NULL REFERENCES athletes([id]), 
        [value] TEXT NOT NULL);

""")
connection.commit()
connection.close()