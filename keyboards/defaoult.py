from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# class ReplyKeyboard:
#     def keyboard(buttons: list[str]) -> ReplyKeyboardMarkup:
        
cancel = KeyboardButton(text='Bekor qilish')
cancel_keyboard = ReplyKeyboardMarkup(keyboard=[[cancel]], resize_keyboard=True)

done = KeyboardButton(text="Tayyor")
done_cancel_keyboard = ReplyKeyboardMarkup(keyboard=[[cancel, done]], resize_keyboard=True)