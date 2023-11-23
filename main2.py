import logging
import asyncio
import aioschedule
import time

from googleTim import googleTimStart, TakeDataForText
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.utils.executor import start_polling

API_TOKEN = '6253548575:AAEYWskJsB49t4elTtRYJ_ARi_DE0d8S390'

logging.basicConfig(level=logging.INFO)
#604659723
#5678060218
global list

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def send_message():
    global list
    textOfMessage = TakeDataForText(list)
    print(textOfMessage)
    if textOfMessage!=f"начали работать в {time.strftime('%H')}:{time.strftime('%M')} : \n":
        await bot.send_message(chat_id=460141280, text=textOfMessage)
        await bot.send_message(chat_id=604659723, text=textOfMessage)
        await bot.send_message(chat_id=5678060218, text=textOfMessage)
        await bot.send_message(chat_id=421468072, text=textOfMessage)

async def scheduler():
    aioschedule.every().hours.at(":00").do(send_message)
    aioschedule.every().hours.at(":05").do(send_message)
    aioschedule.every().hours.at(":10").do(send_message)
    aioschedule.every().hours.at(":15").do(send_message)
    aioschedule.every().hours.at(":20").do(send_message)
    aioschedule.every().hours.at(":25").do(send_message)
    aioschedule.every().hours.at(":30").do(send_message)
    aioschedule.every().hours.at(":35").do(send_message)
    aioschedule.every().hours.at(":40").do(send_message)
    aioschedule.every().hours.at(":45").do(send_message)
    aioschedule.every().hours.at(":50").do(send_message)
    aioschedule.every().hours.at(":55").do(send_message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(_):
    global list
    list = googleTimStart()
    asyncio.create_task(scheduler())

@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот, который напоминает о работе")
    print(message.from_user.id)




if __name__ == '__main__':
    start_polling(dp, skip_updates=True , on_startup=on_startup)


