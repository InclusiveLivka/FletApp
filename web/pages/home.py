import logging
import flet as ft


from web import routes
from web.ui.elements import UIConstants
from web.database.engine import read_names_products
from web.database.actions import load_products, load_categories

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

filtered_list = ft.Column()


def handle_change_search_bar(
    e, search_bar: ft.SearchBar,
    filtered_list: ft.Column,
    page: ft.Page
) -> None:
    """
    Handles search bar input changes.

    :param e: Event object.
    :param search_bar: The search bar object.
    :param filtered_list: The filtered results container.
    :param page: The Flet page object.
    """
    search_query = search_bar.value.lower()
    filtered_list.controls.clear()  # Clear previous results

    if search_query:
        for name in read_names_products():  # Replace with actual product list
            if search_query in str(name).lower():
                if len(filtered_list.controls) < 3:
                    link_name = str(name[0])

                    filtered_list.controls.append(
                        ft.ListTile(
                            title=ft.Text(link_name),
                            on_click=lambda e: routes.go_products(
                                page=page, name=link_name),
                        ))
    page.update()


def create_page(page: ft.Page):
    """
    Create the home page view with a search bar, add product button,
    categories, and products.

    :param page: An instance of ft.Page to create the home page for.
    :return: A list of Flet controls for the home page.
    """
    page.clean()

    search_bar = ft.SearchBar(
        view_elevation=2,
        on_change=handle_change_search_bar,
        bar_leading=ft.Icon(ft.icons.SEARCH),
        width=399
    )
    search_bar.on_change = lambda e: handle_change_search_bar(
        e, search_bar, filtered_list, page)

    categories = load_categories(page)

    products = load_products(page)

    return [
        search_bar,
        filtered_list,
        UIConstants.CATEGORY_TEXT,
        categories,
        UIConstants.PRODUCTS_TEXT,
        products,
    ]
