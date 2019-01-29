import sqlite3
from headfirstpython.practice.download.files import *


def insert_db_download(db_connection, uid, uname, filename, save_location):
    connection = sqlite3.connect(db_connection)
    cursor = connection.cursor()
    result = cursor.execute("""SELECT * FROM user WHERE userid=?""", [uid])
    userData = result.fetchone()
    aweme_list = getVidsList(filename)

    if userData is None:
        # Insert User Table
        cursor.execute("""INSERT INTO USER (USERID, USERNAME) VALUES (?, ?)""", [uid, uname])
    else:
        # Update User Table
        cursor.execute("""UPDATE USER SET USERNAME=?""", [uname])

    # Insert Vid Table
    for tiktok in aweme_list:
        target_name = tiktok["aweme_id"]
        target = tiktok["video"]["play_addr"]["url_list"][0]
        media_type = tiktok["media_type"]
        if media_type == 4:
            # Detect whether there is existing vid
            result = cursor.execute("""SELECT * FROM VIDEO WHERE VID=?""", [target_name])
            if result is None:
                cursor.execute("""INSERT INTO VIDEO(VID, UID) VALUES(?,?)""", [target_name, uid])
                do_load_media(target, save_location + uname + "___" + target_name + ".mp4")

    connection.commit()
    connection.close()