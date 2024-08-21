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
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)"""

create_products_table_query = """
CREATE TABLE IF NOT EXISTS products
(   
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    description TEXT NOT NULL,
    encoded_image TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
)"""

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(create_categories_table_query)
    cur.execute(create_products_table_query)
    conn.commit()
    conn.close()

# Добавление категории
def add_category(name):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO categories(name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

# Добавление продукта
def add_product(category_name, name, price, description, encoded_image):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Получение id категории
    cur.execute("SELECT id FROM categories WHERE name = ?", (category_name,))
    category_id = cur.fetchone()

    if category_id:
        category_id = category_id[0]
        cur.execute(
            "INSERT INTO products(category_id, name, price, description, encoded_image) VALUES (?, ?, ?, ?, ?)",
            (category_id, name, price, description, encoded_image),
        )
        conn.commit()
    else:
        logger.error(f"Category '{category_name}' not found. Product '{name}' not added.")
    
    conn.close()

# Инициализация базы данных и добавление данных
init_db()

def read_categories():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM categories")
    categories = cur.fetchall()
    conn.close()
    return categories

def read_products_of_category(category):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE category_id = ?", (category,))
    products = cur.fetchall()
    conn.close()
    return products