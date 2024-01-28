from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


### Меню бота -> Что выпить?
menu_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Меню бота 🟢', callback_data='menu')
draft_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Московская. Что на кранах? 🍻', callback_data='draftbeer')
draft_button2:  InlineKeyboardButton = InlineKeyboardButton(text= 'Мичурина. Что на кранах? 🍻', callback_data='draftbeer_mich')
bottle_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Московская. Подборка недели в банках и бутылках 🍾', callback_data='topbottledbeer')

kb_beers_menu: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[draft_button], [draft_button2], [bottle_button], [menu_button]])

### ### Меню бота -> Что выпить?  -> Московская. Что на кранах?

kb_beer1: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[draft_button2], [bottle_button], [menu_button]])

### Меню бота -> Что выпить?  -> Московская. Что на кранах? 'Московская. Подборка недели в банках и бутылках 🍾'

kb_beer2: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[draft_button], [draft_button2], [menu_button]])

### ### Меню бота -> Что выпить?  -> Мичурина. Что на кранах?
kb_beer3: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[draft_button], [bottle_button], [menu_button]])