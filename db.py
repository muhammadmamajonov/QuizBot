import sqlite3


def connect():
    con = sqlite3.connect('database.db')
    return con

def create_table():
    con = connect()
    cur = con.cursor()
    cur.execute("create table answers(user_id, message_id);")
    con.commit()


def insert(user_id, message_id):
    con = connect()
    cur = con.cursor()
    cur.execute(f"insert into answers values({user_id}, {message_id});")
    con.commit()



def is_answered(user_id, message_id):
    con = connect()
    cur = con.cursor()
    query = f"select * from answers where user_id={user_id} and message_id={message_id};"
    cur.execute(query)
    data = cur.fetchall()
    return bool(data)


if __name__ == '__main__':
    create_table()