"""1- vazifa"""

# from collections import Counter
# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="Foundation"
# )

# my = mydb.cursor()

# mydb.commit()

# my.execute("select * from pharmacy where  drug_price > 200 and  drug_price < 500 order by drug_company desc")
# print(my.fetchall())
# print("=======================================================================\n\n\n")
# a = []
# my.execute("select drug_country from pharmacy")
# a = my.fetchall()

# print(Counter(a))


"""2-vazifa"""


import mysql.connector
my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Foundation"
)
my_cursor = my_database.cursor()
my_database.commit()

my_cursor.execute(
    "select first_name, login, password, position from Registry where position like 'Senior Developer' order by first_name ")
print(my_cursor.fetchmany(20))

my_cursor.execute(
    "select first_name, login, password, position, email from Registry where email like '%@google.%' order by position")
print(my_cursor.fetchmany(5))
