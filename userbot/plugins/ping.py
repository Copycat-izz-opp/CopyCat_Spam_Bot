from userbot import bot 
from datetime import datetime
import time
from ..Config import Config

## NO NEED TO TOUCH THIS ##
ALIVE_NAME = Config.ALIVE_NAME
ID = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
USER = str(ALIVE_NAME) if ALIVE_NAME else "Copycat User"
### End ##
## mention ##
mentionuser = f"[{USER}](tg://user?id={ID})"
## End ##

@bot.on(admin_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))

async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "â¢PONGâ¢")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"""
    ||â¢ðð¢ð£ð¬ððð§ ð¦ð£ðð  ðð¢ð§â¢||
â­ââââ®â±â±â±â±â±â±â±â±â±â±â±â±
ââ­ââ®ââ±â±â±â±â±â±â±â±â±â±â±â±
ââ°ââ¯ââ­âââ®â­âââ®â­âââ®
ââ­âââ¯ââ­â®âââ­â®âââ­â®â
âââ±â±â±ââ°â¯âââââââ°â¯â
â°â¯â±â±â±â°âââ¯â°â¯â°â¯â°ââ®â
â±â±â±â±â±â±â±â±â±â±â±â±â±â­ââ¯â
â±â±â±â±â±â±â±â±â±â±â±â±â±â°âââ¯\n\n
   MY MS â `{ms}`\n
    ð²âð  ð²âðÕá´ð¸â  â {mentionuser}
    """)

# By @Alone_loverboy 
# Don't Steal Credit else gay
# Credit lena wale ki maa ki ch*t ð