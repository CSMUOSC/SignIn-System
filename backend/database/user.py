from pymysql import NULL
from database import crud
from datetime import datetime

class  User(crud.BasicDatabase):
    def __init__(self,):
        super(User, self).__init__("user")

    def searchExsit(self, userId):
        ret = self.run("select * from user where userId = {};".format(userId))
        return ret

    def createUser(self, name, userId, email, info= None, admin=0):
        now = datetime.now()
        createdAt = str(now.strftime("%Y-%m-%d %H:%M:%S"))

        print('INSERT INTO user(name, userId, email, info, createdAt, admin) VALUES("{}", "{}", "{}", {}, "{}", {})'.format \
            (name, userId, email, info , createdAt, admin))
        ret = self.run('INSERT INTO user(name, userId, email, info, createdAt, admin) VALUES("{}", "{}", "{}", "{}", "{}", {})'.format \
            (name, userId, email, info , createdAt, admin)) 
        
        return ret

if __name__ == "__main__":
    db = User()
    db.createUser("王小明", "0770011", "email@test.com", admin = 0)