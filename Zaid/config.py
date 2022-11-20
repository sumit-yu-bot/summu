##Config
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'BQBa1twSr7GwBqVgA2cdxK4xnt8zTSoYuPvmch0HQ-KgmEbn238U6Dhv0XDubJU5YSbL9FcDRRE10J3ivyD6NBUHlIZQpBmOtrEY4iKD1qLcpyLzFEwRgaGD4ydKxZLDYqMyw6PQc69SvQl1HbYGH4s5qNY6Cp2b780mFaXXtD-NG-oG76ca5kh3tSAEA_3CibOKOgho0hR-D0vjOjZecMd71kVfj2-U3I9TG4vv0zwJHTdQwUtNF5I-qfuDQmsgZ81A8G5pqjEG9rD7WLzQUMOpatLbwHLPJ3_ELOo05AFpK-Mebg5xGq41ScsjI0Rp-eP_RJCBFLuvMwkh-_nCx3a-AAAAAUqDigcA')
BOT_TOKEN = getenv('BOT_TOKEN', '5667013817:AAEp9ZEBF6C2bfN9D4Om2xLrOv0dwyNMTW8')
API_ID = int(getenv("API_ID", "14200983"))
API_HASH = getenv('API_HASH', 'f4ac6bbb4e38945379da8ae5a6778e68')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Belly:belly55@atlascluster.ends7zl.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '2139088940').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001573996982'))
ASS_ID = int(getenv("ASS_ID" ,'5677369478'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '2139088940').split()))
RESULT_PIC = getenv('RESULT_PIC', "https://telegra.ph/file/62c6a23532aed6f4def02.jpg")
PLAYLIST_PIC = getenv('PLAYLIST_PIC', "https://telegra.ph/file/cf12b3276d8b2f1aefe48.jpg")
PING_IMG = getenv('PING_IMG', "https://te.legra.ph/file/8eb3466b2e2fc39263665.jpg")
AUTO_LEAVE_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))
AUTO_LEAVE = getenv('AUTO_LEAVING_ASSISTANT', None)
