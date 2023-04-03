
import pymongo
from urllib.parse import quote
from bson import ObjectId
import random

# Credentials
password = "veHt1JK5"
encoded_password = quote(password)
user_name = 'qa_agency'
db_name = "trado_qa"
id_meshi = "641ab56e7b57055c78b51abe"


def create_mongo_connection(user_name, encoded_password, db_name):
    # Connect to MongoDB using the given credentials and return the database object
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{encoded_password}@cluster0.qnr3p.mongodb.net/{db_name}?retryWrites=true&w=majority")
    db = client[db_name]
    return db

def get_specific_key_value(db, collection_name, document_id, key):
    collection = db[collection_name]
    document = collection.find_one({'_id': ObjectId(document_id)})
    if document:
        value = document.get(key)
        return value
    else:
        return None

def code():
    db = create_mongo_connection(user_name, encoded_password, db_name)
    num_code = get_specific_key_value(db, "users",id_meshi , "loginCode")
    print(num_code)
    return num_code


################################################################################################
def loop_for_valid_phone():
    num = "057"
    for i in range(7):
        x = str(random.randint(0,9))
        num = num + x
    return num


def get_specific_key_value_2(phone_num):
    db = create_mongo_connection(user_name, encoded_password, db_name)
    collection = db['users']
    document = collection.find_one({'phone': phone_num})
    doc_code = document['loginCode']
    return doc_code



