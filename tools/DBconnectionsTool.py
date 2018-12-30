from mysql import connector

class connection(object):

    con = ''

    def connect_mysql(self):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': 'test1234',
            'db': 'spider',
            'charset': 'utf8'
        }

        self.con = connector.connect(**config)
        # 使用cursor()方法获取操作游标
        # cursor = self.con.cursor()

        return self.con

    def close_mysql(self):

        # 关闭数据库连接
        self.con.close()

    def insert(self, query):

        con = connection.connect_mysql(self)
        # SQL 插入语句
        sql = query
        print(sql)
        try:
            cursor = con.cursor()
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            con.commit()
        except Exception as e:
            # Rollback in case there is any error
            print('---------------------------')
            print(sql)
            print('Rollback in case there is any error: ')
            print(e)
            con.rollback()
        # 关闭数据库连接
        con.close()