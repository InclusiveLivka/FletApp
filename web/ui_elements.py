import flet as ft
from database_actions import load_categories, load_products
import database.engine as engine



def create_home_page(page: ft.Page):
    search_bar = ft.SearchBar(
        view_elevation=2,
        on_change=lambda e: handle_change_search_bar(e, page),
        on_submit=lambda e: handle_submit_search_bar(e, page),
        bar_leading=ft.Icon(ft.icons.SEARCH),
    )

    button_add_product = ft.ElevatedButton(
        text="Add product",
        on_click=lambda e: page.go('/categoryadd'),
    )

    categories = load_categories(page)
    products = load_products(page)

    return [button_add_product, search_bar, categories, products]

def create_product_add_page(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Product add"),
                ft.TextField(label="Name"),
                ft.TextField(label="Price"),
                ft.TextField(label="Description"),
                ft.Dropdown(label="Categories", options=[
                    ft.dropdown.Option(category[0]) for category in engine.read_categories()]),
                ft.Row(
                    controls=[ft.FloatingActionButton(
                        text="Добавить продукт", width=150), ft.FloatingActionButton(icon=ft.icons.IMAGE, on_click=lambda _: file_picker.pick_files())],
                )
            ]))

def create_category_add_page(page: ft.Page):
    category_name = ft.TextField(
        label="Название категории",
        width=300,
        height=40,
        autofocus=True,
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                category_name,
                ft.Row(
                    controls=[ft.FloatingActionButton(
                        text="Добавить категорию", width=150, on_click=lambda e: engine.add_category(category_name.value)),
                        ft.FloatingActionButton(text="Далее", on_click=lambda _: page.go('/productadd'))],
                )
            ]))

def create_product_details(page: ft.Page):
    try:
        name = page.route.split('/products/')[1]
        description = f"This is a brief description of {name}."
        return [
            ft.Text(description),
            ft.Text(f"Product: {name}", size=25, weight=ft.FontWeight.BOLD),
        ]
    except IndexError:
        return [ft.Text("Product not found.", size=25, weight=ft.FontWeight.BOLD)]

def create_category_details(page: ft.Page):
    try:
        category = page.route.split('/categories/')[1]
        description = f"This is the {category} category."
        return [
            ft.Text(description),
            ft.Text(f"Category: {category}", size=25, weight=ft.FontWeight.BOLD),
        ]
    except IndexError:
        return [ft.Text("Category not found.", size=25, weight=ft.FontWeight.BOLD)]
