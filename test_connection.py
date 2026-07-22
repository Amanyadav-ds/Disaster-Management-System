from utils.db import connect_db

try:
    connection = connect_db()

    if connection.is_connected():
        print("✅ Database Connected Successfully!")

    connection.close()

except Exception as e:
    print("❌ Error:", e)
    