import mysql.connector
from mysql.connector import Error

def check_database_connection():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='gesag.cj8ywoakqg0b.ap-southeast-2.rds.amazonaws.com',
            user='admin',
            password='Gesag%5&7(9',
            database='university_db',  # Ensure this is the correct database name
            port=3306
        )

        if connection.is_connected():
            print("Connection to the database was successful!")
            
            # Create a cursor to execute SQL queries
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print("Connected to the database:", db_name)
            
            # Optional: Execute a query to verify access to a table
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            print("Tables in the database:", tables)

            # Close the cursor and connection
            cursor.close()
            connection.close()
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

if __name__ == "__main__":
    check_database_connection()
