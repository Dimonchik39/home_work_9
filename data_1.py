from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN
from anecAPI import anecAPI
import TicTacToe3 as T3



def start(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f''' Привет {first_name}. Опять ты!
Любишь шутки? Жми сюда: /joke
Я калькулятор шутник. Я могу:
/sum - сложить
/sub - вычесть
/div - разделить
/mul - умножить
За хорошее равенство получишь шутку!
Это не шутка :)
Введи команду из 2 чисел.
Пример: /sum 6 6

    ''')
    
def joke_fun(update: Update, context: CallbackContext):
    after_com = context.args
    update.message.reply_text(anecAPI.random_joke())
    print(after_com)

def tic_tac_toe(update: Update, context: CallbackContext):
    after_com = context.args
    update.message.reply_text(T3.play())
    print(after_com)

def summa(update, context):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        result = number1+number2
        update.message.reply_text((f'Ответ: {number1} + {number2} = {result}'))
        if (result) % 7 == 0:
            after_com = context.args
            update.message.reply_text(anecAPI.random_joke())
            print(after_com)
    except (IndexError, ValueError):
        update.message.reply_text('Введите 2 целых числа(через пробел) после команды')

def subtraction(update, context):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        result = number1-number2
        update.message.reply_text((f'Ответ: {number1} - {number2} = {result}'))
        if (result) % 5 == 0:
            after_com = context.args
            update.message.reply_text(anecAPI.random_joke())
            print(after_com)
    except (IndexError, ValueError):
        update.message.reply_text('Введите 2 целых числа(через пробел) после команды')

def division(update, context):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        try:
            result = number1/number2
        except ZeroDivisionError:
            update.message.reply_text('Не пытайся делить на ноль. Бесполезно!')

        update.message.reply_text((f'Ответ: {number1} / {number2} = {result}'))
        if (result) % 8 == 0:
            after_com = context.args
            update.message.reply_text(anecAPI.random_joke())
            print(after_com)
    except (IndexError, ValueError):
        update.message.reply_text('Введите 2 целых числа(через пробел) после команды')

def multiplication(update, context):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        result = number1*number2
        update.message.reply_text((f'Ответ: {number1} * {number2} = {result}'))
        if (result) % 3 == 0:
            after_com = context.args
            update.message.reply_text(anecAPI.random_joke())
            print(after_com)
    except (IndexError, ValueError):
        update.message.reply_text('Введите 2 целых числа(через пробел) после команды')
      
def catch_message(update: Update, context: CallbackContext):
    message = update.message.text
    first_name = update.message.chat.first_name
    if 'привет' in message.lower():
        update.message.reply_text(f'Доброго времени суток {first_name}')
        return None
    update.message.reply_text(f'Я умею повторять: {message}')
    print(message)

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
summa_handler = CommandHandler('sum', summa)
subtraction_handler = CommandHandler('sub', subtraction)
division_handler = CommandHandler('div', division)
multiplication_handler = CommandHandler('mul', multiplication)
ttt_handler = CommandHandler('ttt', tic_tac_toe)
fun_handler = CommandHandler('joke', joke_fun)
answer_handler = MessageHandler(Filters.text, catch_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(summa_handler)
dispatcher.add_handler(subtraction_handler)
dispatcher.add_handler(division_handler)
dispatcher.add_handler(multiplication_handler)
dispatcher.add_handler(ttt_handler)
dispatcher.add_handler(fun_handler)
dispatcher.add_handler(answer_handler)

print('Началось!')
updater.start_polling()
updater.idle()
