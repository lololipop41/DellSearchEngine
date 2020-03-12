from data import connection


def get_user():
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer")
        records = cursor.fetchall()
        return records
    except Exception as err:
        if conn:
            print("Connection Failed!", err)
    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("Connection Closed!")


def add_user(data):
    try:
        print(data)
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Customer (username, password) VALUES (?, ?)", data)
        conn.commit()
        return True
    except Exception as err:
        if conn:
            print("Connection Failed!", err)
    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("Connection Closed!")