import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user  = 'root',
    password = '',
    db = 'mypython'
    )
try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO test VALUES(105,'daaa','1176534567',15000)"
        try:
            cursor.execute(sql)
            print('TAsk AddEd SuCCeSSSFully')
        except:
            print('OOPS !! Somthing Went Wrong !!')
        connection.commit()
finally:
    connection.close()


