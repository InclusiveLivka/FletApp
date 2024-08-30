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

    window = ft.Column(controls=[
        ft.Container(ft.Stack(controls=[ft.Container(
                width=389,
                height=300,
                bgcolor=ft.colors.BLACK54,
                border_radius=30,
                content=ft.Container(content=ft.Text(
            value=f"Цена: {price} {currency}",
            ),
            alignment=ft.Alignment(-0.9,0.9)
            ),
            ),
                                        ft.Container(
            content=ft.Image(
                src_base64=encoded_image,
                fit=ft.ImageFit.CONTAIN,
                border_radius=30
                
            ),
            width=379,
            height=250,
            border_radius=30,
            bgcolor=ft.colors.GREY_900,
            shadow=UIConstants.BOX_SHADOW,
            margin=5,
        )]),

        ),
        ft.Column(controls=[
            ft.Container(content=ft.Text(
                value=description,
            ),
                width=389,
                border_radius=25,
                bgcolor=ft.colors.GREY_900,
                shadow=UIConstants.BOX_SHADOW,
                padding=10
            ),

            ft.Container(content=ft.FloatingActionButton(
                text="Перейти к покупке",
                on_click=lambda e: print("Купить"),
                bgcolor=ft.colors.GREY_900,
                width=389,
            ),
                shadow=UIConstants.BOX_SHADOW,
                border_radius=25,
            ),
            ft.Container(content=ft.FloatingActionButton(
                text=(
                    f"Перейти в категорию - {engine.read_name_of_link_category(category)[0]}"),
                width=389,
                bgcolor=ft.colors.GREY_900,
                on_click=lambda e: page.go(f"/categories/{category}"),

            ),
                shadow=UIConstants.BOX_SHADOW,
                border_radius=25,

            ),
        ])])
    return [window]
