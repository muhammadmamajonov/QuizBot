
from aiogram import types
from loader import dp, bot


@dp.callback_query()
async def callback_handler(callback_data: types.CallbackQuery):
    user = await bot.get_chat_member(chat_id="@oqiladigan_kitoblar", user_id=callback_data.from_user.id)
    if user.status == "left":
        await callback_data.answer("https://t.me/oqiladigan_kitoblar kanaliga obuna bo'ling", show_alert=True)
    else:
        await callback_data.answer(callback_data.data, show_alert=True)