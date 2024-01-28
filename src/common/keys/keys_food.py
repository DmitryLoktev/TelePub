from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
### Клавиатура: Меню бота -> Что поесть ? ('food')

menu_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Меню бота 🟢', callback_data='menu')
msk_food_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Меню кухни на Московской 📃', callback_data='menu_food_msk')
mich_food_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Меню кухни на Мичурина 📃', callback_data='menu_food_mich')
kb_food: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[msk_food_button], [mich_food_button], [menu_button]])

### Клавиатура: Меню бота -> Что поесть ? -> Меню кухни на Московской

snacks_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Снэки 🍺', callback_data='snacks')
burger_button: InlineKeyboardButton = InlineKeyboardButton(text='Бургеры/Сендвичи 🍔', callback_data='burger')
steak_button: InlineKeyboardButton = InlineKeyboardButton(text='Стейки 🥩', callback_data='steak')
pizza_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Пиццы 🍕', callback_data='pizza')
dishes_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Горячие блюда и салаты 🫕', callback_data='dishes')
msk_food_back_button:  InlineKeyboardButton = InlineKeyboardButton(text= 'Назад🔙', callback_data='food')     ### Клавиатура: Меню бота -> Что поесть ?

kb_food_msk: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[snacks_button], [burger_button], [pizza_button], [steak_button], [dishes_button], [msk_food_back_button]])


###Клавиатура: Меню бота -> Что поесть ? -> Меню кухни на Московской -> *любой раздел*. (Возвращает на предыдущую сцену)
food_menu_button: InlineKeyboardButton = InlineKeyboardButton(text= 'Назад🔙', callback_data='menu_food_msk')

kb_back_to_msk_food: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[food_menu_button], [menu_button]])

###Клавиатура: Меню бота -> Что поесть ? -> Меню кухни на Мичурина (Возвращает на предыдущую сцену)
food_menu_button2: InlineKeyboardButton = InlineKeyboardButton(text= 'Назад🔙', callback_data='food')
kb_back_to_food: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[food_menu_button2], [menu_button]])