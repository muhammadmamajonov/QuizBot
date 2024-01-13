
from aiogram import types
from loader import dp, bot
from config import CHANNELS
from db import is_answered, insert
from keyboards.inline import edit_options_keyboard

@dp.callback_query()
async def callback_handler(callback_data: types.CallbackQuery):
    member_status = ""
    channels = "\n".join(CHANNELS)

    for channel in CHANNELS:
        user = await bot.get_chat_member(chat_id=channel, user_id=callback_data.from_user.id)
        member_status = user.status

    if member_status == "left":
        await callback_data.answer(f"{channels} kanallarga obuna bo'ling", show_alert=True)
    else:
        if is_answered(callback_data.from_user.id, callback_data.message.message_id):
            await callback_data.answer(text="Bu savolga javob bergansiz", show_alert=True)
        else:
            insert(callback_data.from_user.id, callback_data.message.message_id)
            await callback_data.message.edit_reply_markup(str(callback_data.message.message_id), reply_markup=edit_options_keyboard(callback_data))
            await callback_data.answer(callback_data.data[-1], show_alert=True)
