import pymysql
db = pymysql.connect(
    "localhost","root","","mypython"
    )
try:
    cursor = db.cursor()
    #sql = "SELECT empname, MAX(salary) AS salary FROM department WHERE salary IN(SELECT salary FROM department MINUS SELECT MAX(salary) FROM department)"
    #sql = "SELECT max(salary) FROM department WHERE salary NOT IN (SELECT max(salary) FROM department))"
    sql = "SELECT empname, MAX(salary) AS salary FROM department WHERE salary < (SELECT MAX(salary) FROM department)"
    try:
        cursor.execute(sql)
        for row in cursor:
            print(row)
    except:
        print('Error Unable to Fetch Data!!!!')
finally:
    db.close()
