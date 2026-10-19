from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

it_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Python", callback_data="course_python")],
    [InlineKeyboardButton(text="Web dasturlash", callback_data="course_dasturlash")],
    [InlineKeyboardButton(text="Frontend", callback_data="course_frontend")],
    [InlineKeyboardButton(text="Grafik dizain", callback_data="course_grafik")],
])

contact_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📞Telefon", callback_data="contact_phone")],
])

