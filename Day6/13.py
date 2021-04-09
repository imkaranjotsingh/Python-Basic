import pymysql
db = pymysql.connect(
    "localhost","root","","mypython"
    )
try:
    cursor = db.cursor()
    sql = "SELECT empname FROM department WHERE location = 'chd' OR 'mohali' AND empname = 'a%_'"
    try:
        cursor.execute(sql)
        for row in cursor:
            print(row)
    except:
        print('Error Unable to Fetch Data!!!!')
finally:
    db.close()
