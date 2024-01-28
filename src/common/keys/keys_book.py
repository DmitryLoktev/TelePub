import aiogram
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import types
#### Данные клавиатуры выпадают при заполнении формы брони столика.

drop = "Покинуть бронирование 🔚"
skip = 'Пропустить ❌'
msk = 'Декабрист на Московской'
mcrn = 'Декабрист на Мичурина'

#### Выбор бара
kb_bar = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_bar.add(msk).add(mcrn).add(drop)

#### Время брони
time1 = ['14:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00', '18:00 - 19:00']
time_buttons1 = [KeyboardButton(i) for i in time1]
time2 = ['19:00 - 20:00', '20:00 - 21:00', '21:00 - 22:00', '23:00 - 00:00']
time_buttons2 = [KeyboardButton(i) for i in time2]

kb_time = ReplyKeyboardMarkup(keyboard=[time_buttons1, time_buttons2], resize_keyboard=True, one_time_keyboard=True)
kb_time.add(drop)

#### Количество человек
quantity1 = [str(i) for i in range(1, 6)]
quantity_buttons1 = [KeyboardButton(i) for i in quantity1]

quantity2 = [str(i) for i in range(6, 11)]
quantity_buttons2 = [KeyboardButton(i) for i in quantity2]

quantity3 = [str(i) for i in range(11, 16)]
quantity_buttons3 = [KeyboardButton(i) for i in quantity3]

quantity4 = ['16-18', '19-21', '22-24', '25-30', '30+']
quantity_buttons4 = [KeyboardButton(style) for style in quantity4]

kb_quantity = ReplyKeyboardMarkup(keyboard=[quantity_buttons1, quantity_buttons2, quantity_buttons3, quantity_buttons4]
                                  , resize_keyboard=True, one_time_keyboard=True)
kb_quantity.add(drop)

#### Клавиатура пропуска и выхода
kb_skip = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=True)
kb_skip.add(KeyboardButton(skip)).add(drop)

#### Клавиатура сцена номера телефона
kb_phone = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=True)
item = aiogram.types.KeyboardButton("Отправить номер телефона ☎️", request_contact=True)
kb_phone.add(item).add(KeyboardButton(skip)).add(drop)

#### Клавиатура выхода из брони
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_cancel.add(drop)