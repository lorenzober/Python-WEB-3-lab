from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

# Подключение
username = quote_plus("reyget")
password = quote_plus("xPCTVF6:3u,b=qn")
uri = "mongodb+srv://elisaberaudolive:gF4FLZh6NFuYaI01@cluster0.ufxtqwi.mongodb.net/?retryWrites=true&w=majority&appName=PythonWEB"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['LibraryProject']

# Очистим коллекции для чистоты
db.Authors.delete_many({})
db.Categories.delete_many({})
db.Books.delete_many({})
db.Users.delete_many({})
db.Histories.delete_many({})

# Добавим авторов
authors_data = [
    {"nameAuthor": "George", "surnameAuthor": "Orwell"},
    {"nameAuthor": "J.K.", "surnameAuthor": "J.K. Rowling"},
    {"nameAuthor": "Stephen", "surnameAuthor": "King"},
    {"nameAuthor": "Jane", "surnameAuthor": "Austen"}
]
author_ids = db.Authors.insert_many(authors_data).inserted_ids

# Добавим категории
categories_data = [
    {"nameCategory": "Child"},
    {"nameCategory": "Adults"},
    {"nameCategory": "Horror"},
    {"nameCategory": "Classic"}
]
category_ids = db.Categories.insert_many(categories_data).inserted_ids

print("✅ Додано батьківські елементи")

# Добавим книги (используем ObjectId из авторов и категорий)
books_data = [
    {"nameBook": "The Shining", "yearBook": 1977, "availableBook": 3, "category_id": category_ids[2], "author_id": author_ids[2]},
    {"nameBook": "Harry Potter", "yearBook": 1997, "availableBook": 7, "category_id": category_ids[0], "author_id": author_ids[1]},
    {"nameBook": "Disappearance", "yearBook": 1998, "availableBook": 2, "category_id": category_ids[1], "author_id": author_ids[2]},
    {"nameBook": "Pride and Prejudice", "yearBook": 1813, "availableBook": 12, "category_id": category_ids[3], "author_id": author_ids[3]},
    {"nameBook": "Another Book", "yearBook": 2000, "availableBook": 4, "category_id": category_ids[2], "author_id": author_ids[1]}
]
db.Books.insert_many(books_data)

# Добавим пользователя
user_data = {
    "nameUser": "Admin",
    "surnameUser": "Admin",
    "passwordUser": "password",
    "is_admin": True,
    "emailUser": "Admin@gmail.com"
}
db.Users.insert_one(user_data)

print("✅ Додано дитячі елементи з референсом")
