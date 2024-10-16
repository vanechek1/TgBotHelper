#import telebot
from aiogram import Bot, Dispatcher, types, executor
import pymorphy2
from pymorphy2 import MorphAnalyzer

#bot = telebot.TeleBot('8075407431:AAFAhn5On7QgbH3a571MBa4ersEnC8RFDLw')

bot = Bot('8075407431:AAFAhn5On7QgbH3a571MBa4ersEnC8RFDLw')
dp = Dispatcher(bot)


@dp.message_handler(text=['Хочу задать вопрос'])
async def question(message: types.Message):
    await message.reply('Много хочешь, подумай сам и не задавай тупых вопросов')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton('Хочу задать вопрос', callback_data='question')
    markup.row(btn1)
    await message.reply('Привет! Я - бот-помощник, можешь задать мне вопрос, а я попробую на него ответить!', reply_markup=markup)

@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2) # количество кнопок в ряду
    markup.add(types.InlineKeyboardButton('Site', callback_data='сайта нет'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data in ['question'])
async def callback(call: types.CallbackQuery):
    if call.data == 'question':
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, 'Хороший вопрос, подумай сам')


@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True) # после нажатия кнопки пропадут
    markup.add(types.KeyboardButton('site'))
    markup.add(types.KeyboardButton('website'))
    await message.answer('Hello', reply_markup=markup)



@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)




executor.start_polling(dp)
#bot.infinity_polling()