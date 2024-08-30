import asyncio
import logging
import threading
import flet as ft
from web.service import FletService
from bot.start_bot import start_bot

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main() -> None:
    """
    Main entry point of the application.

    :return: None
    """
    logger.info("Starting main application...")

    # Инициализация Flet сервиса
    flet_service = FletService(upload_dir="uploads", view=ft.FLET_APP)

    # Запуск Flet сервиса
    try:

        logger.info("Starting Flet application...")
        await flet_service.start()
    except Exception as e:
        logger.error(f"Failed to start Flet application: {e}")
        return
    # Запуск бота

    logger.info("Application is running...")

if __name__ == '__main__':
    asyncio.run(main())
