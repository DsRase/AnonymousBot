import logging

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.env import MAIN_CHARACTER

async def send_anon_msg(msg: Message, bot: Bot, state: FSMContext):
    id_to = await state.get_data()
    id_to = id_to["id_to"]

    try:
        text = "*Вам анонимное сообщение\!*"

        if id_to == MAIN_CHARACTER:
            text += f" Но для вас, оно от пользователя @{msg.from_user.username}\."

        await bot.send_message(id_to, text=text)
        await msg.copy_to(id_to)
    except BaseException as e:
        logging.error(e)
        await msg.answer(text="Извините, но этот пользователь *не подключен* к боту :\(\n"
                              "Мы не можем отправить ему ваше сообщение\.")
    finally:
        await state.clear()