import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utilites import MyStates
from messages import MESSAGES
from User import User

bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot, storage=MemoryStorage())
USERS = {}


# @dp.message_handler(state=MyStates.STATE_0)
# async def start(message: types.Message):
#
#     await bot.send_message(chat_id=message.from_user.id, text=MESSAGES['start'])


@dp.message_handler(state=MyStates.STATE_1)
async def name(message: types.Message):
    chat_id = message.from_user.id
    USERS[chat_id].name = message.text
    text = f'Очень приятно {message.text}\n{MESSAGES["age"]}'

    state = dp.current_state(user=chat_id)
    await state.set_state(MyStates.all()[2])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(state=MyStates.STATE_2)
async def age(message: types.Message):
    chat_id = message.from_user.id
    if message.text.isdigit():
        USERS[chat_id].age = message.text
        text = f'Спасибо\n{MESSAGES["email"]}'
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[3])
    else:
        text = 'Попробуй все таки число'
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(state=MyStates.STATE_3)
async def email(message: types.Message):
    chat_id = message.from_user.id
    USERS[chat_id].email = message.text
    print(type(USERS[chat_id]))
    text = f'Спасибо за регистрацию {USERS[chat_id].name}\n'

    state = dp.current_state(user=chat_id)
    await state.set_state(MyStates.all()[4])
    await bot.send_message(chat_id=message.from_user.id, text=text)
    await menu(message)


@dp.message_handler(state=MyStates.STATE_4)
async def menu(message: types.Message):
    chat_id = message.from_user.id
    text = f'Главное меню'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.insert(types.KeyboardButton("Кнопка"))
    await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=keyboard)


@dp.message_handler()
async def default(message: types.Message):
    chat_id = message.from_user.id
    if chat_id not in USERS.keys():
        USERS.update({chat_id: User(chat_id)})
        print(User(234))
        state = dp.current_state(user=chat_id)
        await state.set_state(MyStates.all()[1])
        print(await state.get_state())
    await bot.send_message(chat_id=message.from_user.id, text=f'{MESSAGES["start"]}\n{MESSAGES["name"]}')


@dp.message_handler(state='*')
async def all(message: types.Message):
    chat_id = message.from_user.id
    state = dp.current_state(user=chat_id)
    # await state.set_state(MyStates.STATE_1)
    # await state.reset_state()
    print(await state.get_state())
    await bot.send_message(chat_id=message.from_user.id, text='all states')


if __name__ == '__main__':
    executor.start_polling(dp)
