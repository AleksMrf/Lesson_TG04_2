import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import TOKEN

API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("dynamic"))
async def show_initial_button(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data="show_more")],
    ])
    await message.answer("Нажмите кнопку ниже:", reply_markup=keyboard)

@dp.callback_query()
async def handle_callback(callback_query: types.CallbackQuery):
    if callback_query.data == "show_more":
        new_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Опция 2", callback_data="option_2")],
        ])
        await callback_query.message.edit_text("Выберите опцию:", reply_markup=new_keyboard)
    elif callback_query.data == "option_1":
        await callback_query.message.answer("Вы сделали правильный выбор!")
    elif callback_query.data == "option_2":
        await callback_query.message.answer("Вы сделали неправильный выбор!")

        await callback_query.answer()

if __name__ == "__main__":
    dp.run_polling(bot)