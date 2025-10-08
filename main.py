import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram import types
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from buttons import main_menu
from heandler import dp_hodim, dp_info, dp_ish_joy, dp_shogird, dp_ustoz

TOKEN = "8408799044:AAHARQjzhl2Y5q05oknB4b2EymMEFjjBecw"

dp = Dispatcher(storage=MemoryStorage())

bot = Bot(token=TOKEN)


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer(f"Salom {msg.from_user.first_name} xush kelibsiz \n /help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!", reply_markup=main_menu)
    
@dp.message(Command('help'))
async def help(msg: types.Message):
    await msg.answer("Bu bot orqali siz daromad qila olasiz \n\n start ni bosing")




async def main() -> None:
    dp.include_router(dp_info)  
    dp.include_router(dp_hodim)  
    dp.include_router(dp_ustoz)  
    dp.include_router(dp_shogird)  
    dp.include_router(dp_ish_joy)  
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())