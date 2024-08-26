import flet as ft
import logging
from web.ui.elements import UIConstants
from web.database import engine
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_page(page: ft.Page) -> list[ft.Text]:
    try:
        def delete_category(e):
            page.close(dlg_modal)

        def close_modal(e):
            page.close(dlg_modal)
            
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Подтвердите удаление!"),
            content=ft.Text("Вы удаляете категорию и все ее продукты. Продолжить?"),
            actions=[
                ft.TextButton("Подтвердить!",
                            on_click= delete_category),
                ft.TextButton("Отмена", on_click= close_modal),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        window = ft.Column(controls=[
            UIConstants.DELETE_CATEGORY_FIELD,
            ft.FloatingActionButton(
                text="Delete", width=399, on_click=lambda e: page.open(dlg_modal)),
            UIConstants.DELETE_PRODUCT_FIELD,
            ft.FloatingActionButton(text="Delete", width=399, on_click=lambda e: engine.delete_product(
                UIConstants.DELETE_PRODUCT_FIELD.value))

        ])
        return [window]
    except:
        logger.exception("Failed to load delete page")
