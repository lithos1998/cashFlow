import sqlite3


def connect_db():
    connection = sqlite3.connect("testdb.db")

    return connection


def create_tables():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("CREATE TABLE TRANSACTIONS("
                   "TRANSACTION_ID integer primary key autoincrement unique,"
                   "SERVICE_ID integer,"
                   "AMOUNT integer not null,"
                   "DATE datetime not null,"
                   "DESCRIPTION text)")

    cursor.execute("CREATE TABLE SERVICES("
                   "SERVICE_ID integer primary key autoincrement,"
                   "CATEGORY_ID integer not null,"
                   "TYPE_ID integer not null,"
                   "SERVICE_NAME text not null)")

    cursor.execute("CREATE TABLE CATEGORIES("
                   "CATEGORY_ID integer primary key autoincrement,"
                   "CATEGORY_NAME text not null)")

    cursor.execute("CREATE TABLE TRANSACTION_TYPES("
                   "TYPE_ID integer primary key autoincrement,"
                   "TYPE_NAME text not null)")
    print("Tables created")


def insert_data():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("insert into CATEGORIES "
                   "values (1001, 'Services'),"
                   "(1002, 'Food'),"
                   "(1003, 'Supermarket'),"
                   "(1004, 'Car'),"
                   "(1005, 'Fun'),"
                   "(1006, 'Others')")

    cursor.execute("insert into TRANSACTION_TYPES "
                   "values (111, 'expense'),"
                   "(222, 'income')")

    cursor.execute("insert into SERVICES (CATEGORY_ID, TYPE_ID, SERVICE_NAME) "
                   "values (1004, 111, 'Gasoline'),"
                   "(1004, 111, 'Car Wash'),"
                   "(1004, 111, 'Formalities'),"
                   "(1004, 111, 'Repair'),"
                   "(1004, 111, 'Accesories'),"
                   "(1004, 111, 'Others'),"
                   "(1003, 111, 'Consumible'),"
                   "(1003, 111, 'drinks'),"
                   "(1003, 111, 'Others'),"
                   "(1001, 111, 'Phone'),"
                   "(1005, 111, 'Mangas'),"
                   "(1005, 111, 'Hobbies'),"
                   "(1001, 111, 'Bank account'),"
                   "(1005, 111, 'Party'),"
                   "(1005, 111, 'Steam'),"
                   "(1001, 111, 'Clothes'),"
                   "(1001, 111, 'Decoration'),"
                   "(1004, 222, 'Trips'),"
                   "(1006, 222, 'It job'),"
                   "(1006, 222, 'Little job'),"
                   "(1006, 222, 'Others')")

    db.commit()
    print("data inserted")


def create_database():
    create_tables()
    insert_data()


db = connect_db()
cursor = db.cursor()



# insert_data()
# create_tables()



