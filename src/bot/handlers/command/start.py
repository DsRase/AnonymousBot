from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, SwitchInlineQueryChosenChat

from src.bot.orders.anonaskorder import OrderSendAnonMsg

async def start_handler(msg: Message, state: FSMContext):
    try:
        if len(msg.text.split(" ")) > 2: raise Exception
        id_of_user = msg.text.split(" ")[1]

        cancel_markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Отмена!", callback_data="cancel_state")]
        ])

        await msg.answer(text="Напиши *любое* сообщение, оно будет *анонимно* отправлено пользователю, от которого ты пришёл\!",
                         reply_markup = cancel_markup)
        await state.set_state(OrderSendAnonMsg.waiting_for_message)
        await state.update_data(id_to = id_of_user)
    except BaseException:
        link = f"https://t\.me/MsgAnonymousBot?start\={msg.from_user.id}"
        text_for_forward = f"\n\nПерейдите по этой ссылке для того, чтобы задать мне анонимный вопрос!\nhttps://t.me/MsgAnonymousBot?start={msg.from_user.id}"

        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="🔗 Поделиться ссылкой 🔗",
                switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(query=text_for_forward,
                                                                            allow_user_chats=True,
                                                                            allow_group_chats=True,
                                                                            allow_channel_chats=True
                                                                            )
            )]
        ])
        text = (f"*Твоя ссылка:* {link}\n"
                f"Отправь её своим друзьям, чтобы те написали тебе *анонимное сообщение*\!")
        await msg.answer(text=text, reply_markup=markup)