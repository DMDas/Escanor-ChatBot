# Imports all your secret keys (like 'Bot_Api' and 'my_id') from the config.py file
from config import *

# Imports the library that lets you build a Telegram bot
import telebot

# --- (Initialization) ---

# Creates the bot object using your API key from the config file
bot = telebot.TeleBot(Bot_Api)

# A variable to store a log of the chat (it's not used as AI memory)
chatStr = ""

# --- (This function talks to the Google AI) ---
# It's missing the 'model' definition from your previous code.
def ChatModel(prompt):
    # Use the 'chatStr' variable from outside this function
    global chatStr
    # Add the user's new message to the log string
    chatStr += f"User: {prompt}\nAssistant: "

    try:
        # Send the user's prompt to the Gemini model to get a response
        # (This line will fail because 'model' isn't defined in this snippet)
        response = model.generate_content([{"role": "user", "parts": [prompt]}])
        
        # Get just the text part of the AI's answer
        text = response.text
        
        # Add the AI's answer to the log string
        chatStr += text
        
        # Print the full AI response to your terminal (for debugging)
        print(response)
        
        # Send the clean text reply back
        return text
    except Exception as e:
        # If the AI or API has an error, return the error message
        return f"⚠️ Error: {str(e)}"

# --- (Bot Commands) ---

# This function runs when a user types the /start command
@bot.message_handler(commands=['start'])
def start(message):
    # The bot replies with this welcome message
    bot.reply_to(message, "Welcome To My World! I am EscanorLionSin 🤖 (Gemini Edition)")

# This function runs when a user types the /myid command
@bot.message_handler(commands=['myid'])
def get_id(message):
    # The bot replies with the user's personal Telegram ID
    bot.reply_to(message, f"Your Telegram ID is: {message.from_user.id}")

# --- (Main Chat Handler) ---

# This function runs for ANY text message that isn't a command
@bot.message_handler(func=lambda message: True)
def chat(message):
    
    # --- This is the security check ---
    # It checks if the message sender's ID matches YOUR ID (from the config file)
    if message.from_user.id == MY_ID:
        
        # --- If it IS you ---
        try:
            # 1. Get a reply from the Gemini AI
            reply = ChatModel(message.text)
            # 2. Send the AI's reply back to you
            bot.reply_to(message, reply)
            
        except Exception as e:
            # If anything breaks, print the error and send it to you
            print(e)
            bot.reply_to(message, f"⚠️ {str(e)}")
            
    else:
        # --- If it is NOT you ---
        
        # 1. Print a warning to your terminal
        print(f"Unauthorized access attempt by ID: {message.from_user.id}")
        
        # 2. Send a "blocked" message to the other user
        bot.reply_to(message, "🚫 Unauthorized! You are not allowed to use this bot.")

# --- (Start the Bot) ---

# Print a message in the terminal to show the bot is online
print("Gemini Bot Started.... 🚀")

# This starts the bot. It will run forever, checking for new messages.
bot.polling()