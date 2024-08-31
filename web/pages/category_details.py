from web.ui import elements
from web.database.actions import create_product

from web.database import engine
import flet as ft


def create_page(page: ft.Page) -> list[ft.Control]:
    """
    Create the category details page view based on the category name in the
    route.

    :param page: An instance of ft.Page to create the category details page 
    for.
    :return: A list of Flet controls for the category details page.
    """
    try:
        category = page.route.split('/categories/')[1]
    except IndexError:
        return [
            ft.Text(
                "Category not found.", size=25, weight=ft.FontWeight.BOLD
            )
        ]

    window = ft.Column(
        controls=[
            ft.Container(
                content=ft.Text(
                    f"Все товары в категории: {engine.read_name_of_link_category(category)[0]}",
                    size=15,
                    color=ft.colors.WHITE,
                ),
                alignment=ft.Alignment(0, 0),
            
        width=399,
        height=50,
        border_radius=30,
        bgcolor=ft.colors.GREY_900,
        shadow=elements.UIConstants.BOX_SHADOW,
    )])

    for el in engine.read_products_of_category(category):
        name, price, currency, description, category, encoded_image = el
        list_of_product = create_product(name, encoded_image, currency, price, page)
        window.controls.append(list_of_product)
    return [window]
