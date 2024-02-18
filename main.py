import asyncio
import nest_asyncio
import yt_dlp
import os
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import html

from config import TOKEN

nest_asyncio.apply()

bot = Bot(TOKEN)
dp = Dispatcher()


def get_direct_link(video_url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'quiet': True,
        'no_warnings': True,
        'outtmpl': '%(id)s.%(ext)s',
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)

    L = info_dict['formats']
    for x in range(len(L)):
        if L[x].get('height', 0) == 720:
            direct_link = L[x]['url']
            return direct_link


def get_video_title(video_url):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url=video_url, download=False)
        video_title = info_dict.get('title', None)
        return video_title


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.reply(f'Привіт, {message.from_user.first_name}.\n Я бот який допоможе тобі скачати відео з ютубу!')


@dp.message(F.text.regexp(r'^https:\/\/(www\.youtube.*|youtu\.be.*|youtube\.com.*)'))
async def link_answer_handler(message: Message):
    url = str(message.text)
    direct_link = get_direct_link(url)
    video_title = get_video_title(url)
    text = html.link(f'Силка для скачування: \n\n {video_title}', html.quote(direct_link))
    await message.answer(text, parse_mode="HTML")


@dp.message(F.text)
async def text_handler(message: Message):
    await message.answer('Для того щоб скачати відео з ютубу, скиньте силку')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot, skip_updates=True))
    loop.run_forever()
