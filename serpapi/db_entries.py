import mysql.connector
import config

# database connection
db = mysql.connector.connect(
    host="localhost", 
    user="root",
    passwd= config.DB_PASSWORD,  
    database="burger_index_serpapi_db"
)

db_cursor = db.cursor()

"""
def create_table(table_name): 
    query = "CREATE TABLE `{}` (name VARCHAR(50), rating VARCHAR(50), text VARCHAR(1000), date VARCHAR(50), reviewID int PRIMARY KEY AUTO_INCREMENT)".format(table_name)
    db_cursor.execute(query)
"""

def create_table(table_name):
    db_cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    result = db_cursor.fetchone()

    if result:
        print("Table '{}' already exists.".format(table_name))
    else:
        query = "CREATE TABLE `{}` (name VARCHAR(50), rating VARCHAR(50), text VARCHAR(16000), date VARCHAR(50), reviewID int PRIMARY KEY AUTO_INCREMENT)".format(table_name)
        db_cursor.execute(query)
        print("Table '{}' created successfully.".format(table_name))


def insert_into_table(table_name, reviewer_name, rating, text, date): 
    truncated_text = text[:500]  # Truncate the text to 500 characters
    query = "INSERT INTO `{}` (name, rating, text, date) VALUES (%s, %s, %s, %s)".format(table_name)
    values = (reviewer_name, rating, truncated_text, date)
    db_cursor.execute(query, values)

    # db_cursor.execute("INSERT INTO Review (name, rating, text, date) VALUES (%s, %s, %s, %s)", (reviewer_name, rating, text, date))
    
    # save the changes
    db.commit()

# fix this function
def describe_table(table_name):
    # db_cursor.execute("DESCRIBE %s", (table_name)) 
    query = "DESCRIBE `{}`".format(table_name)
    db_cursor.execute(query)

    result = db_cursor.fetchall()
    for row in result:
        print(row)

# create_table()

# db_cursor.execute("DESCRIBE Review")

# insert_into_table("ozan", 5, "best food in the town", "04.09.2022")

# db_cursor.execute("SELECT * FROM Review")

# for value in db_cursor: 
#    print(value)