
from data.config import TOKEN
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher

# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()