import flet as ft
import os

from web.database import engine
from web.ui.error_image import image_scr
from dotenv import load_dotenv, find_dotenv

currency = [
    'usd',
    'byn',
    'rub',
    'eur',
    'uah',
]

class UIConstants:
    """
    Class to hold constant values used in the UI.
    """
    
    load_dotenv(find_dotenv())
    ADMIN_LINK = os.getenv('ADMIN_LINK')

    COLORS = {
        # Color used for the shadow
        "shadow": ft.colors.BLACK87,
    }

    BOX_SHADOW = ft.BoxShadow(
        # Spread radius of the shadow
        spread_radius=0.2,
        # Blur radius of the shadow
        blur_radius=10,
        # Color of the shadow
        color=COLORS["shadow"],
        # Offset of the shadow
        offset=ft.Offset(0, 2.5),
        # Blur style of the shadow
        blur_style=ft.ShadowBlurStyle.SOLID
    )

    # Assuming the default value and other initializations
    ENCODED_IMAGE_CATEGORY = ft.TextField(
        # Initial value of the image
        value=image_scr,
        # Opacity of the image
        opacity=0,
        # Read-only flag
        read_only=True
    )

    ENCODED_IMAGE_PRODUCT = ft.TextField(
        # Initial value of the image
        value=image_scr,
        # Opacity of the image
        opacity=0,
        # Read-only flag
        read_only=True
    )

    NAME_PRODUCT = ft.TextField(
        # Label of the field
        label="Название",
        # Width of the field
        width=399
    )

    PRICE_PRODUCT = ft.TextField(
        # Label of the field
        label="Цена",
        # Width of the field
        width=294
    )

    DESCRIPTION_PRODUCT = ft.TextField(
        # Label of the field
        label="Описание",
        # Width of the field
        width=399,
        # Multiline flag
        multiline=True
    )

    CATEGORY_NAME_FIELD = ft.TextField(
        # Label of the field
        label="Название категории",
        # Width of the field
        width=399,
        # Height of the field
        height=40,
        # Autofocus flag
        autofocus=True,
    )

    CATEGORY_NAME = ft.Dropdown(
        # Label of the field
        label="Категория",
        # Width of the field
        width=399,
        # Options of the dropdown
        options=[
            ft.dropdown.Option(category[0]) for category in engine.read_categories()
        ]
    )

    DELETE_CATEGORY_FIELD = ft.Dropdown(
        # Label of the field
        label="Выберите категорию для удаления",
        # Width of the field
        width=399,
        # Options of the dropdown
        options=[
            ft.dropdown.Option(category[0]) for category in engine.read_categories()
        ]
    )

    DELETE_PRODUCT_FIELD = ft.Dropdown(
        # Label of the field
        label="Выберите продукт",
        # Width of the field
        width=399,
        # Options of the dropdown
        options=[ft.dropdown.Option(product[0])
                 for product in engine.read_products()]
    )

    CHEKBOX = ft.Checkbox(
        # Label of the field
        label="Возвращать на главную?",
        # Value of the field
        value=False
    )

    CURRENCY_FIELD = ft.Dropdown(
        # Initial value of the field
        value="usd",
        # Label of the field
        label="Валюта",
        # Width of the field
        width=94,
        # Options of the dropdown
        options=[
            ft.dropdown.Option(currency[i]) for i in range(len(currency))
        ]
    )
    
    CATEGORY_TEXT = ft.Container(
        content=ft.Text(value="Категории", size=20, weight=10),
        alignment=ft.Alignment(0, -0.5),
        width=399,
        height=50,
        opacity=0.5,
        padding=0
    )
    PRODUCTS_TEXT = ft.Container(
        content=ft.Text(value=" Товары", size=20, weight=10),
        alignment=ft.Alignment(0, -0.5),
        width=399,
        height=50,
        opacity=0.5,
        padding=0
    )


