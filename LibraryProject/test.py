from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

# Подключение к MongoDB
username = quote_plus("reyget")
password = quote_plus("xPCTVF6:3u,b=qn")
uri = "mongodb+srv://elisaberaudolive:gF4FLZh6NFuYaI01@cluster0.ufxtqwi.mongodb.net/?retryWrites=true&w=majority&appName=PythonWEB"

client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("✅ Успешно подключено к MongoDB!")
except Exception as e:
    print("❌ Ошибка подключения:", e)

# Выбираем базу данных и коллекцию
db = client['LibraryProject']
users_collection = db['Users']

# Данные для вставки
users_to_add = [
    {
        "nameUser": "Admin",
        "surnameUser": "Admin",
        "passwordUser": "password",
        "is_admin": True,
        "emailUser": "admin@gmail.com",
        "numberUser": 123456789
    },
    {
        "nameUser": "Alice",
        "surnameUser": "Smith",
        "passwordUser": "alicepass",
        "is_admin": False,
        "emailUser": "alice@example.com",
        "numberUser": 111222333
    },
    {
        "nameUser": "Bob",
        "surnameUser": "Brown",
        "passwordUser": "bobpass",
        "is_admin": False,
        "emailUser": "bob@example.com",
        "numberUser": 444555666
    }
]

# Добавление с проверкой на дублирующийся email
existing_emails = {
    user["emailUser"] for user in users_collection.find({}, {"emailUser": 1})
}

for user in users_to_add:
    if user["emailUser"] in existing_emails:
        print(f"⛔️ Email already exists: {user['emailUser']} — skipping.")
        continue
    users_collection.insert_one(user)
    print(f"✅ Added user: {user['emailUser']}")


