
import pymongo
from urllib.parse import quote

# Credentials
password = "veHt1JK5"
encoded_password = quote(password)
user_name = 'qa_agency'
db_name = "trado_qa"


def create_mongo_connection(user_name, encoded_password, db_name):
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{encoded_password}@cluster0.qnr3p.mongodb.net/{db_name}?retryWrites=true&w=majority")
    db = client[db_name]
    return db


def show_connection(db):
    try:
        db.command("ping")
        print("Connected to MongoDB.")
    except Exception as e:
        print("Error connecting to MongoDB:", e)


def display_collections(db):
    collections = db.list_collection_names()
    print(f'Collections in {db_name}: {collections}')


def check_users_active_and_not_active(db):
    users = db['users']
    users_active = users.count_documents({ 'active': True})
    print(f"There are {users_active} users active in DB")
    users_not_active = users.count_documents({ 'active': False})
    print(f"There are {users_not_active} users not active in DB")
    print(f"There are {users_active +users_not_active} users in DB")


def get_my_user(db,phone_num):
    collection = db['users']
    document = collection.find_one({'phone': phone_num})
    print(f"My Details: {document}" )


def check_products_active_and_not_active(db):
    products = db['products']
    products_active = products.count_documents({ 'active': True})
    print(f"There are {products_active} products active in DB")
    products_not_active = products.count_documents({ 'active': False})
    print(f"There are {products_not_active} products not active in DB")
    print(f"There are {products_active +products_not_active} products in DB")


def check_products_with_and_without_sales_Quantity(db):
    products = db['products']
    without_salesQuantity = products.count_documents({ 'salesQuantity': 0 })
    print(f"There are {without_salesQuantity} products of none sales Quantity in DB")
    with_salesQuantity = products.count_documents({ 'salesQuantity': {"$gt":0} })
    print(f"There are {with_salesQuantity} products of  sales Quantity in DB")
    print(f"There are {without_salesQuantity + with_salesQuantity} products in DB")

def check_languages(db):
    collection = db['languages']
    distinct_values = collection.distinct('name')
    print(f"There are {distinct_values} languages in Trado web")

def check_productStock_1(db):
    collection = db['products']
    document = collection.find_one({'name': "קורונה"})
    if document:
        value = document.get("productStock")
        if value != '1000':
            print(f"Name Product:קורונה the productStock in DB: {value} , in web the productStock: 1000")
        else:
            print(f"Name Product:קורונה the productStock in DB and in web{value}")

def check_productStock_2(db):
    collection = db['products']
    document = collection.find_one({'name': "אקדיה"})
    if document:
        value = document.get("productStock")
        if value != '10000':
            print(f"Name Product:אקדיה the productStock in DB: {value} , in web the productStock: 10000")
        else:
            print(f"Name Product:אקדיה the productStock in DB and in web{value}")

def check_productStock_3(db):
    collection = db['products']
    document = collection.find_one({'name': "שמן למון קוש"})
    if document:
        value = document.get("productStock")
        if value != '10000':
            print(f"Name Product:שמן למון קוש the productStock in DB: {value} , in web the productStock: 10000")
        else:
            print(f"Name Product:שמן למון קוש the productStock in DB and in web{value}")

def check_productStock_4(db):
    collection = db['products']
    document = collection.find_one({'name': "קווין ג'קי"})
    if document:
        value = document.get("productStock")
        if value != '10000':
            print(f"Name Product: קווין ג'קי the productStock in DB: {value} , in web the productStock: 10000")
        else:
            print(f"Name Product: קווין ג'קי the productStock in DB and in web{value}")

def check_productStock_5(db):
    collection = db['products']
    document = collection.find_one({'name': "גורילה גלו"})
    if document:
        value = document.get("productStock")
        if value != '10000':
            print(f"Name Product: גורילה גלו the productStock in DB: {value} , in web the productStock: 10000")
        else:
            print(f"Name Product: גורילה גלו the productStock in DB and in web{value}")


def main():
    db = create_mongo_connection(user_name, encoded_password, db_name)
    print(show_connection(db))
    print(display_collections(db))
    print(check_users_active_and_not_active(db))
    print((get_my_user)(db,"0523387577"))
    print(check_products_active_and_not_active(db))
    print(check_products_with_and_without_sales_Quantity(db))
    print(check_languages(db))
    print(check_productStock_1(db))
    print(check_productStock_2(db))
    print(check_productStock_3(db))
    print(check_productStock_4(db))
    print(check_productStock_5(db))


if __name__ == '__main__':
    main()