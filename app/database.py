from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    print("Mongo URI:", app.config.get("MONGO_URI"))
    mongo.init_app(app)

    try:
        # Attempt to access a collection to test the connection
        test_db = mongo.cx.get_database()  # get default DB from URI
        print(f"✅ MongoDB connected successfully to DB: {test_db.name}")
    except Exception as e:
        print("❌ MongoDB connection failed:", str(e))

def get_users_collection():
    return mongo.db.users

def get_websites_collection():
    return mongo.db.websites
