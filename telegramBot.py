from aiogram.utils import executor
from createBot import dp
from handlers import register_handlers

register_handlers(dp)

#запуск бота
executor.start_polling(dp, skip_updates=True)

