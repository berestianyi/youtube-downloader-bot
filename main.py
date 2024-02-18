import asyncio
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import nest_asyncio

from config import TOKEN

nest_asyncio.apply()

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.reply(f'Hello, {message.from_user.first_name}.\n I will help you to download any video from youtube!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot, skip_updates=True))
    loop.run_forever()