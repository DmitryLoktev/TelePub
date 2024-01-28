from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


### Клавиатура: /start

menu_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Меню бота 🟢', callback_data='menu')

kb_start: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[menu_button]])


### Клавиатура: /start -> Меню бота

beer_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Что выпить? 🍺', callback_data='beer')
food_button: InlineKeyboardButton = InlineKeyboardButton(text='Что поесть? 🍽', callback_data='food')
week_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'События и акции на неделе  📆', callback_data='week')
table_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Забронировать столик 📲', callback_data ='book_a_table')
info_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Информация о барах 📝', callback_data='info')

kb_menu_bot: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[beer_button], [food_button], [week_button], [table_button], [info_button]])









