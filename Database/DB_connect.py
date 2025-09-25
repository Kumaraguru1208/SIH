from pymongo import MongoClient, errors

# MongoDB connection URI
MONGO_URI = "mongodb://localhost:27017/"

def get_db():
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.server_info()  # Force connection to test it
        db = client["my_database"]
        return db

    except errors.ServerSelectionTimeoutError as err:
        print("❌ Could not connect to MongoDB server.")
        print(f"Error: {err}")
        return None

    except Exception as e:
        print("❌ An unexpected error occurred while connecting to MongoDB.")
        print(f"Error: {e}")
        return None

# Only run this test when the file is executed directly, not when imported
if __name__ == "__main__":
    db = get_db()
    if db is not None:
        print("✅ MongoDB connection successful.")
    else:
        print("❌ MongoDB connection failed.")
