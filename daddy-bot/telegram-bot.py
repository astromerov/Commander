import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6484238483:AAHEUF9m6Bx53y2xLWfFUGL6WnJfB6YNyL8'

# Create an instance of the Bot
bot = telebot.TeleBot(TOKEN)

# Function to handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! You can find more about me at https://www.t.me/astromerov.")

# Function to handle the /help command
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "This is a simple bot. Use /start to get started and /learn to learn more.")

# Function to handle the /learn command
@bot.message_handler(commands=['learn'])
def learn(message):
    bot.send_message(message.chat.id, "You can learn more about me at https://www.t.me/astromerov.")

# Start the bot
bot.polling()
