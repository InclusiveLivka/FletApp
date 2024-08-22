import flet as ft
import database.engine as engine
from main import route_page


all_categories = engine.read_categories()
names = ['product']

colors_dict = {
    "shadow": ft.colors.PURPLE_ACCENT,
}

all_shadow = ft.BoxShadow(
    spread_radius=0.2,
    blur_radius=10,
    color=colors_dict["shadow"],
    offset=ft.Offset(0, 2.5),
    blur_style=ft.ShadowBlurStyle.SOLID,)


encoded_image = ft.TextField(value='1',opacity=1.0)
name_product = ft.TextField(label="Name")
price_product = ft.TextField(label="Price")
description_product = ft.TextField(label="Description")
category_product = ft.Dropdown(label="Categories", options=[
        ft.dropdown.Option(category[0]) for category in engine.read_categories()])

category_name = ft.TextField(
        label="Название категории",
        width=300,
        height=40,
        autofocus=True,
    )

print (route_page)


