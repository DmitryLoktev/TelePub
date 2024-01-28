from aiogram import Bot, Dispatcher
from config import API_BEER
from aiogram.contrib.fsm_storage.memory import MemoryStorage
### Хранилище состояний бота
storage = MemoryStorage()

### Создание объекта бота и диспетчера для создания бота.
bot = Bot(API_BEER)
dp = Dispatcher(bot, storage=storage)
