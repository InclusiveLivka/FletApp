import logging
import flet as ft
import transliterate
from typing import List
from web.database import engine
from web.ui import elements
from web.ui import error_image
from web import routes

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


categories = ft.Row()


def load_categories(page: ft.Page) -> ft.Row:
    """
    Load categories from the database and return a Flet Column with category
    items.

    :return: An instance of ft.Column containing category items.
    """
    logger.info("Loading categories")
    categories.controls.clear()
    for el in engine.read_categories():
        name, encoded_image = el
        category = create_category(name, encoded_image, page)
        categories.controls.append(category)
    return categories


def create_category(name, encoded_image, page: ft.Page) -> ft.Row:
    name = transliterate.translit(name, 'ru', reversed=False)
    """
    Create a list of Flet Text items from data.

    :param data: List of data to convert into text items.
    :param label: The label to prefix each text item with.
    :return: A list of Flet Text items.
    """
    if not name:
        return [ft.Text('Нет категорий', size=20, text_align=ft.TextAlign.CENTER)]
    else:
        if encoded_image == '0':
            encoded_image = error_image.image_scr
        name_link = transliterate.translit(name, reversed=True)
        return ft.Container(content=ft.Stack(
            controls=[
                ft.Image(
                    src_base64=encoded_image,
                    fit=ft.ImageFit.FILL,
                    width=100,
                    height=100
                ),
                ft.Container(content=ft.Text(
                    name,
                    size=10
                ),
                    alignment=ft.Alignment(0, 0),
                    bgcolor=ft.colors.BLACK87,
                    opacity=0.5,

                ),

            ]
        ),
            bgcolor=ft.colors.BLACK,
            width=100,
            height=100,
            border_radius=30,
            shadow=elements.UIConstants.BOX_SHADOW,
            on_click=lambda e: routes.go_categories(page, name_link),
            margin=10,
        )


products = ft.Column()


def load_products(page: ft.Page) -> ft.Column:
    """
    Load products from the database and return a Flet Column with product
    items.

    :return: An instance of ft.Column containing product items.
    """
    logger.info("Loading products")
    products.controls.clear()
    for el in engine.read_products():
        name, description, price, category, encoded_image = el
        list_of_product = create_product(name, encoded_image, page)
        products.controls.append(list_of_product)
    return products


def create_product(name, encoded_image, page: ft.Page) -> ft.Container:
    """
    Create a list of Flet Text items from data.

    :param data: List of data to convert into text items.
    :param label: The label to prefix each text item with.
    :return: A list of Flet Text items.
    """
    if not name:
        return [ft.Text('Нет товаров', size=20, text_align=ft.TextAlign.CENTER)]
    
    else:
        if encoded_image == '0':
            encoded_image = error_image.image_scr
        return ft.Container(content=ft.Stack(
            controls=[
                ft.Image(
                    src_base64=encoded_image,
                    width=399,
                    height=100,
                    fit=ft.ImageFit.FIT_WIDTH,
                    error_content=ft.Text('Нет изображения', size=20),

                ),
                ft.Container(content=ft.Text(
                    name,
                    size=20,

                ), alignment=ft.Alignment(0, 0),
                    bgcolor=ft.colors.BLACK87,
                    opacity=0.5,
                ),
            ]),
            bgcolor=ft.colors.BLACK,
            width=399,
            height=100,
            border_radius=30,
            shadow=elements.UIConstants.BOX_SHADOW,
            on_click=lambda e: routes.go_products(page, name),
            margin=10,
        )


products_in_category = ft.Column()


def load_products_of_category(page: ft.Page, name_link: str) -> None:
    # if engine.read_products_of_category(name) == []:
    #     return ft.Text("Эта категория пуста", size=20, text_align=ft.TextAlign.CENTER)
    # else:
    name = transliterate.translit(name_link, 'ru', reversed=False)

    products_in_category.controls.clear()
    products_in_category.controls.append(ft.Container(content=ft.Text(
        f"Все товары в ктегории {name}", size=20, color=ft.colors.WHITE)))
    for el in engine.read_products_of_category(name_link):
        name, description, price, category, encoded_image = el
        list_of_product = create_product(name, encoded_image, page)
        products_in_category.controls.append(list_of_product)
    return products_in_category
