from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME


bot = Client(
    ":rockerz:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "instance"},
)

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

calls = PyTgCalls(user, overload_quiet_mode=True)
