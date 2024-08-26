import flet as ft
import logging

from web.pages.home import create_page as create_home_page
from web.pages.admin_home import create_page as create_admin_home_page
from web.pages.product_add import create_page as create_product_add_page
from web.pages.category_add import create_page as create_category_add_page
from web.pages.product_details import create_page as create_product_details
from web.pages.category_details import create_page as create_category_details

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def go_products(page: ft.Page, name: str):
    page.go(f'/products/{name}')
    
def go_categories(page: ft.Page, name: str):
    page.go(f'/categories/{name}')

async def get_view_controls(page: ft.Page):
    """
    Returns the list of controls for the given route.

    :param page: The Flet page object.
    :param route: The current route.
    :return: List of Flet controls.
    """
    if page.route == '/home':
        return create_home_page(page)
    elif page.route.startswith('/products/'):
        return create_product_details(page)
    elif page.route.startswith('/categories/'):
        return create_category_details(page)
    elif page.route == '/productadd':
        return [create_product_add_page(page)]
    elif page.route == '/categoryadd':
        return [create_category_add_page(page)]
    elif page.route == '/adminhome':
        return create_admin_home_page(page)
        

    return []


async def setup_routes(page: ft.Page):
    """
    Configures routes and view changes for the page.

    :param page: The Flet page object.
    """
    async def route_change(route):
        page.views.clear()
        view_controls = await get_view_controls(page)
        page.views.append(ft.View(route, view_controls, scroll="adaptive"))
        page.update()
        logger.info(f"Route changed to: {route}")

    def view_pop():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        logger.info(f"View popped to: {top_view.route}")

    # Если маршрут пустой, устанавливаем начальный маршрут как /home
    if not page.route or page.route == "/":
        logger.info("Initial route is empty. Navigating to /home.")
        page.route = '/home'
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    logger.info("Route setup completed")
