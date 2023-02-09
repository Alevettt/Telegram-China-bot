from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "BOT_TOKEN_HERE"

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda c: c.data == "usa")
async def usa_callback(callback_query: types.CallbackQuery):
    message = callback_query.message
    with open("audio/bad.mp3", "rb") as f:
        await bot.send_voice(chat_id=message.chat.id, voice=f)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="You bad citizen!!!")

@dp.callback_query_handler(lambda c: c.data == "china")
async def china_callback(callback_query: types.CallbackQuery):
    message = callback_query.message
    with open("audio/good.mp3", "rb") as f:
        await bot.send_voice(chat_id=message.chat.id, voice=f)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="You good citizen.")

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    keyboard = types.InlineKeyboardMarkup()
    usa_button = types.InlineKeyboardButton("🇺🇸 USA", callback_data="usa")
    china_button = types.InlineKeyboardButton("🇨🇳 China", callback_data="china")
    keyboard.add(usa_button, china_button)
    message_with_buttons = await bot.send_message(chat_id=message.chat.id, text="VERY IMPORTANT CHOICE!!!", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
