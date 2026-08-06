import bcrypt 
from utils.db import connect_db

def authenticate(username,password):
    connection = connect_db()
    cursor=connection.cursor(dictionary=True)
    
    query = """
    SELECT * FROM users
    WHERE username =%s
    """
    
    cursor.execute(query,(username,))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if user:
        stored_hash = user["password_hash"].encode()
        
        if bcrypt.checkpw(password.encode(), stored_hash):
            return user
    
    return None
    