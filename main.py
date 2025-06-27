import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

import config, getweather

# Объект бота
bot = Bot(token=config.token)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start", "help"))
async def cmd_start(message: types.Message):
    await message.reply(f"Hello, {message.from_user.full_name}")


# Хендлер на директ
@dp.message()
async def private(message: types.Message):
    if message.chat.type == 'private':
        try:
            await message.reply(str(getweather.get_location(message.text)))
        except Exception as err:
            return err
    return None


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())