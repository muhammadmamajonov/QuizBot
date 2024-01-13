import sys
import asyncio
import logging
import keyboards, states
from loader import bot, dp
from handlers.make_quiz import *
from handlers.answer_quiz import *
from utils import set_bot_commands

async def main() -> None:
    await set_bot_commands.set_defaoul_commands(bot)
    # the run events dispatching
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())