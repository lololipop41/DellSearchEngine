from data import connection


def validate(data):
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer")
        records = cursor.fetchall()
        record = list(filter(lambda item: data in item, records))
        if any(data in x for x in record):
            return False, "Username already existed!"
        else:
            return True, "Username valid!"
    except Exception as error:
        if conn:
            print("Validation Fail! ", error)
    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("Connection Closed!")
