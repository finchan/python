import sqlite3
import glob
from athletemodel import put_to_store
from athletelist import AthleteList
import yate

connection = sqlite3.connect('data/coachdata.sqlite')
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

data_files = glob.glob("data/*.txt")
athletes = put_to_store(data_files)
for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob
    cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))
    results = cursor.execute("SELECT id FROM athletes WHERE name=? AND dob=?", (name, dob))
    the_current_id = results.fetchone()[0]
    for each_time in athletes[each_ath].clean_data:
        cursor.execute('INSERT INTO timing_data(athlete_id, value) VALUES (?, ?)', (the_current_id, each_time))
connection.commit()
connection.close()

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.include_footer({"Home":"/index.html"}))