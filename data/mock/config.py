import pymysql


class Config:
    host = '127.0.0.1'
    port = 3306
    database = 'mysql_exercise'
    user = 'root'
    password = 'zhang123'

    connect = pymysql.connect(
        host=host, database=database, port=port, user=user, password=password)
