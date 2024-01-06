from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

options_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ctrl + X yoki Shift + Delete", callback_data='1')],
    [InlineKeyboardButton(text="Ctrl + X yoki Ctrl + Shift + F12", callback_data='0')],
    [InlineKeyboardButton(text="Ctrl + S yoki Shift + F12 yoki Alt + Shift + F12", callback_data='0')],
    [InlineKeyboardButton(text="Ctrl + Z yoki Alt + Backspace", callback_data='0')],
    ])

