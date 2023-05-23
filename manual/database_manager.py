import mysql.connector
import config

class DatabaseManager:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            passwd=config.DB_PASSWORD,
            database=config.DB_DATABASE
        )
        self.db_cursor = self.db.cursor()

    def create_table(self, table_name):
        self.db_cursor.execute("SHOW TABLES LIKE %s", (table_name,))
        result = self.db_cursor.fetchone()

        if result:
            print("Table '{}' already exists.".format(table_name))
        else:
            query = "CREATE TABLE `{}` (name VARCHAR(50), rating VARCHAR(50), text VARCHAR(16000), date VARCHAR(50), reviewID int PRIMARY KEY AUTO_INCREMENT)".format(
                table_name)
            self.db_cursor.execute(query)
            print("Table '{}' created successfully.".format(table_name))

    def insert_into_table(self, table_name, reviewer_name, rating, text, date):
        truncated_text = text[:500]  # Truncate the text to 500 characters
        query = "INSERT INTO `{}` (name, rating, text, date) VALUES (%s, %s, %s, %s)".format(table_name)
        values = (reviewer_name, rating, truncated_text, date)
        self.db_cursor.execute(query, values)
        self.db.commit()

    def describe_table(self, table_name):
        query = "DESCRIBE `{}`".format(table_name)
        self.db_cursor.execute(query)
        result = self.db_cursor.fetchall()
        for row in result:
            print(row)

"""
    USAGE: 
        
        db_manager = DatabaseManager()
        db_manager.create_table("<table_name>")
        db_manager.insert_into_table("<table_name>", "John Doe", "5", "Great food!", "2022-04-09")
        db_manager.describe_table("<table_name>")
"""

