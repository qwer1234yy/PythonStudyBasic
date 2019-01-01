from tools import DBconnectionsTool


def get_count_location(self, location):
    query = "SELECT COUNT(id) total FROM 51job_position_v1 WHERE locate('{0}',location)".format(location)
    count = 0
    con = DBconnectionsTool.connection.connect_mysql(self)
    try:
        cursor = con.cursor()
        # 执行sql语句
        cursor.execute(query)
        result = cursor.fetchone()
        count = result[0]
    except Exception as e:
        print('Rollback in case there is any error: ')
        print(e)
        con.close()
    return count
