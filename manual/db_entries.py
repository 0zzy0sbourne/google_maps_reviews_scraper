import mysql.connector
import config

# database connection
db = mysql.connector.connect(
    host="localhost", 
    user="root",
    passwd= config.DB_PASSWORD,  
    database="burger_index"
)

db_cursor = db.cursor()

def create_table(table_name): 
    db_cursor.execute( "CREATE TABLE Review (name VARCHAR(50), rating smallint UNSIGNED, text VARCHAR(100), date VARCHAR(50), reviewID int PRIMARY KEY AUTO_INCREMENT)")

def insert_into_table(table_name, reviewer_name, rating, text, date): 
    db_cursor.execute("INSERT INTO Review (name, rating, text, date) VALUES (%s, %s, %s, %s)", (reviewer_name, rating, text, date))
    # save the changes
    db.commit()

# fix this function
def describe_table(table_name):
    db_cursor.execute("DESCRIBE %s", (table_name)) 




# create_table()

# db_cursor.execute("DESCRIBE Review")

# insert_into_table("ozan", 5, "best food in the town", "04.09.2022")

# db_cursor.execute("SELECT * FROM Review")

# for value in db_cursor: 
#    print(value)