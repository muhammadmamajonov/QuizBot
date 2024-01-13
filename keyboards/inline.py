from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



def make_options_keyboard(options: list[str], index_of_clicked=None):

    options_list = []
    i = 0
    for option in options:
        options_list.append([InlineKeyboardButton(text=option[1:] if option[0]=='*' else option, callback_data=f"{i}✅" if option[0]=='*' else f"{i}❌")])
        i += 1
    return InlineKeyboardMarkup(inline_keyboard=options_list)
    

def edit_options_keyboard(callback: CallbackQuery):
        index_of_clicked = callback.data[0]
        i = 0
        options_list = []
        for option in callback.message.reply_markup.inline_keyboard:
            splited_text = option[0].text.split(' ')
            count=int(splited_text[-1])
            if i == int(index_of_clicked):
                count += 1
                splited_text[-1] = str(count)
            text = " ".join(splited_text)
            option[0].text = text
            options_list.append(option)
            i += 1
        return InlineKeyboardMarkup(inline_keyboard=options_list)