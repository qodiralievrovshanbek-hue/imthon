import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from replay_keyboards import main_keyboards, bekor_keyboards
from inline_keyboards import kurslar_buttons, kurs_tanlash_buttons, tasdiqlash_buttons


bot = Bot(token="8953558652:AAErID4V0biMEt-fYAygAUpSP7QdVqGkor0")
dp = Dispatcher()


async def start():
    print("Bot ishga tushdi ...")
    await dp.start_polling(bot)


kurslar = {
    "python": ("Python", "4 oy", "800 000 so'm"),
    "web": ("Web dasturlash", "6 oy", "1 000 000 so'm"),
    "frontend": ("Frontend", "5 oy", "900 000 so'm"),
    "dizayn": ("Grafik dizayn", "3 oy", "700 000 so'm"),
}


class Yozilish(StatesGroup):
    ism = State()
    telefon = State()
    kurs = State()
    tasdiq = State()


@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Helloo", reply_markup=main_keyboards)


@dp.message(F.text == "❌ Bekor qilish")
async def bekor_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Yozilish bekor qilindi", reply_markup=main_keyboards)


@dp.message(F.text == "Kurslar")
async def about_kurslar(message: Message):
    await message.answer(text="Bizning kurslar", reply_markup=kurslar_buttons)


@dp.callback_query(F.data.startswith("course_"))
async def kurslar_haqida(callback: CallbackQuery):
    nom, davomiylik, narx = kurslar[callback.data.split("_")[1]]
    await callback.message.answer(
        text=f"📚 Kurs: {nom}\n⏳ Davomiyligi: {davomiylik}\n💰 Narxi: {narx}")
    await callback.answer()


@dp.message(F.text == "Markaz haqida")
async def markaz_haqida(message: Message):
    await message.answer(
        text="Markazimiz 2018-yildan beri IT sohasida zamonaviy bilim beradi.",
        reply_markup=main_keyboards)


@dp.message(F.text == "Aloqa")
async def aloqa(message: Message):
    await message.answer(
        text="📞 Telefon: +998 90 123 45 67\n📍 Manzil: Farg'ona sh.\n🕘 Ish vaqti: 08:00 - 21:00",
        reply_markup=main_keyboards)


@dp.message(F.text == "Kursga yozilish")
async def yozilish_boshlash(message: Message, state: FSMContext):
    await state.set_state(Yozilish.ism)
    await message.answer(text="Ism va familiyangizni kiriting:", reply_markup=bekor_keyboards)


@dp.message(Yozilish.ism, F.text)
async def ism_qabul(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await state.set_state(Yozilish.telefon)
    await message.answer(text="Telefon raqamingizni kiriting:")


@dp.message(Yozilish.telefon, F.text)
async def telefon_qabul(message: Message, state: FSMContext):
    await state.update_data(telefon=message.text)
    await state.set_state(Yozilish.kurs)
    await message.answer(text="Kursni tanlang:", reply_markup=kurs_tanlash_buttons)


@dp.callback_query(Yozilish.kurs, F.data.startswith("tanla_"))
async def kurs_tanlash(callback: CallbackQuery, state: FSMContext):
    await state.update_data(kurs=kurslar[callback.data.split("_")[1]][0])
    malumot = await state.get_data()
    await state.set_state(Yozilish.tasdiq)
    await callback.message.answer(
        text=f"Ism: {malumot['ism']}\nTelefon: {malumot['telefon']}\nKurs: {malumot['kurs']}",
        reply_markup=tasdiqlash_buttons)
    await callback.answer()


@dp.callback_query(Yozilish.tasdiq, F.data == "tasdiqlash")
async def tasdiqlash(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(text="✅ Qabul qilindi!", reply_markup=main_keyboards)
    await callback.answer()




asyncio.run(start())