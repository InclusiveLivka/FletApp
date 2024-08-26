from typing import Text
import flet as ft
from web.database import engine



def create_page(page: ft.Page) -> list[Text]:
    """
    Create the product details page view based on the product name in the route.

    :param page: An instance of ft.Page to create the product details page for.
    :return: A list of Flet controls for the product details page.
    """
    
    name = page.route.split("/products/")[1]
    name_data = engine.read_data_of_name(name)[0]
    window = ft.Column(controls=[
            ft.Text(f"Product: {name}", size=20, color=ft.colors.WHITE),
            ft.Text(f"Price: {name_data[1]}", size=20, color=ft.colors.WHITE),
            ft.Text(f"Description: {name_data[2]}",
                    size=20, color=ft.colors.WHITE),
            ft.Text(f"Category: {name_data[3]}",
                    size=20, color=ft.colors.WHITE),
        ])
    return [window]
