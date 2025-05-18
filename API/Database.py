import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv


class Database:
    def __init__(self):
        load_dotenv()
        # test if environment variables are loaded
        print(os.getenv("DB_NAME"))
        print(os.getenv("DB_USER"))
        print(os.getenv("DB_PASSWORD"))
        print(os.getenv("DB_HOST"))

        # self.dbname = os.getenv("DB_NAME")
        # self.user = os.getenv("DB_USER")
        # self.password = os.getenv("DB_PASSWORD")
        # self.host = os.getenv("DB_HOST")
        self.connection = None



    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.dbname
            )
            if self.connection.is_connected():
                print("Connected to the database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        # Logic to disconnect from the database
        if self.connection.is_connected():
            self.connection.close()
            print("Disconnected from the database")
        else:
            print("No active connection to disconnect")
        pass

    def execute_query(self, query):
        # Logic to execute a query
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            try:
                cursor.execute(query)
                self.connection.commit()
                print("Query executed successfully")
            except Error as e:
                print(f"Error executing query: {e}")
            finally:
                cursor.close()
        else:
            print("No active connection to execute the query")
        pass

    def fetch_results(self):
        # Logic to fetch results from the last executed query
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            try:
                results = cursor.fetchall()
                return results
            except Error as e:
                print(f"Error fetching results: {e}")
            finally:
                cursor.close()
        else:
            print("No active connection to fetch results")
        pass