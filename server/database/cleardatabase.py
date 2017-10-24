import mysql.connector
from mysql.connector import errorcode

def drop_table(table):
    # Add user into the table, initially unverified
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='users')
    cursor = cnx.cursor()
    query = ("DROP TABLE IF EXISTS `%s`")
    cursor.execute(query, table)
    cnx.commit()
    cursor.close()
    cnx.close()

if __name__ == '__main__':
    drop_table('users')
    drop_table('notifications')
