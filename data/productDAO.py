from data import connection


def get_product():
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Product")
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


def get_single_product(pid):
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Product WHERE productid = ?", (pid,))
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
