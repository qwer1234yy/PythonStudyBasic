import unittest
from tools import DBconnectionsTool
from spider.job51 import queries
from spider.job51.test_first import position
from spider.job51 import assists


class AnalysisTool(unittest.TestCase):

    def test_format_salary_final(self):
        print(assists.format_salary_final('15.0-20.0千/月'))

    def test_get_count_per_city(self):
        result = DBconnectionsTool.connection.get_sql_excuted_result(queries.sql_get_count_per_city)
        position_count_per_city = {}
        for i in result:
            position_count_per_city[i[1]] = i[0]
        return position_count_per_city

    def test_get_max_salary_per_city(self):
        result = DBconnectionsTool.connection.get_sql_excuted_result(queries.sql_get_max_salary_per_city)
        position_count_per_city = {}
        for i in result:
            position_count_per_city[i[1]] = i[0]
        return position_count_per_city

    def test_uniform_salary(self):
        sql = "SELECT * from 51job_position_v3 WHERE salary like '%-%'"

        con = DBconnectionsTool.connection.connect_mysql(self)
        cursor = con.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            update_sql = "UPDATE 51job_position_v3 SET avg_salary = '{0}' WHERE id = {1}".format(
                assists.format_salary_final(assists.format_salary(i[4])), i[0])
            print(update_sql)
            try:
                # 执行sql语句
                cursor.execute(update_sql)
                # 提交到数据库执行
                con.commit()
                con.close
            except Exception as e:
                # Rollback in case there is any error
                print('---------------------------')
                print(sql)
                print('Rollback in case there is any error: ')
                print(e)
                con.rollback()
        con.close

    def test_get_data(self):
        sql = "SELECT * from 51job_position_v3 WHERE salary like '%元%' "
        update_sql = 'UPDATE 51job_position_v3 SET salary = {0} WHERE id = {1}'
        con = DBconnectionsTool.connection.connect_mysql(self)
        cursor = con.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            update_sql = "UPDATE 51job_position_v3 SET salary = '{0}' WHERE id = {1}".format(
                assists.format_salary(i[4]), i[0])
            print(update_sql)
            try:
                # 执行sql语句
                cursor.execute(update_sql)
                # 提交到数据库执行
                con.commit()
                con.close
            except Exception as e:
                # Rollback in case there is any error
                print('---------------------------')
                print(sql)
                print('Rollback in case there is any error: ')
                print(e)
                con.rollback()


if __name__ == '__main__':
    unittest.main()
