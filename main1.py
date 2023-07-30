from main import getweather
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor


API_TOKEN = '6184735775:AAFI0jobSpVhmqETzc76wamaSuz7imE0n-k'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
class Form(StatesGroup):
    city = State() 

@dp.message_handler(commands=['start'])
async def cancel_handler(message: types.Message, state: FSMContext):
    await message.answer("Введите название города:")
    await state.set_state(Form.city)
@dp.message_handler(state=Form.city)
async def weather(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply(await getweather(message.text))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
