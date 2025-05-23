from aiogram import Bot, Dispatcher, F
from asyncio import run

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

import logging

from src.env import TOKEN
from src.bot.orders.anonaskorder import OrderSendAnonMsg

from src.bot.handlers.command.start import start_handler
from src.bot.handlers.sendAnonMsg import send_anon_msg
from src.bot.handlers.cancel_state import cancel

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] >> %(message)s")

bot = Bot(token=TOKEN,
          default=DefaultBotProperties(
              parse_mode=ParseMode.MARKDOWN_V2
          ))

dp = Dispatcher(storage=MemoryStorage())

def register_handlers():
    # STATES
    dp.message.register(send_anon_msg, OrderSendAnonMsg.waiting_for_message)

    # COMMANDS
    dp.message.register(start_handler, Command("start"))

    # CALLBACKS
    dp.callback_query.register(cancel, F.data == "cancel_state")

    # ANYTHING ELSE
    dp.message.register(start_handler, lambda data: True)

async def main():
    register_handlers()
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())