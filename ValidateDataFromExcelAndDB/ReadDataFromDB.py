import pymysql

# Establish DB connection

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='employee_db',
    charset='utf8'
)

cursor= connection.cursor()

# Fetch data

query = "Select * from salary_info"
cursor.execute(query)  # execute the query

db_data = cursor.fetchall()  # fetch data

print(db_data)  # print the output