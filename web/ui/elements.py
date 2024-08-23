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
    ENCODED_IMAGE = ft.TextField(value='1', opacity=1.0)
    NAME_PRODUCT = ft.TextField(label="Name")
    PRICE_PRODUCT = ft.TextField(label="Price")
    DESCRIPTION_PRODUCT = ft.TextField(label="Description")

    @staticmethod
    def get_category_dropdown_options() -> List[ft.dropdown.Option]:
        """
        Get dropdown options for categories.

        :return: List of Flet dropdown options for categories.
        """
        categories = engine.read_categories()
        return ft.Dropdown(
            label="Categories", options=[
                ft.dropdown.Option(category[0]) for category in categories
            ]
        )

    CATEGORY_NAME_FIELD = ft.TextField(
        label="Название категории",
        width=300,
        height=40,
        autofocus=True,
    )
