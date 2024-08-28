import aiogram
from aiogram.types import Message
from bot.inline import open_inline, open_admin_inline
from aiogram.filters import CommandStart
from aiogram import Router

import os
from dotenv import load_dotenv, find_dotenv

router = Router()

load_dotenv(find_dotenv())
id_owner = int(os.getenv("ID_OWNER"))

@router.message()
async def command_start_handler(message: Message) -> None:
    if message.from_user.id == id_owner:
        await message.answer("Привет, поздравляю вы администратор!!!", reply_markup=open_admin_inline())
    else:
        await message.answer("Привет, это переходник в мой онлайн магазин, давай закупимся?", reply_markup=open_inline())