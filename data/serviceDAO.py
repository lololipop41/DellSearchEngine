from data import connection


def get_service():
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Service")
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


def get_default_service():
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Service WHERE duration = 3")
        record = cursor.fetchall()
        return record[0]
    except Exception as err:
        if conn:
            print("Connection Failed!", err)
    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("Connection Closed!")
