from loader import dp, bot
from aiogram import types
from keyboards.inline import options_keyboard

@dp.poll_answer()
async def process_poll_answer(event: types.PollAnswer):
    r = await bot.get_chat_member(chat_id="@oqiladigan_kitoblar", user_id=event.user.id)
    print(r.status)
    event
    # print(event)

@dp.callback_query()
async def callback_handler(callback_data: types.CallbackQuery):
    user = await bot.get_chat_member(chat_id="@oqiladigan_kitoblar", user_id=callback_data.from_user.id)
    if user.status == "left":
        await callback_data.answer("https://t.me/oqiladigan_kitoblar kanaliga obuna bo'ling", show_alert=True)
    else:
        await callback_data.answer("to'g'ri", show_alert=True)
    
    

@dp.message()
async def message_handler(event: types.Message):
    chat_id = event.from_user.id #"@oqiladigan_kitoblar"
    await bot.send_message(chat_id=chat_id, text="Танлаб олинган матн қисми нусхасини хотирага кўчириб (қирқиб) олиш қандай амалга оширилади?", reply_markup=options_keyboard)#(chat_id=chat_id, question="test ucun", options=["tanlov 1", "tanlov 2"], type="quiz", correct_option_id=1, is_anonymous=False)
    # print(event)
