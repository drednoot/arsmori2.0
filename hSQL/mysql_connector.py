import mysql.connector
from mysql.connector import Error
from Constants.secret import HOST, LOGIN, PASSWORD

def create_connection(host_name:str, user_name:str, user_password:str, database_name:str) -> mysql.connector.MySQLConnection:
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def main():
    connection = create_connection(HOST, LOGIN, PASSWORD, 'arsbot')
    print(connection)

if __name__ == "__main__":
    main()