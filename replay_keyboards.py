from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kurslar"), KeyboardButton(text="Kursga yozilish")],
        [KeyboardButton(text="Markaz haqida"), KeyboardButton(text="Aloqa")],
    ],
    resize_keyboard=True,
)

bekor_keyboards = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="❌ Bekor qilish")]],
    resize_keyboard=True,
)