import logging

from aiogram import executor
from create_bot import dp
from src.common.db.models import async_main
from src.modules.handlers import beer_handler, week_handler
from src.modules.handlers import info_handlers, start_handler, food_handler, book_a_table

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def on_startup(_):
    await async_main()
    logger.info('Bot successfully enabled')


start_handler.register_handlers_menu(dp)
beer_handler.register_handlers_beer(dp)
food_handler.register_handlers_food(dp)
week_handler.register_handlers_week(dp)
info_handlers.register_handlers_info(dp)
book_a_table.register_handlers_book(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
