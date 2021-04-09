import pymysql
db = pymysql.connect(
    "localhost","root","","mypython"
    )
try:
    cursor = db.cursor()
    sql = "SELECT location FROM department"
    try:
        cursor.execute(sql)
        for row in cursor:
            print(row)
    except:
        print('ERROR UNABLE TO FETCH DATA!!!!')
finally:
    db.close()
