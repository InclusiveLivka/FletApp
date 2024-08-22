import database.engine as engine
import flet as ft

def reload_data(page):
    # Вызываем загрузку данных из базы и обновляем элементы страницы
    load_categories(page)
    load_products(page)

def load_categories(page):
    items_categories = []
    for i in engine.read_categories():
        items_categories.append(
            ft.Text(f"Category: {i[0]}", size=20, color=ft.colors.WHITE)
        )
    return ft.Column(controls=items_categories)

def load_products(page):
    items_product = []
    for name in engine.read_products():
        items_product.append(
            ft.Text(f"Product: {name}", size=20, color=ft.colors.WHITE)
        )
    return ft.Column(controls=items_product)
