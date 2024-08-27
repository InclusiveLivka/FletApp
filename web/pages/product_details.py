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
    name, price, description, category, encoded_image = engine.read_data_of_name(name_link)[
        0]
    if encoded_image == error_image.image_scr:
        encoded_image = error_image.image_scr_detalis
    window = ft.Column(controls=[
        ft.Container(
            content=ft.Image(src_base64=encoded_image
                             , fit=ft.ImageFit.SCALE_DOWN,
                             border_radius=30),
            width=389,
            height=200,
            border_radius=30,
            bgcolor=ft.colors.GREY_900,
            shadow=UIConstants.BOX_SHADOW
            
        ),

    ])
    return [window]
