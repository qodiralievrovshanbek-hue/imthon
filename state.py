from aiogram.fsm.state import StatesGroup,State


class RegisterState(StatesGroup):
    full_name = State()
    phone_number= State()
    course = State()
    confirmation = State()