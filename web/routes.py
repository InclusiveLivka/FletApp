import flet as ft
from ui_elements import create_home_page, create_product_add_page, create_category_add_page, create_product_details, create_category_details
from database_actions import reload_data

def setup_routes(page: ft.Page):
    def route_change(route):
        page.views.clear()

        if page.route == '/home':
            view_controls = create_home_page(page)
        elif page.route.startswith('/products/'):
            view_controls = create_product_details(page)
        elif page.route.startswith('/categories/'):
            view_controls = create_category_details(page)
        elif page.route == '/productadd':
            view_controls = create_product_add_page(page)
        elif page.route == '/categoryadd':
            view_controls = create_category_add_page(page)

        page.views.append(
            ft.View(
                route,
                view_controls,
                scroll="adaptive",
            )
        )
        page.update()

    def go_home(e):
        reload_data(page)  # Перезагружаем данные из базы данных
        page.route = '/home'
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = lambda view: page.go(page.views[-1].route)
