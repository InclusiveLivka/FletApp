import flet as ft
import logging

from web.ui.elements import UIConstants
from web.database import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_page(page: ft.Page) -> list[ft.Control]:
    """
    Create a page for deleting categories and products.

    :param page: The page to create the delete page for.
    :return: A list of Flet controls for the delete page.
    """
    try:
        categories = engine.read_categories()
        products = engine.read_products()

        UIConstants.DELETE_CATEGORY_FIELD.options = [
            ft.dropdown.Option(category[0]) for category in categories]
        UIConstants.DELETE_PRODUCT_FIELD.options = [
            ft.dropdown.Option(product[0]) for product in products]

        def delete_category(e: ft.ControlEvent):
            category_link = engine.read_link_of_name_category(
                UIConstants.DELETE_CATEGORY_FIELD.value)[0]
            engine.delete_category_and_products(category_link)
            UIConstants.DELETE_CATEGORY_FIELD.options = [
                ft.dropdown.Option(category[0]) for category in engine.read_categories()]
            page.close(dlg_modal)
            page.update()

        def delete_product(e: ft.ControlEvent):
            engine.delete_product(UIConstants.DELETE_PRODUCT_FIELD.value)
            UIConstants.DELETE_PRODUCT_FIELD.options = [
                ft.dropdown.Option(product[0]) for product in engine.read_products()]
            page.update()

        def close_modal(e: ft.ControlEvent):
            page.close(dlg_modal)

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Подтвердите удаление!"),
            content=ft.Text(
                "Вы удаляете категорию и все ее продукты. Продолжить?"),
            actions=[
                ft.TextButton("Подтвердить!",
                              on_click=delete_category),
                ft.TextButton("Отмена", on_click=close_modal),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        window = ft.Column(controls=[
            UIConstants.DELETE_CATEGORY_FIELD,
            ft.FloatingActionButton(
                text="Удалить категорию", width=399, on_click=lambda e: page.open(dlg_modal)),
            UIConstants.DELETE_PRODUCT_FIELD,
            ft.FloatingActionButton(
                text="Удалить продукт", width=399, on_click=lambda e: delete_product(e)),


        ])
        return [window]
    except:
        logger.exception("Failed to load delete page")
