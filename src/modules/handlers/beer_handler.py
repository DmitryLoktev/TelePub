from src.common.db.models import Moskovskaya, Michurina, BottledBeer
from src.common.db.requests import add_user, get_tapboard, format_table, get_bottled
import datetime
from aiogram import types, Dispatcher
from create_bot import bot
import time

from src.common.keys.keys_beer import kb_beers_menu, kb_beer1, kb_beer3, kb_beer2
from src.common.messages_bot.bot_messages import remember_message
from src.common.messages_bot.start_menu_messages import Beer_message
from src.common.messages_bot.stickers import hi_beer_sticker


### Вызов Меню пива
# @dp.callback_query_handler(lambda c: c.data == 'beer')
async def beer_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_sticker(chat_id, sticker=hi_beer_sticker)
    time.sleep(1)
    await bot.send_message(chat_id, text=Beer_message, reply_markup=kb_beers_menu)

    # Получаем информацию о пользователе
    tg_id = callback_query.message.chat.id
    tg_name = callback_query.message.chat.full_name
    td_link_way = callback_query.message.chat.username
    tg_link = f"https://t.me/{td_link_way}" if td_link_way else "N/A"
    time_on = datetime.datetime.now()

    await add_user(tg_link, tg_name, tg_id, time_on)


# @dp.callback_query_handler(lambda c: c.data == 'draftbeer')
async def draftbeer_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    beer_table = await get_tapboard(Moskovskaya)
    print(beer_table)
    format_row = format_table(beer_table)
    await bot.send_message(chat_id, format_row, parse_mode='HTML')
    await bot.send_message(chat_id, remember_message, parse_mode='HTML', reply_markup=kb_beer1)


async def draftbeer_mich_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    beer_table = await get_tapboard(Michurina)
    format_row = format_table(beer_table)
    await bot.send_message(chat_id, format_row, parse_mode='HTML')
    await bot.send_message(chat_id, remember_message, parse_mode='HTML', reply_markup=kb_beer3)


# @dp.callback_query_handler(lambda c: c.data == 'topbottledbeer')
async def bottled_button(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    beer_table = await get_bottled(BottledBeer)

    beer_info = []
    for beer in beer_table:
        beer_info.append(f"♦️ *{beer.name}*\n{beer.description}\n[Глянуть в Untappd]({beer.untpd})\n")

    beer_text = "\n".join(beer_info)

    await bot.send_message(chat_id, beer_text, parse_mode="Markdown", reply_markup=kb_beer2)


def register_handlers_beer(dp: Dispatcher):
    dp.register_callback_query_handler(beer_button, lambda c: c.data == 'beer')
    dp.register_callback_query_handler(draftbeer_button, lambda c: c.data == 'draftbeer')
    dp.register_callback_query_handler(draftbeer_mich_button, lambda c: c.data == 'draftbeer_mich')
    dp.register_callback_query_handler(bottled_button, lambda c: c.data == 'topbottledbeer')
