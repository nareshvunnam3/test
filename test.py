import sqlite3

def get_user_info(username):
    # Connect to the database
    password = 'password'
    username = 'abc@getethos.com'
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    conn.close()
    return result

# Example usage
user_input = input("Enter your username: ")
user_info = get_user_info(user_input)
print(user_info)
