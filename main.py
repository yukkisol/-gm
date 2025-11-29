# Main entry point for Telegram bot

from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создаем клавиатуру с меню
def create_main_menu():
    keyboard = [
        [KeyboardButton(text="📅 Записаться на тренировку")],
        [KeyboardButton(text="👨‍🏫 Мои записи")],
        [KeyboardButton(text="💰 Цены и абонементы")],
        [KeyboardButton(text="📋 Расписание")],
        [KeyboardButton(text="👤 Тренеры"), KeyboardButton(text="📞 Контакты")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(
        '🏋️‍♂️ Добро пожаловать в фитнес-бот!',
        reply_markup=create_main_menu()
    )

@dp.message(Command('menu'))
async def show_menu(message: Message):
    await message.answer(
        '🏋️‍♂️ Главное меню:',
        reply_markup=create_main_menu()
    )

# Обработчик кнопки "Расписание"
@dp.message(lambda message: message.text == "📋 Расписание")
async def show_schedule(message: Message):
    schedule_text = """
📋 Расписание тренировок:

Понедельник:
• 09:00 - 💪 Силовая тренировка
• 11:00 - 🧘 Йога
• 18:00 - 🥊 Бокс
• 20:00 - 🏃 Кардио

Вторник:
• 10:00 - 💪 Силовая тренировка
• 12:00 - 🧘 Йога
• 19:00 - 💃 Фитнес

Среда:
• 09:00 - 🏃 Кардио
• 11:00 - 💪 Силовая тренировка
• 18:00 - 🥊 Бокс

Четверг:
• 10:00 - 🧘 Йога
• 12:00 - 💪 Силовая тренировка
• 19:00 - 💃 Фитнес

Пятница:
• 09:00 - 🥊 Бокс
• 11:00 - 🏃 Кардио
• 18:00 - 💪 Силовая тренировка

Суббота:
• 10:00 - 🧘 Йога
• 12:00 - 💃 Фитнес

Воскресенье:
• Выходной
    """
    await message.answer(schedule_text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())