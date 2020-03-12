from data import connection


def add_order(data):
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Orderinfo (customerid, productid, serviceid, origindate, finalperiod, finalprice) VALUES (?, ?, ?, ?, ?, ?)", data)
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


def get_order(custid):
    try:
        conn = connection.establish_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Orderinfo Where customerid = ?", (custid,))
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
