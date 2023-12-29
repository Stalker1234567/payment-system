from aiogram.filters import Filter
from aiogram.types import Message

from bot.core.configuration import Configuration

class Admin(Filter):
    async def __call__(self, message: Message):
        return str(message.from_user.id) in Configuration.get_admins()