import pyodbc


def establish_connection():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-98SH10H;"  # Depends on the server name
        "Database=DellSupport;"
        "Trusted_Connection=yes;"
    )

    return conn


# cursor = establish_connection().cursor()
# cursor.execute('SELECT * FROM Customer')
#
# for row in cursor:
#     print('row = %r' % (row,))
