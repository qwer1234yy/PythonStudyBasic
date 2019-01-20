import unittest
import tools.DBconnectionsTool as DBconnectionsTool
from spider.job51.test_first import position


class MyTestCase(unittest.TestCase):
    def test_get_all(self):
        con = DBconnectionsTool.connection.connect_mysql(self)

        sql = 'SELECT * FROM 51job_position_v3'

        cursor = con.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()
        positions = []
        for i in result:
            pos = position(position = i[1],company = i[2],location = i[3],salary = i[4],date = i[5],quality = i[6])
            positions.append(pos)

        for j in positions:
            print(j.quality)



        con.close()


if __name__ == '__main__':
    unittest.main()
