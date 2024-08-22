import flet as ft
import file_handling
import my_web_elements
import os
import database.engine as engine
import base64
from typing import List, Optional

route_page = None

os.environ["FLET_SECRET_KEY"] = os.urandom(12).hex()


def main(page: ft.Page):
    global route_page
    route_page = page

    page.title = "Shop_constructor"
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 399
    page.window_height = 629
    page.window_max_height = 629
    page.window_max_width = 399
    page.scroll = ft.ScrollMode.HIDDEN
    page.theme = ft.Theme(color_scheme_seed=ft.colors.DEEP_PURPLE)
    page.update()

    selected_description = ft.Text("")  # Текстовое поле для краткого описания


    def handle_file_upload(file_picker, page):
        pass

    file_picker = ft.FilePicker(
        on_result=lambda _: handle_file_upload(file_picker, page)
    )
    page.overlay.append(file_picker)

    def add_new_category(category):
        engine.add_category(category)

    page_category_add = ft.Container(
        content=ft.Column(
            controls=[
                my_web_elements.category_name,
                ft.Row(
                    controls=[ft.FloatingActionButton(
                        text="Добавить категорию", width=150, on_click=lambda e: add_new_category(my_web_elements.category_name.value)), ft.FloatingActionButton(text="Далее", on_click=lambda _: page.go('/productadd'))],
                )
            ]))

    page_product_add = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Product add"),
                my_web_elements.name_product,
                my_web_elements.price_product,
                my_web_elements.description_product,
                my_web_elements.category_product,
                ft.Row(
                    controls=[ft.FloatingActionButton(
                        text="Добавить продукт", width=150, on_click=lambda e: add_new_product(my_web_elements.name_product.value, my_web_elements.price_product.value, my_web_elements.description_product.value, my_web_elements.category_product.value,my_web_elements.encoded_image.value)), ft.FloatingActionButton(icon=ft.icons.IMAGE, on_click=lambda _: file_picker.pick_files())],
                ),
                my_web_elements.encoded_image,
            ]))

    def add_new_product(name, price, description, category,encoded_image):
        engine.add_product(name, price, description, category,encoded_image)
        print("Товар добавлен в базу данных")

    button_add_product = ft.ElevatedButton(
        text="Add product",
        on_click=lambda e: page.go('/categoryadd'),
    )

    def handle_change_search_bar(e):
        search_query = search_bar.value.lower()
        filtered_list.controls.clear()  # Очистка предыдущих результатов
        if search_query:
            for name in my_web_elements.names:
                if search_query in name.lower():
                    if filtered_list.controls.__len__() < 3:
                        filtered_list.controls.append(
                            ft.ListTile(title=ft.Text(name), on_click=lambda e, link_name=name: page.go(f'/products/{link_name}')))
        page.update()

    def handle_submit_search_bar(e):
        print("Search submitted:", search_bar.value)

    # Контейнер для отображения отфильтрованных имен
    filtered_list = ft.Column()

    # Создание SearchBar
    search_bar = ft.SearchBar(
        view_elevation=2,
        on_change=handle_change_search_bar,
        on_submit=handle_submit_search_bar,
        bar_leading=ft.Icon(ft.icons.SEARCH),
    )

    items_product = []
    for name in my_web_elements.names:
        items_product.append(ft.Container(
            content=ft.Text(name, size=50, opacity=0.5),
            alignment=ft.alignment.center,
            width=399,
            height=100,
            border_radius=30,
            shadow=my_web_elements.all_shadow,
            bgcolor=ft.colors.BLACK,
            on_click=lambda e, link_name=name: page.go(
                f'/products/{link_name}'),
        ))

    products = ft.Container(
        content=ft.Column(controls=items_product),
        padding=10,
        margin=0,
    )

    items_categories = []
    for i in engine.read_categories():
        items_categories.append(ft.Container(
            content=ft.Stack(controls=[
                ft.Image(src="https://img.freepik.com/free-photo/the-adorable-illustration-of-kittens-playing-in-the-forest-generative-ai_260559-483.jpg?size=338&ext=jpg&ga=GA1.1.2008272138.1724025600&semt=ais_hybrid",
                         width=200,
                         height=200,

                         ),
                ft.Container(
                    content=ft.Text(
                        i[0], size=20, color=ft.colors.BACKGROUND, style=ft.TextThemeStyle.DISPLAY_LARGE),
                    alignment=ft.Alignment(0, 0),

                    on_click=lambda e, category=i: page.go(
                        f'/categories/{category[0]}'),



                )]),


            alignment=ft.alignment.center,
            width=150,
            height=150,
            bgcolor=ft.colors.BLACK,
            border_radius=30,
            shadow=my_web_elements.all_shadow,
        ))

    categories = ft.Container(
        ft.Row(controls=items_categories, scroll=True, height=200, width=399,
               spacing=15, tight=100, vertical_alignment=ft.alignment.center),
        height=200,
        width=399,
        margin=0,
        padding=0
    )

    def route_change(route):
        page.views.clear()

        view_controls = []
        if page.route == '/home':
            view_controls = [
                button_add_product,
                search_bar,
                filtered_list,
                categories,
                products,
            ]
        elif page.route.startswith('/products/'):
            # Проверяем и извлекаем имя товара
            try:
                name = page.route.split('/products/')[1]
                # Пример краткого описания
                description = f"This is a brief description of {name}."
                selected_description.value = description  # Обновляем описание
                view_controls = [
                    selected_description,
                    ft.Text(f"Product: {name}", size=25,
                            weight=ft.FontWeight.BOLD),
                ]
            except IndexError:
                view_controls = [
                    ft.Text("Product not found.", size=25,
                            weight=ft.FontWeight.BOLD),
                ]
        elif page.route.startswith('/categories/'):
            try:
                category = page.route.split('/categories/')[1]
                # Пример краткого описания
                selected_description.value = f"This is the {category} category."
                view_controls = [
                    selected_description,
                    ft.Text(f"Category: {category}", size=25,
                            weight=ft.FontWeight.BOLD),
                ]
            # Пример краткого описания для категорий
            except IndexError:
                view_controls = [
                    selected_description,
                    ft.Text("Category not found.", size=25,
                            weight=ft.FontWeight.BOLD),
                ]

        elif page.route == '/productadd':
            view_controls = [page_product_add]
        elif page.route == '/categoryadd':
            view_controls = [page_category_add]
        # Добавляем кнопку "Home" на все страницы, кроме главной
        if page.route != '/home':
            search_bar.value = ''
            view_controls.append(
                ft.CupertinoNavigationBar(
                    destinations=[
                        ft.NavigationBarDestination(
                            icon=ft.icons.HOME,
                            label="На главную",
                            bgcolor=ft.colors.PURPLE_200
                        )
                    ], on_change=go_home
                )


            )

        # Обновляем содержимое страницы
        page.views.append(
            ft.View(
                route,
                view_controls,
                scroll="adaptive",
            )
        )
        page.update()  # Прямо вызываем обновление страницы

    def go_home(e):
        page.route = '/home'
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    go_home(None)
    


ft.app(target=main, upload_dir="images", view=ft.WEB_BROWSER)
