from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



def make_options_keyboard(options: list[str]):

    options_list = []

    for option in options:
        options_list.append([InlineKeyboardButton(text=option[1:] if option[0]=='*' else option, callback_data="✅" if option[0]=='*' else "❌")])

    return InlineKeyboardMarkup(inline_keyboard=options_list)
    

