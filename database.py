import psycopg2
from psycopg2 import sql


# Function to connec to the PostgreSQL database
def connect_to_db():
    try:
        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            host="localhost",
            database="mydatabase",  # Replace with your DB name
            user="song9537",  # Replace with your username
            password="qwaszx56",  # Replace with your password
        )
        connection.autocommit = True  # Enable autocommit to make changes immediately
        print("Connection to PostgreSQL DB successful")
        return connection
    except Exception as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        return None


# Function to create a table
def create_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS GF_Data(
            date DATE,
            student_name VARCHAR(255),
            form_id VARCHAR(255)
        );
        """
        cursor.execute(create_table_query)
        print("Table created successfully")
    except Exception as error:
        print(f"Error while creating table: {error}")


# Fucntion to insert data into the table
def insert_data(connection, date, student_name, form_id):
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO GF_Data (date, student_name, form_id)
        VALUES (%s, %s, %s);
        """
        cursor.execute(insert_query, (date, student_name, form_id))
        print("Data inserted successfully")
    except Exception as error:
        print(f"Error while inserting data: {error}")


# Function to query data from the table
def query_data(connection):
    try:
        cursor = connection.cursor()
        select_query = "SELECT * From GF_Data;"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        print("Query Results:")
        for row in rows:
            print(row)
    except Exception as error:
        print(f"Error while querying data: {error}")
