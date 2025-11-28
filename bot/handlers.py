from aiogram import F, Router
from aiogram.types import Message

from core.services import (
    create_trainer,
    create_slot,
    list_slots,
    book_slot
)

router = Router()


@router.message(F.text == "показать слоты")
async def show_slots_handler(message: Message):
    slots = list_slots()
    if not slots:
        await message.answer("Нет доступных слотов")
    else:
        response = "Доступные слоты:\n"
        for slot in slots:
            response += f"ID: {slot.id}, Тренер: {slot.trainer_id}, Время: {slot.time}\n"
        await message.answer(response)


@router.message(F.text == "записаться")
async def book_slot_handler(message: Message):
    await message.answer("Введите ID слота для бронирования")
