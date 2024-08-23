from typing import Text
import flet as ft


def create_page(page: ft.Page) -> list[Text]:
    """
    Create the product details page view based on the product name in the route.

    :param page: An instance of ft.Page to create the product details page for.
    :return: A list of Flet controls for the product details page.
    """
    try:
        name = page.route.split('/products/')[1]
        description = f"This is a brief description of {name}."
        return [
            description,
            ft.Text(f"Product: {name}", size=25, weight=ft.FontWeight.BOLD),
        ]
    except IndexError:
        return [ft.Text(
            "Product not found.", size=25, weight=ft.FontWeight.BOLD
        )]
