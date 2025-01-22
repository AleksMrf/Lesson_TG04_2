
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN

API_TOKEN = TOKEN

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Создаем инлайн-клавиатуру с URL кнопками
inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url="https://ria.ru/")],
    [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru/")],
    [InlineKeyboardButton(text="Видео", url="https://www.kinopoisk.ru/")]
])

@dp.message(Command("links"))
async def send_links(message: types.Message):
    await message.answer("Выберите категорию:", reply_markup=inline_keyboard)

if __name__ == "__main__":
    dp.run_polling(bot)


