from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz(message: types.Message):
    button_quiz = InlineKeyboardMarkup(row_width=1)

    button_quiz.add(InlineKeyboardButton("Дальше!", callback_data="button_1"))

    question = 'Дарк соулс 1 или пошел нахуй'

    answer = ['Dark souls 1', 'pohui kazual', 'fear and hunger(ebanat)']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='eblan suka tupoi',
        open_period=60,
        reply_markup=button_quiz

    )


async def quiz_2(call: types.CallbackQuery):
    button_quiz = InlineKeyboardMarkup(row_width=1)

    button_quiz.add(InlineKeyboardButton("Дальше!", callback_data="button_2"))

    question = 'Лучшая игра на свете'

    answer = ['КС срака', 'дота хуета', 'влорант хуета', 'ФОРТНАЙТ', 'ДАРКСОООУУУЛС']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=4,
        explanation='ОЙОЙОЙ ПИДАРААААЗ',
        open_period=60,
        reply_markup=button_quiz

    )


async def quiz_3(call: types.CallbackQuery):

    question = 'Best album of all time'

    answer = ['the great dismal', 'the wall', 'dont mind the bollocks its sex pistols']

    await bot.send_photo(chat_id=call.from_user.id,
                         photo='https://pbs.twimg.com/media/GJslnQ7XIAA9h--?format=jpg&name=large')

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='OOOOOOOO TUPOOOI SUKA',
        open_period=60,

    )


def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=["quiz"])
    dp.register_callback_query_handler(quiz_2, text='button_1')
    dp.register_callback_query_handler(quiz_3, text='button_2')
