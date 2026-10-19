import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart


from buttons import register
from buttons2 import it_buttons, contact_buttons
from state import RegisterState


bot = Bot(token="8953558652:AAErID4V0biMEt-fYAygAUpSP7QdVqGkor0")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    print("bot ishlamoqda...")
    await message.answer("Hellow", reply_markup=await register())


@dp.message(F.text == "📚Kurslar")
async def about_it(message:Message):
    await message.answer(text="IT kurslarimiz",
                         reply_markup=it_buttons)

    
@dp.message(F.text == "📝Kursga yozlish")
async def register_course(message:Message):
    await message.answer(text="Ismingizni kiriting",
                         reply_markup=ReplyKeyboardRemove())

    
@dp.message(RegisterState.full_name)
async def get_full_name(message:Message):
    await message.answer(text="Telefon raqamingizni kiriting",
                         reply_markup=ReplyKeyboardRemove())

    
@dp.message(RegisterState.phone_number,F.course)
async def get_phone_number(message:Message):
    await message.answer(text="Kursni tanlang",
                         reply_markup=ReplyKeyboardRemove())

    
@dp.message(RegisterState.course)
async def get_course(message:Message):
    await message.answer(text="Tasdiqlang",
                         reply_markup=ReplyKeyboardRemove())

    
@dp.message(RegisterState.confirmation)
async def get_confirmation(message:Message):
    await message.answer(text="yozilish yakunlandi",
                         reply_markup=ReplyKeyboardRemove())


malumot = "Najot Ta'lim. Markazimizda IT sohasidagi eng zamonaviy kurslar o'tkaziladi. "
@dp.message(F.text == "🎞Markaz xaqida")
async def about_center(message:Message):
    await message.answer(text=malumot,
                         reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == "📞Aloqa")
async def contact(message:Message):
    await message.answer(text="Biz bilan aloqaga chiqish",
                         reply_markup=contact_buttons)

    
async def main():
    await dp.start_polling(bot)


asyncio.run(main())