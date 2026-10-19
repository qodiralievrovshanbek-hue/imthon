from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def register():
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="📚Kurslar"),
            KeyboardButton(text="📝Kursga yozlish")
        ],
        [
            KeyboardButton(text="🎞Markaz xaqida"),
            KeyboardButton(text="📞Aloqa")
        ]
        
    ],resize_keyboard=True)

    return markup