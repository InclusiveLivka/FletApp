import logging
import flet as ft
from web.ui.elements import UIConstants
from web import routes
from web.database.engine import read_names_products
from web.database.actions import load_categories, load_products

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def handle_submit_search_bar(e, search_bar: ft.SearchBar):
    """
    Handles search bar submit action.

    :param e: Event object.
    :param search_bar: The search bar object.
    """
    logger.info(f"Search submitted: {search_bar.value}")


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
    logger.info(f"Search query: {search_query}")

    if search_query:
        for name in read_names_products():  # Replace with actual product list
            if search_query in str(name).lower():
                if len(filtered_list.controls) < 3:
                    link_name = str(name[0])
                    
                    filtered_list.controls.append(
                        ft.ListTile(
                            title=ft.Text(link_name),
                            on_click=lambda e: routes.go_products(page=page, name=link_name),
                        ))
    page.update()



def create_page(page: ft.Page):
    """
    Create the home page view with a search bar, add product button,
    categories, and products.

    :param page: An instance of ft.Page to create the home page for.
    :return: A list of Flet controls for the home page.
    """

    search_bar = ft.SearchBar(
        view_elevation=2,
        on_submit=handle_submit_search_bar,
        bar_leading=ft.Icon(ft.icons.SEARCH),
    )
    search_bar.on_change = lambda e: handle_change_search_bar(
        e, search_bar, filtered_list, page
    )
    filtered_list

    button_add_product = ft.ElevatedButton(
        text="Add product",
        on_click=lambda e: page.go('/categoryadd'),
    )

    categories = load_categories()
    products = load_products()

    return [button_add_product, search_bar, filtered_list, categories, products]
