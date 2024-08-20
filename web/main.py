import flet as ft
from utilits import web_elements


def main(page: ft.Page):
    page.window_width = 399
    page.window_height = 629
    page.window_max_height = 629
    page.window_max_width = 399
    page.scroll = 'adaptive'
    page.theme = ft.Theme(color_scheme_seed=ft.colors.DEEP_PURPLE)
    page.update()

    page.add(ft.Column([web_elements.search_bar,web_elements.filtered_list]))
    page.add(web_elements.categories)
    page.add(web_elements.products)


ft.app(target=main,)
