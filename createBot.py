from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from constants import BOT_API_KEY

#створення і підлючення боту
bot = Bot(token=BOT_API_KEY)
dp = Dispatcher(bot)