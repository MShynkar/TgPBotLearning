from aiogram import Bot, Dispatcher, types, executor


with open("token.txt", "r") as f:
    TOKEN = f.read()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# @dp.message_handler()
# async def echo(message: types.Message):
#     #uppercase echo
#     await message.answer(message.text.upper())

@dp.message_handler()
async def echo(message: types.Message):
    #two words echo
    if message.text.count(" ") >= 1: 
        await message.answer(message.text)
    else:
        await message.answer("Не браток, не піде")

if __name__ == "__main__":
    executor.start_polling(dp)


