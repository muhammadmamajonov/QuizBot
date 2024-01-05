from aiogram.types import BotCommand


async def set_defaoul_commands(bot):
    await bot.set_my_commands(
        [
            BotCommand("start", "botni ishga tushirish"),
        ]

    )