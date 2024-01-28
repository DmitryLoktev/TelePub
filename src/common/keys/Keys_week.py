from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
### Клавиатура: Меню бота ->  События и акции на неделе.


monday_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Акция в понедельник на Мичурина 🍟', callback_data='monday_mich')

tuesday_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Акция во вторник на Московской🍾', callback_data='tuesday')

wednesday_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Акция в среду на Московской🍗', callback_data='wednesday')

weekend_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Лотерея в пятницу на Московской 🎉', callback_data='weekend')

weekend_button1:  InlineKeyboardButton = InlineKeyboardButton(text= 'Пятничное блюдо на Мичурина 🦪', callback_data='weekend1')

menu_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Меню бота 🟢', callback_data='menu')

kb_week: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[monday_button], [tuesday_button], [wednesday_button], [weekend_button1], [weekend_button], [menu_button]])


### Клавиатура: Меню бота ->  События и акции на неделе -> *любой день недели*.
back_to_week: InlineKeyboardButton = InlineKeyboardButton(text= 'К другим дням недели 📆', callback_data='week')
kb_back_to_week: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[back_to_week], [menu_button]])