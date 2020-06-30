"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

@command(outgoing=True, pattern="^.jarvis$")
async def amireallyalive(alive):
    """ For .jarvis command, check if the bot is running.  """
    await alive.edit("`𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐉𝐚𝐫𝐯𝐢𝐬☣️️\n𝐉𝐚𝐫𝐯𝐢𝐬 𝐈𝐬 𝐑𝐮𝐧𝐧𝐢𝐧𝐠♨️\n𝐉𝐚𝐫𝐯𝐢𝐬 𝐂𝐨𝐧𝐭𝐫𝐨𝐥𝐥𝐢𝐧𝐠 𝐒𝐲𝐬𝐭𝐞𝐦⚙️\n𝐋𝐨𝐚𝐝𝐞𝐝 𝐂𝐡𝐚𝐭'𝐬 - 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬 - 𝐆𝐫𝐨𝐮𝐩'𝐬💬\n`"
                     f"`𝐎𝐰𝐧𝐞𝐫` -:-  {DEFAULTUSER}\n"
                     "`𝐉𝐚𝐫𝐯𝐢𝐬 - 𝐕𝐞𝐫𝐬𝐢𝐨𝐧⚙️ -:- 6.9.0\n𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 - 𝐏𝐚𝐭𝐜𝐡⚙️ -:- 3.7.3\n`\n"
                     "`𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 𝐒𝐭𝐚𝐭𝐮𝐬 -:- 𝐒𝐲𝐬𝐭𝐞𝐦 𝐒𝐞𝐜𝐮𝐫𝐞𝐝🛡️\n𝐒𝐲𝐬𝐭𝐞𝐦 𝐈𝐬 𝐒𝐞𝐜𝐮𝐫𝐞𝐝 -:- 24/7🛡️\n`"
                     "")
