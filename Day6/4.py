import pymysql
db = pymysql.connect(
    "localhost","root","","mypython"
    )
try:
    cursor = db.cursor()
    sql = "DELETE FROM test WHERE NAME ='daa'"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
finally:
    db.close()
