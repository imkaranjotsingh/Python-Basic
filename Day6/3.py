import pymysql
db = pymysql.connect(
    "localhost","root","","mypython"
    )
try:
    cursor = db.cursor()
    sql = "SELECT * FROM test"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            idno = row[0]
            name = row[1]
            mobileno = row[2]
            salary = row[3]
            print('idno = %s, name = %s, mobileno = %s, salary = %s'%(idno,name,mobileno,salary))
    except:
        print('Error:unable to fetch data!!!')
finally:
              db.close()
