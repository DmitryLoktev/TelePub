from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from src.common.db.requests import add_book
from src.common.keys.keys_book import kb_time, kb_quantity, kb_skip, kb_phone, kb_cancel, kb_bar
from config import admins
from create_bot import bot
from src.common.keys.keys_start_menu import kb_start
from time import sleep
from aiogram.dispatcher.filters import Text
import datetime
from src.common.messages_bot.bot_messages import name_message, data_message, time_message, quantity_message, wish_message, \
    phone_message, cancel_message, finish_message, bar_message
from src.common.messages_bot.stickers import cancel_book_sticker


class Book(StatesGroup):
    bar = State()
    name = State()
    data = State()
    time = State()
    quantity = State()
    wish = State()
    phone = State()


# @dp.message_handler(commands='booking', state= None)
async def cm_start(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await Book.bar.set()
    await bot.send_message(chat_id, text=bar_message, reply_markup=kb_bar, parse_mode='HTML')


# @dp.message_handler(state='*', commands="Выйти из бронирования" )
# @dp.message_handler(Text(equals='Выйти из бронирования', ignore_case=True), state='*' )
async def cancel_book(message=types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_sticker(message.from_user.id, sticker=cancel_book_sticker)
    await message.reply(cancel_message, reply_markup=kb_start, parse_mode='HTML')


# @dp.message_handler(content_types= ["photo"], state=Book.photo)

async def load_bar(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['bar'] = message.text
    await Book.name.set()
    await bot.send_message(message.from_user.id, text=name_message, reply_markup=kb_cancel, parse_mode='HTML')


async def load_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Book.next()
    await bot.send_message(message.from_user.id, data_message, reply_markup=kb_cancel, parse_mode='HTML')


async def load_data(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['data'] = message.text
    await Book.next()
    await bot.send_message(message.from_user.id, time_message, reply_markup=kb_time, parse_mode='HTML')


# @dp.message_handler( state = Book.data)
async def load_time(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    await Book.next()
    await bot.send_message(message.from_user.id, quantity_message, reply_markup=kb_quantity, parse_mode='HTML')


# @dp.message_handler( state = Book.how_many)
async def load_quantity(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text
    await Book.next()
    await bot.send_message(message.from_user.id, wish_message, reply_markup=kb_skip, parse_mode='HTML')


async def load_wish(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['wish'] = message.text
    await Book.next()
    await bot.send_message(message.from_user.id, phone_message, reply_markup=kb_phone, parse_mode='HTML')


# @dp.message_handler( state = Book.wish)
async def load_phone(message: types.Message, state=FSMContext):

    async with state.proxy() as data:
        if message.contact and message.contact.phone_number:
            data['phone'] = message.contact.phone_number
        else:
            # Если атрибут 'phone_number' не доступен, сохраняем текстовое сообщение
            data['phone'] = message.text

    async with state.proxy() as data:
        pub = data.get('bar')
        name = data.get('name')
        date = data.get('data')
        time = data.get('time')
        quantity = data.get('quantity')
        wish = data.get('wish')
        phone = data.get('phone')
        tg_name = message.from_user.full_name
        tg_link = '@' + message.from_user.username
        tg_id = message.from_user.id
        time_on = datetime.datetime.now()

        await add_book(pub, name, tg_name, tg_link, tg_id, phone, date, time, quantity, wish)

        for admin in admins:
            await bot.send_message(admin, f' НОВАЯ БРОНЬ в <b>{pub}!</b>\n\n'
                                          f'<b>Имя:</b> {name}\n'
                                          f'<b>Имя в тг:</b> {tg_name}\n'
                                          f'<b>tg:</b> {tg_link}\n'
                                          f'<b>Дата:</b> {date}\n'
                                          f'<b>Время:</b> {time}\n'
                                          f'<b>Количество:</b> {quantity}\n'
                                          f'<b>Комментарии:</b> {wish}\n'
                                          f'<b>Мобильный:</b> {phone}'
                                   , parse_mode='HTML')
        sleep(1)
        await bot.send_message(message.from_user.id, finish_message, reply_markup=kb_start, parse_mode='HTML')

    await state.finish()


def register_handlers_book(dp: Dispatcher):
    dp.register_callback_query_handler(cm_start, lambda c: c.data == 'book_a_table', state=None)
    dp.register_message_handler(cancel_book, state='*', commands="Покинуть бронирование 🔚")
    dp.register_message_handler(cancel_book, Text(equals='Покинуть бронирование 🔚', ignore_case=True), state='*')
    dp.register_message_handler(load_bar, state=Book.bar)
    dp.register_message_handler(load_name, state=Book.name)
    dp.register_message_handler(load_data, state=Book.data)
    dp.register_message_handler(load_time, state=Book.time)
    dp.register_message_handler(load_quantity, state=Book.quantity)
    dp.register_message_handler(load_wish, state=Book.wish)
    dp.register_message_handler(load_phone, state=Book.phone, content_types=[types.ContentType.CONTACT])
    dp.register_message_handler(load_phone, state=Book.phone)
