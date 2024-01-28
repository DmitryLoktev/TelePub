from aiogram import types, Dispatcher
from create_bot import dp, bot
import datetime

from src.common.keys.keys_food import kb_food, kb_back_to_food, kb_food_msk, kb_back_to_msk_food
from src.common.messages_bot.food_messages import food_message, food_mich_message, snacks_message, burgers_message, \
    steak_message, pizza_message, dishes_message


### Вызов меню кухни
@dp.callback_query_handler(lambda c: c.data == 'food')
async def food_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    tg_id = callback_query.message.chat.id
    tg_name = callback_query.message.chat.full_name
    td_link_way = callback_query.message.chat.username
    tg_link = f"https://t.me/{td_link_way}" if td_link_way else "N/A"
    time_on = datetime.datetime.now()


    await bot.send_message(chat_id, text= food_message, reply_markup=kb_food)


async def food_msk_button(callback_query: types.CallbackQuery):

    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, text= food_message, reply_markup=kb_food_msk)


async def food_mich_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, text=food_mich_message, reply_markup=kb_back_to_food)

@dp.callback_query_handler(lambda c: c.data == 'snacks')
async def snacks_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, text=snacks_message, reply_markup=kb_back_to_msk_food)

@dp.callback_query_handler(lambda c: c.data == 'burger')
async def burger_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, text=burgers_message, reply_markup=kb_back_to_msk_food)

@dp.callback_query_handler(lambda c: c.data == 'steak')
async def steak_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, text=steak_message, reply_markup=kb_back_to_msk_food)

@dp.callback_query_handler(lambda c: c.data == 'pizza')
async def pizza_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, text=pizza_message, reply_markup=kb_back_to_msk_food)

@dp.callback_query_handler(lambda c: c.data == 'dishes')
async def dishes_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, text=dishes_message, reply_markup=kb_back_to_msk_food)




def register_handlers_food(dp : Dispatcher):
    dp.register_callback_query_handler(food_button, lambda c: c.data == 'food')
    dp.register_callback_query_handler(food_msk_button, lambda c: c.data == 'menu_food_msk')
    dp.register_callback_query_handler(food_mich_button, lambda c: c.data == 'menu_food_mich')
    dp.register_callback_query_handler(snacks_button, lambda c: c.data == 'snacks')
    dp.register_callback_query_handler(burger_button, lambda c: c.data == 'burger')
    dp.register_callback_query_handler(steak_button, lambda c: c.data == 'steak')
    dp.register_callback_query_handler(pizza_button, lambda c: c.data == 'pizza')
    dp.register_callback_query_handler(dishes_button, lambda c: c.data == 'dishes')
