import asyncio
import logging
import flet as ft
from web.app import flet_app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FletService:
    """
    Service class to handle starting the Flet application.

    :param upload_dir: Directory for file uploads.
    :param view: Type of view for the Flet application (e.g., WEB_BROWSER).
    """

    def __init__(self, upload_dir: str, view: ft.View) -> None:
        logger.info("Initializing FletService...")
        self.upload_dir = upload_dir
        self.view = view

    async def start(self) -> asyncio.Task:
        """
        Starts the Flet application asynchronously.

        :return: An asyncio.Task object representing the Flet application task.
        :raises RuntimeError: If an error occurs while starting the Flet
        application.
        """
        try:
            flet_task = asyncio.create_task(
                await ft.app_async(
                    target=flet_app,
                    upload_dir=self.upload_dir,
                    view=self.view
                )
            )
            return flet_task
        except Exception as e:
            logging.getLogger(__name__).error(
                f"Error while starting Flet application: {e}"
            )
            raise
