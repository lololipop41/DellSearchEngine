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


def read_service(pid, sid):
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Support WHERE productid = ? AND serviceid = ?", (pid, sid,))
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


def update_support(usage, support_id):
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("Update Support SET usage = ? where supportid = ? ", (usage, support_id,))
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