import logging
import flet as ft
from typing import List
from web.database import engine

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def reload_data(page: ft.Page) -> None:
    """
    Reload data from the database and update the page elements.

    :param page: An instance of ft.Page to update with new data.
    """
    logger.info("Starting data reload")

    # Обновляем данные и страницу
    update_page_with_data(page, load_categories(), load_products())

    logger.info("Data reload completed and page updated")


def update_page_with_data(
    page: ft.Page,
    categories_column: ft.Column,
    products_column: ft.Column
) -> None:
    """
    Update the page with new data.

    :param page: An instance of ft.Page to update.
    :param categories_column: An instance of ft.Column containing category
    items.
    :param products_column: An instance of ft.Column containing product items.
    """
    page.controls.clear()
    page.controls.append(categories_column)
    page.controls.append(products_column)
    page.update()


def load_categories() -> ft.Column:
    """
    Load categories from the database and return a Flet Column with category
    items.

    :return: An instance of ft.Column containing category items.
    """
    logger.info("Loading categories")
    items_categories = create_text_items(engine.read_categories(), "Category")
    logger.info(f"Loaded {len(items_categories)} categories")
    return ft.Column(controls=items_categories)


def load_products() -> ft.Column:
    """
    Load products from the database and return a Flet Column with product 
    items.

    :return: An instance of ft.Column containing product items.
    """
    logger.info("Loading products")
    items_product = create_text_items(engine.read_products(), "Product")
    logger.info(f"Loaded {len(items_product)} products")
    return ft.Column(controls=items_product)


def create_text_items(data: List[str], label: str) -> List[ft.Text]:
    """
    Create a list of Flet Text items from data.

    :param data: List of data to convert into text items.
    :param label: The label to prefix each text item with.
    :return: A list of Flet Text items.
    """
    return [ft.Text(
        f"{label}: {item}", size=20, color=ft.colors.WHITE
    ) for item in data]
