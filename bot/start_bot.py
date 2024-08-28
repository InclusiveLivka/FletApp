import asyncio
import logging
import sys
import os
from dotenv import load_dotenv, find_dotenv

from aiogram import Bot, Dispatcher
from bot.__init__ import setup_routers




async def start_bot() -> None:
    """
    Asynchronous function that sets up and runs the bot instance.

    This function initializes the bot instance with the default bot properties
    which will be passed to all API calls. It then creates a dispatcher instance
    and logs the creation of the dispatcher. The function then sets up the routers
    and logs the setup of the routers. Finally, it starts the polling of events
    for the bot instance.
    """
    dp = Dispatcher()

    # Настройка логирования
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    load_dotenv(find_dotenv())  # Load environment variables from .env file
    # Create bot instance with bot token from environment variables
    bot = Bot(os.getenv("BOT_TOKEN"))

    # Создание диспетчера
    dp = Dispatcher()  # Create dispatcher instance
    logger.info("Dispatcher instance created")  # Log creation of dispatcher

    # Подключение роутеров
    setup_routers(dp)  # Set up routers
    logger.info("Routers setup")  # Log setup of routers

    # And the run events dispatching
    await dp.start_polling(bot)  # Start polling of events for the bot instance
    
    return asyncio.run(start_bot())


    

