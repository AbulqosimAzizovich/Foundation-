import mysql.connector


class Database():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="Foundation"
        )

        self.cursor = self.mydb.cursor()
        self.create_table()
        # self.insert_table()
        self.inner_join()
        self.left_join()
        self.right_join()
        # self.full_outer_join()

    def create_table(self):
        self.cursor.execute("""create table if not exists Kurs(
        kurs_id int auto_increment, kurs_name varchar(30), 
        teacher varchar(50), primary key(kurs_id)) """)

        self.cursor.execute("""create table if not exists Talaba(
        talaba_id int primary key auto_increment, talaba_name varchar(30),
        kurs_id int)""")

    def insert_table(self):
        self.cursor.executemany("insert into Kurs(kurs_name, teacher) values(%s, %s)",
                                [("Fronted", "Shahboz aka"),
                                 ("Flutter", "Abdusamad aka"),
                                 ("Full-stack", "Husanboy Mansurov"),
                                 (".Net", "John"),
                                 ("Java", "Mayk"),
                                 ("Golang", "Antony",)])

        self.cursor.executemany("insert into Talaba(talaba_name, kurs_id) values(%s,%s)",
                                [("Behzod", 7), ("A. Samandar", 2), ("Dilxiroj", 3),
                                 ("Saidazim", 4), ("Muhammadamin",
                                                   1), ("T. Samandar", 4),
                                 ("Mirshod", 3), ("Bekzod", 1), ("Abdunazir", 5),
                                 ("Javohir", 4), ("Feruza", 4), ("Rasuljon", 2)])
        self.mydb.commit()

    def inner_join(self):
        print("Inner Join")
        self.cursor.execute("""select talaba_id, talaba_name, kurs_name, teacher 
        from Kurs inner join Talaba on Kurs.kurs_id = Talaba.kurs_id """)

        text = self.cursor.fetchall()

        for i in text:
            print(i)

    def left_join(self):
        print("Left Join")
        self.cursor.execute("""select talaba_id, talaba_name, kurs_name, teacher 
        from Kurs left join Talaba on Kurs.kurs_id = Talaba.kurs_id """)

        text = self.cursor.fetchall()

        for i in text:
            print(i)

    def right_join(self):
        print("Right Join")
        self.cursor.execute("""select talaba_id, talaba_name, kurs_name, teacher 
        from Kurs right join Talaba on Kurs.kurs_id = Talaba.kurs_id """)

        text = self.cursor.fetchall()

        for i in text:
            print(i)

    def full_outer_join(self):
        print("Full Outer Join")
        self.cursor.execute("""select talaba_id, talaba_name, kurs_name, teacher 
        from Kurs full outer join Talaba on Kurs.kurs_id = Talaba.kurs_id """)

        text = self.cursor.fetchall()

        for i in text:
            print(i)


db = Database()
