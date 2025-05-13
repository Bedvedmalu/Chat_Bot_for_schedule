from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import get_groups, get_group_day

async def groups():
    all_groups = await get_groups()
    keyboard = InlineKeyboardBuilder()
    for group in all_groups:
        keyboard.add(InlineKeyboardButton(text=group.name, callback_data=f"group_{group.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def days(group_id):
    all_days = await get_group_day(group_id)
    keyboard = InlineKeyboardBuilder()
    for day in all_days:
        keyboard.add(InlineKeyboardButton(text=day.name, callback_data=f"day_{day.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()
