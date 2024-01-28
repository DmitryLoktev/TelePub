from create_bot import bot
from aiogram import Dispatcher
from aiogram import types

from src.common.keys.keys_start_menu import kb_start
from src.common.messages_bot.info_message import info_message


async def info_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, text= info_message, reply_markup=kb_start, parse_mode='HTML')


def register_handlers_info(dp: Dispatcher):
    dp.register_callback_query_handler(info_button, lambda c: c.data == 'info')


