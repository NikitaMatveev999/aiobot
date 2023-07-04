import logging
import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
my_chat_id = os.getenv('ID')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я бот-приветственщик. Как могу тебе помочь?")



@dp.message_handler()
async def handle_message(message: types.Message):
    user = message.from_user
    user_id = user.id
    user_username = user.username
    user_first_name = user.first_name
    user_last_name = user.last_name

    text = message.text

    forward_message = f'Новое сообщение от пользователя:\n\n'
    forward_message += f'Пользователь: {user_first_name} {user_last_name} (@{user_username})\n'
    forward_message += f'ID пользователя: {user_id}\n'
    forward_message += f'Сообщение: {text}'

    await bot.send_message(chat_id=my_chat_id, text=forward_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
