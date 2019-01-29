import sqlite3
from headfirstpython.practice.download.files import *

def insertData(db_connection, uid, uname, filename, save_location, prefix):
    connection = sqlite3.connect(db_connection)
    cursor = connection.cursor()
    result = cursor.execute("""SELECT * FROM user WHERE userid=?""", [uid])
    userData = result.fetchone()
    aweme_list = getVidsList(filename)
    if userData is None:
        # Insert User Table
        cursor.execute("""INSERT INTO USER (USERID, USERNAME) VALUES (?, ?)""", [uid, uname])
        # Inserrt Vid Table
        for tiktok in aweme_list:
            target_name = tiktok["aweme_id"]
            target = tiktok["video"]["play_addr"]["url_list"][0]
            media_type = tiktok["media_type"]
            if media_type == 4:
                cursor.execute("""INSERT INTO VIDEO (VID, UID, PROCESSED) VALUE(?,?,?)""", [])
                do_load_media(target, save_location + prefix + "___" + target_name + ".mp4")

        connection.commit()
    else:
        # Update User Table and Vid Table
        pass
    connection.close()