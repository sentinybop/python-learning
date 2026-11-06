import os
import asyncio
from dotenv import load_dotenv
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot, F, Dispatcher
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from zametkiSQL import sqlite
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
class StatusUser(StatesGroup):
    waiting = State()
load_dotenv()
token = os.getenv('BOT_TOKEN')
if token is None:
    raise SystemExit('bot token not found. check .env')
dp=Dispatcher()
c= sqlite('usersdb.db')
def build_menu(menuName): # все кнопки
    builder= InlineKeyboardBuilder()
    if menuName == '/start':
        builder.button(text='new note', callback_data='newnote')
        builder.button(text='view your notes', callback_data='viewnotes')
    elif menuName == 'back':
        builder.button(text='back', callback_data='back')
    elif menuName == 'VN':
        builder.button(text='delete note', callback_data='delnote')
        builder.button(text='delete all notes', callback_data='dellallnote')
        builder.button(text='back', callback_data='back')
    return builder    
@dp.message(Command('start')) # ответ с меню на start
async def cmd_start(message: Message):
    mainmenu=build_menu('/start')
    await message.answer("Hi it's notes bot, tap 1 button for add note and 2 to view all notes", reply_markup=mainmenu.as_markup())
@dp.callback_query(F.data == 'newnote')
async def newnote(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Enter your text for note')
    await state.set_state(StatusUser.waiting)
    await callback.answer()
@dp.message(StatusUser.waiting)
async def got_message(message: Message, state: FSMContext):
    user_id = message.from_user.id
    c.add_note(user_id, message.text)
    await message.answer(f"Your note,'{message.text}' has been added!", reply_markup=build_menu('/start').as_markup())
    await state.clear()
@dp.callback_query(F.data=='viewnotes')
async def viewnotes(callback: CallbackQuery):
    user_id = callback.from_user.id
    row = c.view_notes(user_id)
    notes = []
    if not row == 'notes not found':
        for i, (note_id, text) in enumerate(row, start=1):
            notes.append(f'{i}. {text}')
    result= '\n'.join(notes)
    await callback.message.edit_text(f'your notes:\n {result}', reply_markup=build_menu('VN').as_markup())
@dp.callback_query(F.data=='back')
async def back(callback: CallbackQuery):
    await callback.message.edit_text("Hi it's notes bot, tap 1 button for add note and 2 to view all notes", reply_markup=build_menu('/start').as_markup())
async def main(): # start bot
    bot = Bot(token=token)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

