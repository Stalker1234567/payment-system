from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class AdminFactory():
    action: str
    value: str

    @staticmethod
    def main_menu() -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        builder.button(text="First Button", callback_data=AdminFactory(action='get_active_list', value='announce'))

        builder.adjust(2)
        return builder.as_markup()


    # @staticmethod
    # def channel_keyboard_view(channels: list[]):