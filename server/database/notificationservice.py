import mysql.connector

def notify(info):
    # Add user into the table, initially unverified
    token = info["token"]
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='users')
    cursor = cnx.cursor()
    query = ("SELECT n.notification_id FROM notifications AS n"
         "INNER JOIN users AS u ON n.user_id = u.user_id"
         "WHERE u.token = %s")
    cursor.execute(query, token)
    for (notification_id) in cursor:
        # TODO load the notification information from a non-relational db and return it
        print(notification_id)
    cnx.commit()
    cursor.close()
    cnx.close()
    return [1, 4]
