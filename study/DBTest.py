import unittest
from mysql import connector
import tools.DBconnectionsTool as DBconnector
import tools.DBconnectionsTool as DBconnectionsTool


class MyTestCase(unittest.TestCase):

    cursor = ''
    con = ''

    def setUp(self):

        self.con = DBconnector.connection.connect_mysql(self)
        self.cursor = self.con.cursor()

    def tearDown(self):

        # 关闭数据库连接
        DBconnector.connection.close_mysql(self)

    def test_mysql(self):

        # 使用execute方法执行SQL语句
        self.cursor.execute("SELECT * FROM 51job_position")
        # 使用 fetchone() 方法获取一条数据
        data = self.cursor.fetchone()
        print("Database version : {0} ".format(data))



    def test_insert(self):

        position_='tetet'
        company='tetet'
        location='tete'
        salary='tete'
        date='2018-12-30'
        detail_description='ewewew'
        # SQL 插入语句
        query = """INSERT INTO 51job_position(position,company,location,salary,date,description)VALUES ('{0}', '{1}', '{2}','{3}','{4}','{5}')""".format(
            position_, company, location, salary, date, detail_description)

        DBconnectionsTool.connection.insert(self,query)



if __name__ == '__main__':
    unittest.main()
