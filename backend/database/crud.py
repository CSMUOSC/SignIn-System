import pymysql
from database import dbconfig

class BasicDatabase():
    def __init__(self, table):
        self.table = table
        config = dbconfig.dbconfig
        self.conn = pymysql.connect(host=config["host"], port=config["port"], user=config["user"], passwd=config["password"], db=config["database"], charset='utf8')
        self.cursor = self.conn.cursor()
        row1 = self.cursor.execute("describe user")

    def run(self, cmd):
        ret = self.cursor.execute(cmd)
        self.conn.commit()
        return ret

    def destory(self):
        self.cursor.close()
        self.conn.close()

