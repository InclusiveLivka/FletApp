import flet as ft
from web.database import engine
from typing import List
from web.ui.error_image import image_scr, image_scr_detalis

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
    COLORS = {
        "shadow": ft.colors.BLACK87,
    }

    BOX_SHADOW = ft.BoxShadow(
        spread_radius=0.2,
        blur_radius=10,
        color=COLORS["shadow"],
        offset=ft.Offset(0, 2.5),
        blur_style=ft.ShadowBlurStyle.SOLID
    )

    # Assuming the default value and other initializations
    ENCODED_IMAGE_CATEGORY = ft.TextField(
        value=image_scr, opacity=0, read_only=True)
    ENCODED_IMAGE_PRODUCT = ft.TextField(
        value=image_scr, opacity=0, read_only=True)
    NAME_PRODUCT = ft.TextField(label="Название", width=399)
    PRICE_PRODUCT = ft.TextField(label="Цена", width=259)
    DESCRIPTION_PRODUCT = ft.TextField(
        label="Описание", width=399, multiline=True)

    CATEGORY_NAME_FIELD = ft.TextField(
        label="Название категории",
        width=399,
        height=40,
        autofocus=True,
    )

    CATEGORY_NAME = ft.Dropdown(
        label="Категория",
        width=399,
        options=[
            ft.dropdown.Option(category[0]) for category in engine.read_categories()
        ]
    )
    DELETE_CATEGORY_FIELD = ft.Dropdown(
        label="Выберите категорию для удаления",
        width=399,
        options=[
            ft.dropdown.Option(category[0]) for category in engine.read_categories()
        ]
    )

    DELETE_PRODUCT_FIELD = ft.Dropdown(
        label="Выберите продукт",
        width=399,
        options=[ft.dropdown.Option(product[0])
                 for product in engine.read_products()]
    )

    CHEKBOX = ft.Checkbox(label="Возвращать на главную.", value=False)

    CURRENCY_FIELD = ft.Dropdown(
        value="USD",
        label="валюта",
        width=94,
        options=[
            ft.dropdown.Option(currency[i]) for i in range(len(currency))
            
        ]
    )

