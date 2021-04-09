import pymysql
db = pymysql.connect(
    "localhost","root","","mypython"
    )
try:
    cursor = db.cursor()
    sql = "SELECT dname FROM department WHERE empname = 'raj'"
    try:
        cursor.execute(sql)
        for row in cursor:
            print(row)
    except:
        print('Error Unable to Fetch Data!!!!')
finally:
    db.close()
