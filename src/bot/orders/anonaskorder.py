from aiogram.fsm.state import State, StatesGroup

class OrderSendAnonMsg(StatesGroup):
    waiting_for_message = State()