
import sqlite3
def createDatabase():
    global connection, cursor
    connection = sqlite3.connect("userData.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        cursor.execute("INSERT INTO `member` (username, password) VALUES('pavithra', 'password')")
        connection.commit()

def getLoginDetails(user,password):

    cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (user, password))
    if cursor.fetchone() is not None:
      return True
    else:
      return False
    cursor.close()
    connection.close()
