import sqlite3

# Connect to Database


conn = sqlite3.connect("bot.db")
cursor = conn.cursor()



# CREATE TABLE


def create_table():

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY,
        coins INTEGER,
        xp INTEGER,
        level INTEGER)''')

    conn.commit()



# INSERT USER


def add_user(user_id, coins, xp, level):

    cursor.execute(
        """
        INSERT INTO users(id,coins,xp,level)
        VALUES(?,?,?,?)
        """,
        (user_id, coins, xp, level)
    )

    conn.commit()



# SELECT ONE USER


def get_user(user_id):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    return cursor.fetchone()



# SELECT ALL USERS


def get_all_users():

    cursor.execute(
        "SELECT * FROM users"
    )

    return cursor.fetchall()



# UPDATE COINS

def update_coins(user_id, coins):

    cursor.execute(
        """
        UPDATE users
        SET coins=?
        WHERE id=?
        """,
        (coins, user_id)
    )

    conn.commit()



# DELETE USER


def delete_user(user_id):

    cursor.execute(
        """
        DELETE FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    conn.commit()



# Close Database

conn.close()
