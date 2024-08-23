import logging
import flet as ft
from web.database import engine
from web.ui.elements import UIConstants

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_new_category(category_name: str):
    """
    Adds a new category to the database.

    :param category_name: Name of the new category.
    """
    engine.add_category(category_name, 1)
    logger.info(f"New category added: {category_name}")


def create_page(page: ft.Page) -> ft.Container:
    """
    Create the category add page view with a field to add a new category.

    :param page: An instance of ft.Page to create the category add page for.
    :return: A Flet Container with controls for adding a category.
    """
    return ft.Container(
        content=ft.Column(
            controls=[
                UIConstants.CATEGORY_NAME_FIELD,
                ft.Row(
                    controls=[
                        ft.FloatingActionButton(
                            text="Добавить категорию",
                            width=150,
                            on_click=lambda e: add_new_category(
                                UIConstants.CATEGORY_NAME_FIELD.value)
                        ),
                        ft.FloatingActionButton(
                            text="Далее",
                            on_click=lambda _: page.go('/productadd')
                        )
                    ],
                )
            ]
        )
    )
