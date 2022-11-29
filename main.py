from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

# async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


app = ApplicationBuilder().token(
    "YOUR TOKEN HERE").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sqrt", sqrt_command))
app.add_handler(CommandHandler("pow", pow_command))

print('Сервер запущен.')
app.run_polling()
