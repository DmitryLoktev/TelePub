from aiogram import types, Dispatcher
from create_bot import bot
from src.common.keys.Keys_week import kb_week, kb_back_to_week
from src.common.messages_bot.start_menu_messages import Week_message
from src.common.messages_bot.week_messages import monday_mich_photo, tuesday_photo, tuesday_message, wednesday_photo, \
    wednesday_message, koleso_message, koleso_photo, weekend_mich_photo, weekend_mich_message


### Вызов событий недели

# @dp.callback_query_handler(lambda c: c.data == 'week')
async def week_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, text=Week_message, reply_markup=kb_week)


async def monday_mich_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id

    await bot.send_photo(chat_id, photo=monday_mich_photo)
    await bot.send_message(chat_id, text=monday_mich_message, reply_markup=kb_back_to_week)


# @dp.callback_query_handler(lambda c: c.data == 'tuesday')
async def tuesday_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id

    await bot.send_photo(chat_id, photo=tuesday_photo)
    await bot.send_message(chat_id, text=tuesday_message, reply_markup=kb_back_to_week)


# @dp.callback_query_handler(lambda c: c.data == 'wednesday')
async def wednesday_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_photo(chat_id, photo=wednesday_photo)
    await bot.send_message(chat_id, text=wednesday_message, reply_markup=kb_back_to_week)


# @dp.callback_query_handler(lambda c: c.data == 'weekend')
async def koleso_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_photo(chat_id, photo=koleso_photo)
    await bot.send_message(chat_id, text=koleso_message, reply_markup=kb_back_to_week)


async def weekend_mich_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id

    await bot.send_photo(chat_id, photo=weekend_mich_photo)
    await bot.send_message(chat_id, text=weekend_mich_message, reply_markup=kb_back_to_week)


def register_handlers_week(dp: Dispatcher):
    dp.register_callback_query_handler(week_button, lambda c: c.data == 'week')
    dp.register_callback_query_handler(monday_mich_button, lambda c: c.data == 'monday_mich')
    dp.register_callback_query_handler(tuesday_button, lambda c: c.data == 'tuesday')
    dp.register_callback_query_handler(wednesday_button, lambda c: c.data == 'wednesday')
    dp.register_callback_query_handler(koleso_button, lambda c: c.data == 'weekend')
    dp.register_callback_query_handler(weekend_mich_button, lambda c: c.data == 'weekend1')
