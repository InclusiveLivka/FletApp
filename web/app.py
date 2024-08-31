import flet as ft
import os
import logging

from web.routes import setup_routes


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

os.environ["FLET_SECRET_KEY"] = os.urandom(12).hex()


async def flet_app(page: ft.Page):
    """
    Main entry point for the Flet application.

    :param page: The main Flet page object.
    """

    await set_windows(page)
    await setup_routes(page)


async def set_windows(page: ft.Page):
    """
    Configures the main page properties such as title, alignment, and
    dimensions.

    :param page: The Flet page object.
    """
    page.title = "Shop"
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 399
    page.window_height = 629
    page.window_max_height = 629
    page.window_max_width = 399
    page.scroll = ft.ScrollMode.HIDDEN
    page.theme = ft.Theme(color_scheme_seed=ft.colors.DEEP_PURPLE)
    page.update()
    logger.info("Page setup completed")
