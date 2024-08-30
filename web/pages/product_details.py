from typing import Text
import flet as ft
from web.database import engine
from web.ui.elements import UIConstants
from web.ui import error_image


def create_page(page: ft.Page) -> list[Text]:
    """
    Create the product details page view based on the product name in the route.

    :param page: An instance of ft.Page to create the product details page for.
    :return: A list of Flet controls for the product details page.
    """

    name_link = page.route.split("/products/")[1]
    name, price, currency, description, category, encoded_image = engine.read_data_of_name(name_link)[
        0]
    if encoded_image == error_image.image_scr:
        encoded_image = error_image.image_scr_detalis

    if description == '':
        description = "Описание отсутствует."
    else:
        description = (f"Описание товара: {description}")

    window = ft.Column(controls=[ft.Container(content=ft.FloatingActionButton(
        text=(f"Категория - {engine.read_name_of_link_category(category)[0]}"),
        width=389,
        bgcolor=ft.colors.GREY_900,
        on_click=lambda e: page.go(f"/categories/{category}"),
        
    ),
        shadow=UIConstants.BOX_SHADOW,
        border_radius=30,
        
    ),
        ft.Container(
            content=ft.Image(src_base64=encoded_image, fit=ft.ImageFit.SCALE_DOWN,
                             border_radius=30),
            width=389,
            height=200,
            border_radius=30,
            bgcolor=ft.colors.GREY_900,
            shadow=UIConstants.BOX_SHADOW,
    ),
        ft.Column(controls=[
            ft.Container(content=ft.Text(
                value=description,
            )),
            ft.Container(content=ft.Text(
                value=f"Цена: {price} {currency}",
            )),
            ft.Container(content=ft.FloatingActionButton(
                text="Купить",
                on_click=lambda e: print("Купить"),
                bgcolor=ft.colors.GREY_900,
                width=389,
                
            ),
            shadow=UIConstants.BOX_SHADOW,
            border_radius=30
                
            )
        ])])
    return [window]
