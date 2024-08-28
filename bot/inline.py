from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def open_inline():
    builder = InlineKeyboardBuilder()
    builder.button(text="💎Посетить онлайн магазин💎",web_app = WebAppInfo(url="https://b396-2a02-d247-5101-2104-65c1-4e4a-a36f-c321.ngrok-free.app"),)
    return builder.as_markup()

def open_admin_inline():
    builder = InlineKeyboardBuilder()
    builder.button(text="⚙️Войти как Админ⚙️",web_app= WebAppInfo(url="https://3af2-2a02-d247-5101-2104-a919-ba3e-e87a-bedc.ngrok-free.app"),)
    return builder.as_markup()