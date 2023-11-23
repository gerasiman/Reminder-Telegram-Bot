from __future__ import print_function

import logging
import time
import asyncio
import aioschedule
import string
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.utils.executor import start_polling
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Google import google

text1="дата пустая"

API_TOKEN = '6253548575:AAEYWskJsB49t4elTtRYJ_ARi_DE0d8S390'

arrOfChar=['_',"G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA","AB","AC","AD","AE","AF","AG","AH","AI","AJ","AK"]
dateOfDay=arrOfChar[15]

loop = asyncio.get_event_loop()
# Настройки логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def send_message():
    await bot.send_message(chat_id=460141280, text="q")

async def scheduler():
    aioschedule.every(3).seconds.do(send_message)
    aioschedule.every(3).minutes.do(send_message)
    aioschedule.every(3).hours.do(send_message)
    aioschedule.every(3).days.do(send_message)
    aioschedule.every(3).weeks.do(send_message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(_):

    asyncio.create_task(scheduler())


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот, который напоминает о работе")
    print(message.from_user.id)





@dp.message_handler()
async def reminder(message: types.Message):
    void=""
    out=[]
    global text1

    var = google(arrOfChar[int(message.text)])
    print(var)

    if var:
        text1 = " "



        for i in range(len(var)):

            if var[i][0][0] == '&':

                var[i] = var[i][1:]
                text1=text1+"\n"
                out=[]
                text1 = text1 + var[i]
                out.append(var[i])
            elif var[i] == ' ':
                var.pop(i)
                var.insert(i,"")
            elif var[i][0][0] == '*':
                var[i] = var[i][1:]
                void=void+var[i]+"\n"
            elif len(out) == 6:
                out.append(var[i])

                text1 = text1 + "   "+ var[i]
            elif len(out) == 5:
                out.append(var[i])

                text1 = text1 + "   "+ var[i]
            elif len(out) == 4:
                out.append(var[i])

                text1 = text1 + "-"+ var[i]
            elif len(out) == 3:
                out.append(var[i])

                text1=text1+"   "+ var[i]
            elif len(out) == 2:

                out.append(var[i])
                text1 = text1 + "-" + var[i]
            elif len(out) == 1:

                text1=text1+"\n"+ var[i]
                out.append(var[i])


    text1=text1+"\n"+void
    await message.answer(text=text1)





# Запускаем бота
if __name__ == '__main__':
    start_polling(dp, skip_updates=True , on_startup=on_startup)