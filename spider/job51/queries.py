sql_get_count_per_city = '''SELECT COUNT(*) as count, LEFT(location,2) as location from 51job_position_v3 GROUP BY LEFT(location,2)
         ORDER BY count DESC LIMIT 20'''
sql_get_max_salary_per_city = '''SELECT COUNT(*) as count, LEFT(location,2) as location from 51job_position_v3 GROUP BY LEFT(location,2)
         ORDER BY count DESC LIMIT 20'''
sql_uniform_salary = "SELECT * from 51job_position_v3 WHERE salary like '%-%'"
