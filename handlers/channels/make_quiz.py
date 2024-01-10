from states import Quiz
from loader import dp, bot
from aiogram import types, F
from data.config import CHANNEL_ID, ADMINS
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from keyboards.inline import make_options_keyboard
from keyboards.defaoult import cancel_keyboard, done_cancel_keyboard


@dp.message(Command('quiz'))
async def message_handler(message: types.Message, state: FSMContext) -> None:
    print(ADMINS, )
    if str(message.from_user.id) in ADMINS:
        await state.set_state(Quiz.question)
        print(await state.get_state())
        await message.answer("Savolni yuboring.", reply_markup=cancel_keyboard)
    else:
        await message.answer("Sizga ruxsat yo'q")
       

@dp.message(F.text == 'Bekor qilish')
async def cancel_quizmaker(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Bekor qilindi.", reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text == "Tayyor")
async def quiz_ready(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(chat_id=CHANNEL_ID, text=data['question'], reply_markup=make_options_keyboard(data['options']))
    await message.answer(text="Savol kanalga joylandi", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@dp.message(Quiz.question)
async def get_question(message: types.Message, state: FSMContext):
    await state.update_data(question=message.text)
    await state.update_data(options=[])
    await state.set_state(Quiz.option)
    await message.answer(text="Varyantlarni kiriting. Har bir varyantni alohida yuboring. To'g'ri variantni boshiga <code>*</code> yozib jo'nating", reply_markup=done_cancel_keyboard)


@dp.message(Quiz.option)
async def get_option(message: types.Message, state: FSMContext):
    data = await state.get_data()
    options = data['options']
    options.append(message.text)
    await state.update_data(options=options)


