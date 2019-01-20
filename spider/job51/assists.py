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


def format_salary_final(salary):
    salary_final = salary

    if '-' in salary:
        salary = salary.replace("千/月", "")
        salary_temp = salary.split('-')
        salary_left = round(float(salary_temp[0]), 2)
        salary_right = round(float(salary_temp[1]), 2)

        salary_final = (salary_left + salary_right) / 2
    elif '-' not in salary:
        salary_final = salary.replace("千/月", "")

    return salary_final


def format_salary(salary):
    salary_final = salary
    salary_unit = '千/月'
    if (salary.endswith("万/年")):
        salary = salary.replace("万/年", "")
        salary_temp = salary.split('-')
        salary_left = round(float(salary_temp[0]) / 12 * 10, 2)
        salary_right = round(float(salary_temp[1]) / 12 * 10, 2)
        salary_final = salary_left.__str__() + '-' + salary_right.__str__() + salary_unit.__str__()
    elif (salary.endswith("万/月")):
        salary = salary.replace("万/月", "")
        salary_temp = salary.split('-')
        salary_left = round(float(salary_temp[0]) * 10, 2)
        salary_right = round(float(salary_temp[1]) * 10, 2)
        salary_final = salary_left.__str__() + '-' + salary_right.__str__() + salary_unit.__str__()
    elif (salary.endswith("元/天")):
        salary = salary.replace("元/天", "")
        salary_temp = float(salary) * 22 / 1000
        salary_final = salary_temp.__str__() + salary_unit
    elif salary == '':
        salary_final = 'Null'
    else:
        salary_final = salary
    return salary_final
