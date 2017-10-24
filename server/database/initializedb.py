import mysql.connector
from mysql.connector import errorcode

# TODO move database creation/destruction to one file
# TODO make enums for shared names

DB_NAME = 'users'

TABLES = {}
TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `user_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "  `username` varchar(20) NOT NULL,"
    "  `password` varchar(20) NOT NULL,"
    "  `validated` enum('Y', 'N') NOT NULL,"
    "   `token` varchar(105)"
    ") ENGINE=InnoDB")

TABLES['notifications'] = (
    "CREATE TABLE `notifications` ("
    "   `notification_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "   `user_id` int(11),"
    "   CONSTRAINT FOREIGN KEY (`user_id`)"
    "       REFERENCES `users` (`user_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='root')
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.iteritems():
    try:
        print("Creating table%s: ", name)
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
