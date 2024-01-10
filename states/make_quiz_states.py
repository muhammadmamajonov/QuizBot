from aiogram.fsm.state import State, StatesGroup


class Quiz(StatesGroup):
    question = State()
    option = State()

    