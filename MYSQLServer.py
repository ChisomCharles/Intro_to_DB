import mysql.connector

def create_database(host_name, user_name, user_password, db_name):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        connection.commit()
        print(f"Database '{db_name}' created successfully!")
    except mysql.connector.Error as error:
        print(f"Error: '{error}'")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    host_name = "localhost"
    user_name = "root"
    user_password = "your_password"  # Replace with your MySQL password
    db_name = "alx_book_store"
    create_database(host_name, user_name, user_password, db_name)


