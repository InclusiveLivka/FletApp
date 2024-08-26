import flet as ft
from web.database import engine
from typing import List


class UIConstants:
    """
    Class to hold constant values used in the UI.
    """
    COLORS = {
        "shadow": ft.colors.PURPLE_ACCENT,
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
        value='0', opacity=0, read_only=True)
    ENCODED_IMAGE_PRODUCT = ft.TextField(
        value='0', opacity=0, read_only=True)
    NAME_PRODUCT = ft.TextField(label="Название", width=399)
    PRICE_PRODUCT = ft.TextField(label="Цена", width=399)
    DESCRIPTION_PRODUCT = ft.TextField(
        label="Описание", width=399, multiline=True)

    CATEGORY_NAME_FIELD = ft.TextField(
        label="Название категории",
        width=399,
        height=40,
        autofocus=True,
    )

    CATEGORY_NAME = ft.Dropdown(
        label="Категория (обязательно)",
        width=399,
        options=[
            ft.dropdown.Option(category[0]) for category in engine.read_categories()
        ]
    )
