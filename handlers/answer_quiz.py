
from aiogram import types
from loader import dp, bot
from data.config import CHANNEL_ID

@dp.callback_query()
async def callback_handler(callback_data: types.CallbackQuery):
    user = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=callback_data.from_user.id)
    if user.status == "left":
        await callback_data.answer(f"{CHANNEL_ID} kanaliga obuna bo'ling", show_alert=True)
    else:
        await callback_data.answer(callback_data.data, show_alert=True)