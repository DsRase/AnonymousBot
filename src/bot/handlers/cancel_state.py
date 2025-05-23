import logging

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.bot.handlers.command.start import start_handler

async def cancel(callback: CallbackQuery, state: FSMContext):
    try:
        await state.clear()
        await start_handler(callback.message, state)
        await callback.message.delete()
    except BaseException as e:
        logging.error(e)
        print(e)