from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

# Подключение к MongoDB Atlas
username = quote_plus('reyget')
password = quote_plus('xPCTVF6:3u,b=qn')
uri = "mongodb+srv://new_user:new_password@cluster0.byc49.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Создание клиента и подключение
client = MongoClient(uri, server_api=ServerApi('1'), tls=False)

try:
    db = client['LibraryProject']
    print(f"✅ База даних {db.name} успішно створена")

    # Создание коллекций
    authors_collection = db['Authors']
    categories_collection = db['Categories']
    books_collection = db['Books']
    users_collection = db['Users']
    histories_collection = db['Histories']

    print(f"✅ Документи даних {authors_collection.name}, {categories_collection.name}, {books_collection.name}, {users_collection.name}, {histories_collection.name} успішно створені")

    # Создание индексов
    users_collection.create_index("emailUser", unique=True)
    categories_collection.create_index("nameCategory", unique=True)

    # Вставка авторов
    authors_data = [
        {"nameAuthor": "George", "surnameAuthor": "Orwell"},
        {"nameAuthor": "J.K.", "surnameAuthor": "Rowling"},
        {"nameAuthor": "Stephen", "surnameAuthor": "King"},
        {"nameAuthor": "Jane", "surnameAuthor": "Austen"}
    ]
    authors_result = authors_collection.insert_many(authors_data)

    # Вставка категорий
    categories_data = [
        {"nameCategory": "Child"},
        {"nameCategory": "Adults"},
        {"nameCategory": "Horror"},
        {"nameCategory": "Classic"},
        {"nameCategory": "Fantasy"},
        {"nameCategory": "Thriller"},
        {"nameCategory": "Mystery"},
        {"nameCategory": "Romance"}
    ]
    categories_result = categories_collection.insert_many(categories_data)

    # Вставка пользователей
    users_data = [
        {"nameUser": "Admin", "surnameUser": "Admin", "passwordUser": "password", "is_admin": True, "emailUser": "Admin@gmail.com"}
    ]
    users_result = users_collection.insert_many(users_data)

    # Вставка книг (теперь с корректными id категорий и авторов)
    books_data = [
        {"nameBook": "The Shining", "yearBook": 1977, "availableBook": 3, "category_id": categories_result.inserted_ids[2], "author_id": authors_result.inserted_ids[0]},
        {"nameBook": "Harry Potter", "yearBook": 1997, "availableBook": 7, "category_id": categories_result.inserted_ids[4], "author_id": authors_result.inserted_ids[1]},
        {"nameBook": "Disappearance", "yearBook": 1998, "availableBook": 2, "category_id": categories_result.inserted_ids[5], "author_id": authors_result.inserted_ids[2]},
        {"nameBook": "Pride and Prejudice", "yearBook": 1813, "availableBook": 12, "category_id": categories_result.inserted_ids[3], "author_id": authors_result.inserted_ids[3]},
        {"nameBook": "Another Book", "yearBook": 2000, "availableBook": 4, "category_id": categories_result.inserted_ids[1], "author_id": authors_result.inserted_ids[1]}
    ]
    books_result = books_collection.insert_many(books_data)

    # Вставка истории аренды книг
    histories_data = [
        {"user_id": users_result.inserted_ids[0], "books_id": books_result.inserted_ids[0], "dateLoan": "2024-02-24T12:00:00", "dateReturn": None, "isReturned": False},
        {"user_id": users_result.inserted_ids[0], "books_id": books_result.inserted_ids[1], "dateLoan": "2024-02-20T12:00:00", "dateReturn": "2024-02-22T12:00:00", "isReturned": True}
    ]
    histories_collection.insert_many(histories_data)

    # Вывод подтверждения вставки данных
    print("✅ Введені автори:", list(authors_collection.find({}, {"_id": 0})))
    print("✅ Введені категорії:", list(categories_collection.find({}, {"_id": 0})))
    print("✅ Введені книжки:", list(books_collection.find({}, {"_id": 0})))
    print("✅ Введені користувачі:", list(users_collection.find({}, {"_id": 0})))
    print("✅ Введені записи історії:", list(histories_collection.find({}, {"_id": 0})))

except Exception as e:
    print(f"❌ Виникла помилка: {e}")
