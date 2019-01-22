import sqlite3
import glob
from athletemodel import put_to_store
from athletelist import AthleteList

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

data_files = glob.glob("../data/*.txt")
athletes = put_to_store(data_files)
for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob
    cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))
    cursor.execute("SELECT id FROM athletes WHERE name=? AND dob=?", (name, dob))
    the_current_id = cursor.fetchone()[0]
    for each_time in athletes[each_ath].clean_data:
        cursor.execute('INSERT INTO timing_data(athlete_id, value) VALUES (?, ?)', (the_current_id, each_time))
connection.commit()
connection.close()