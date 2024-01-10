import sys
import asyncio
import logging
from loader import bot, dp
import handlers, filters, keyboards, states, data
from utils import set_bot_commands

async def main() -> None:
    await set_bot_commands.set_defaoul_commands(bot)
    # the run events dispatching
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())