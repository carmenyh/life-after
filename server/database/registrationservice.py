import mysql.connector

def register(info):
    # Add user into the table, initially unverified
    # TODO check that there doesn't already exist a user with that username
    # TODO replace the token placeholder with an actual token
    # TODO replace the password with a hashed one
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='users')
    cursor = cnx.cursor()
    add_user = ("INSERT INTO users "
               "(username, password, validated, token) "
               "VALUES (%s, %s, %s, %s)")
    user = (info["username"], info["password"], "N", "token_placeholder")
    cursor.execute(add_user, user)
    cnx.commit()
    cursor.close()
    cnx.close()
    return "token_placeholder"

def get_registered_user(username):
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='users')
    cursor = cnx.cursor(buffered=True)
    get_user = ("SELECT username, password, validated, token FROM users "
               "WHERE username='%s'")
    cursor.execute(get_user, (username))
    for (username, password, validated, token) in cursor:
        # TODO don't return the password
        cnx.commit()
        cursor.close()
        cnx.close()
        return (username, password, validated, token)
