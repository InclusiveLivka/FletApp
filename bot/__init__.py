from aiogram import Dispatcher

def setup_routers(dp: Dispatcher):
    import bot.handler
    dp.include_router(bot.handler.router)