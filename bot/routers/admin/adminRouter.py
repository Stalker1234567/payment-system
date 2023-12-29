from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.core.database import DataBase
from bot.core.keyboards import AdminFactory
from bot.core.filters import Admin

main_router = Router()

@main_router.message(Admin(), Command(commands=['start', 'admin']))
async def start(message: Message, state: FSMContext):
    logging.info(f"user [ {message.from_user.id} ] {message.from_user.username}")
    await message.answer("Admin Panel", reply_markup=AdminFactory.main_menu())
    await state.clear()

@main_router.callback_query(AdminFactory.filter(F.action=='open' and F.value=='admin'))
async def admin_panel(callback: CallbackQuery):
    await callback.message.edit_text(
        "Admin Panel",
        reply_markup=AdminFactory.main_menu()
    )