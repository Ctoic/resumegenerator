from app import mongo

def save_user_data(data):
    user_id = mongo.db.users.insert_one(data).inserted_id
    return user_id
