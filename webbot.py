from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = Bot('6747997606:AAEonniPONqo7lHhD5U3Wx8bT1XY9v_3PKg')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("O'zbek 🇺🇿", callback_data='set_lang_uz'))
    keyboard.add(InlineKeyboardButton("Русский 🇷🇺", callback_data='set_lang_ru'))

    await message.answer("Muloqot uchun tlini tanlang\n\nВыберите язык для общения", reply_markup=keyboard)


@dp.callback_query_handler(lambda callback_query: True)
async def process_callback(callback_query: types.CallbackQuery):
    # Обрабатываем нажатие кнопок
    if callback_query.data == 'set_lang_uz':
        await bot.answer_callback_query(callback_query.id, text="🇺🇿 O‘zbek tili tanlandi ")
        await send_webpage_button(callback_query.message.chat.id, 'uz')  # Передаем язык 'uz'
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    elif callback_query.data == 'set_lang_ru':
        await bot.answer_callback_query(callback_query.id, text="🇷🇺 Выбран русский язык")
        await send_webpage_button(callback_query.message.chat.id, 'ru')  # Передаем язык 'ru'
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)


async def send_webpage_button(chat_id, lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if lang == 'uz':
        markup.add(types.KeyboardButton("🎁 Oling 🎁", web_app=types.WebAppInfo(url='https://clickuz.github.io/clickuz/test/uz.html')))
    elif lang == 'ru':
        markup.add(types.KeyboardButton("🎁 Получить 🎁", web_app=types.WebAppInfo(url='https://clickuz.github.io/clickuz/')))

    await bot.send_message(chat_id, 'Нажмите на кнопку 👇🏻\n\nTugmani bosing 👇🏻', reply_markup=markup)


executor.start_polling(dp)


