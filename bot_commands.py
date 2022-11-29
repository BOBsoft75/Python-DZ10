from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import math


# -> None:
async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi - приветствие\n/help - список команд\n/time - текущее время)\n/sum X Y - сложение X и Y\n/sqrt X Y - корень степени Y из X\n/pow - X в степени Y')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now().time()}')
    # await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    # print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')


async def sqrt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    # print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    z = pow(x, (1/y))
    await update.message.reply_text(f'Корень {y} степени из {x} равен {z}')


async def pow_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    # print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} в степени {y} равняется {x**y})')

    # await update.message.reply_text(f'{datetime.datetime.now().time()}')

# async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hi {update.effective_user.first_name}!')
