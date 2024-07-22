import os
import pyodbc
from dotenv import load_dotenv


load_dotenv()

SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER},{PORT};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'


# print(connectionString)

conn = pyodbc.connect(connectionString)

cursor = conn.cursor()
