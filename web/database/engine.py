import sqlite3
import logging
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
def add_category(name, encoded_image):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO categories(name, encoded_image) VALUES (?, ?)", (name, encoded_image))
        conn.commit()

# Добавление продукта
def add_product(category_name, name, price, description, encoded_image):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # Проверка существования категории
        cur.execute("SELECT name FROM categories WHERE name = ?", (category_name,))
        if cur.fetchone():
            cur.execute(
                "INSERT INTO products(name, price, description, category, encoded_image) VALUES (?, ?, ?, ?, ?)",
                (name, price, description, category_name, encoded_image),
            )
            conn.commit()
        else:
            logger.error(f"Category '{category_name}' not found. Product '{name}' not added.")

# Чтение категорий
def read_categories():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM categories")
        categories = cur.fetchall()
    return categories

# Чтение продуктов конкретной категории
def read_products_of_category(category_name):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE category = ?", (category_name,))
        products = cur.fetchall()
    return products

# Чтение всех продуктов
def read_products():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()
    return products

# Инициализация базы данных и добавление данных
add_category('яблоки',1)
