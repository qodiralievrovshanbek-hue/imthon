from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kurslar_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Python", callback_data="course_python")],
    [InlineKeyboardButton(text="Web dasturlash", callback_data="course_web")],
    [InlineKeyboardButton(text="Frontend", callback_data="course_frontend")],
    [InlineKeyboardButton(text="Grafik dizayn", callback_data="course_dizayn")],
])

kurs_tanlash_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Python", callback_data="tanla_python")],
    [InlineKeyboardButton(text="Web dasturlash", callback_data="tanla_web")],
    [InlineKeyboardButton(text="Frontend", callback_data="tanla_frontend")],
    [InlineKeyboardButton(text="Grafik dizayn", callback_data="tanla_dizayn")],
])

tasdiqlash_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="tasdiqlash")],
])