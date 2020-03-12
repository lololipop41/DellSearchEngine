from data import connection


def get_product_support(pid):
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Support WHERE productid = ?", (pid,))
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
