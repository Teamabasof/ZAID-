##Config
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'AgAj0wFPavV5LhgeeK2gu7LiX3bLApjj9Oq42JAQOUodAtPgR_o0DXbd0RPKm0Jsxz5sw49B3hupQyS4OfFwbzbff_BLQb7gEEywlosiHsVELhYnbmhgXIA8QdvwP6lg_QUqx4Eflowz6fxSwpeDKMNCpxNIDXSkgeNr2owRlLJaeGDbyLZFB26_QZEgIus2wkYg6sYayCqzrzYSPegLEybUuilod_6qbaS8D9dXDWVzWRAmM-2PNfQcmqB3kSOqCgDzLI6Y1pRH37VpwAFp2SbiOTX1Jm_E5Mo0CuSbPRQnTMtM5rmvOqSsGeqVg0lZCJajFCCZve_C7CM6umBjfo6FAAAAAUhXc-UA')
BOT_TOKEN = getenv('BOT_TOKEN', '5681957815:AAFu8TdIl9pYlQjSzm2r8rDL1TQqjxGyzGg')
API_ID = int(getenv("API_ID", "15954332"))
API_HASH = getenv('API_HASH', '85adea6f1eaf068b707703b4846a9ced')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", 'mongodb+srv://hiyplva100:hiyplva100@cluster0.p1vcumr.mongodb.net/?retryWrites=true&w=majority')
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '5134595693').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001737573985'))
ASS_ID = int(getenv("ASS_ID"))
OWNER_ID = list(map(int, getenv('OWNER_ID', '5134595693').split()))
RESULT_PIC = getenv('RESULT_PIC', "https://telegra.ph/file/62c6a23532aed6f4def02.jpg")
PLAYLIST_PIC = getenv('PLAYLIST_PIC', "https://telegra.ph/file/cf12b3276d8b2f1aefe48.jpg")
PING_IMG = getenv('PING_IMG', "https://telegra.ph/file/85c226cce124d25c5b2ad.jpg")
AUTO_LEAVE_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))
AUTO_LEAVE = getenv('AUTO_LEAVING_ASSISTANT', None)
