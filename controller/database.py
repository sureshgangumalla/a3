import mysql.connector
from .customexception import CustomException




class Assign3Database:
    # THIS IS THE ONLY FILE THAT WILL ALWAYS DIFFER FROM TEST / DEVINT / PROD

    user = 'sibbala'
    password = 'B00779862'
    host = 'db.cs.dal.ca'
    database = 'sibbala'
    port = '3306'

    def __init__(self, user=None, password=None, host=None, database=None):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def data_connect(self, dict = False):
        try:
            cnx = mysql.connector.connect(user='CSCI5308_16_DEVINT_USER', password='CSCI5308_16_DEVINT_16175',
                                          host='db-5308.cs.dal.ca', database='CSCI5308_16_DEVINT')

        except mysql.connector.Error as e:
            print(e.errno)        # 2003
            print(e.sqlstate)  # SQLSTATE value
            # Error message:%s Can't connect to MySQL server on 'db-5308.cs.dal.c:3306' (11001 getaddrinfo failed)
            print(e.msg)
            # Error:%s 2003: Can't connect to MySQL server on 'db-5308.cs.dal.c:3306' (11001 getaddrinfo failed)
            print(e)
            s = str(e)
            # Error:%s 2003: Can't connect to MySQL server on 'db-5308.cs.dal.c:3306' (11001 getaddrinfo failed)
            print(s)
            # raise CustomException("error/2003.html")
            return e.sqlstate
        return cnx


# cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
