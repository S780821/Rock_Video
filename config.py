import os
from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SESSION_NAME = getenv("SESSION_NAME", "session")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/S780821/Rock_Video")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Rockerz_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Rockerz_Updates")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/0d0cd252270861a6838ce.jpg")
IMG_2 = getenv("IMG_2","https://telegra.ph/file/0d0cd252270861a6838ce.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/0d0cd252270861a6838ce.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/0d0cd252270861a6838ce.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/0d0cd252270861a6838ce.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/0d0cd252270861a6838ce.jpg")
