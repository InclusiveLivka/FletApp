import sqlite3
import logging
import transliterate
import os

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Путь к базе данных
os.makedirs("database", exist_ok=True)
DB_PATH = os.path.join("database", "data.db")

# SQL-запросы для создания таблиц
create_categories_table_query = """
CREATE TABLE IF NOT EXISTS categories
(
    name TEXT NOT NULL UNIQUE,
    name_link TEXT NOT NULL UNIQUE,
    encoded_image BLOB NOT NULL
)
"""

create_products_table_query = """
CREATE TABLE IF NOT EXISTS products
(
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    encoded_image BLOB NOT NULL
)
"""

# Инициализация базы данных


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(create_categories_table_query)
        cur.execute(create_products_table_query)
        conn.commit()

# Добавление категории


def add_category(name, name_link, encoded_image):
    with sqlite3.connect(DB_PATH) as conn:
        name_link.replace(' ', '%20')
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO categories(name, name_link, encoded_image) VALUES (?, ?, ?)", (name, name_link, encoded_image))
        conn.commit()

# Добавление продукта


def add_product(name, price, description, category_name, encoded_image):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # Проверка существования категории
        cur.execute("SELECT name_link FROM categories WHERE name_link = ?",
                    (category_name,))
        if cur.fetchone():
            cur.execute(
                "INSERT INTO products(name, price, description, category, encoded_image) VALUES (?, ?, ?, ?, ?)",
                (name, price, description, category_name, encoded_image),
            )
            conn.commit()
        else:
            logger.error(
                f"Category '{category_name}' not found. Product '{name}' not added.")

# Чтение категорий


def read_categories():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM categories")
        categories = cur.fetchall()
    return categories

# Чтение продуктов конкретной категории


def read_products_of_category(category_name):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE category = ?",
                    (category_name,))
        products = cur.fetchall()
    return products

# Чтение всех продуктов


def read_products():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()
    return products


def read_name_and_encoded_image_product():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, encoded_image FROM products")
        products = cur.fetchall()
    return products


def read_names_products():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM products")
        products = cur.fetchall()
    return products
# Инициализация базы данных и добавление данных


def read_data_of_name(name):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE name = ?", (name,))
        data_products = cur.fetchall()
    return data_products


def delete_product(name):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM products WHERE name = ?", (name,))
        conn.commit()


def delete_category_and_products(category_name):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM products WHERE category = ?",
                    (category_name,))
        cur.execute("DELETE FROM categories WHERE name_link = ?", (category_name,))
        conn.commit()


def read_link_of_name_category(name):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name_link FROM categories WHERE name = ?", (name,)) 
        link = cur.fetchone()
        return link
    