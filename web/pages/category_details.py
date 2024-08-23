from typing import Text
import flet as ft


def create_page(page: ft.Page) -> list[Text]:
    """
    Create the category details page view based on the category name in the
    route.

    :param page: An instance of ft.Page to create the category details page 
    for.
    :return: A list of Flet controls for the category details page.
    """
    try:
        category = page.route.split('/categories/')[1]
        description = f"This is the {category} category."
        return [
            description,
            ft.Text(f"Category: {category}", size=25,
                    weight=ft.FontWeight.BOLD),
        ]
    except IndexError:
        return [ft.Text(
            "Category not found.", size=25, weight=ft.FontWeight.BOLD
        )]
