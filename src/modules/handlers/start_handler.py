from aiogram import types, Dispatcher
from create_bot import bot
from src.common.messages_bot.start_menu_messages import Start_message, Menu_message
from src.common.keys.keys_start_menu import kb_start, kb_menu_bot


### Начало работы

# @dp.message_handler(commands=['start'])
async def start_button(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=Start_message, reply_markup=kb_start)


### Вызов Меню бота

# @dp.callback_query_handler(lambda c: c.data == 'menu')
async def menu_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, text=Menu_message, reply_markup=kb_menu_bot)


def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(start_button, commands='start')
    dp.register_callback_query_handler(menu_button, lambda c: c.data == 'menu')
