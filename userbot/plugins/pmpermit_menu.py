# if you change credits, you get anal cancer and get murdered by russians in 3 days.
"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: written by Indian Bhai {@pureindialover}
"""
import asyncio
import io 
import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in heroku vars"
PREV_REPLY_MESSAGE = {}


@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if event.is_private:
         
         PM = ("`𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐌𝐞𝐧𝐮 𝐎𝐟 𝐉𝐚𝐫𝐯𝐢𝐬 𝐌𝐚𝐝𝐞 𝐁𝐲,`"
               f"{DEFAULTUSER}.\n"
               "𝐋𝐞𝐭'𝐬 𝐦𝐚𝐤𝐞 𝐭𝐡𝐢𝐬 𝐬𝐦𝐨𝐨𝐭𝐡 𝐚𝐧𝐝 𝐥𝐞𝐭 𝐦𝐞 𝐤𝐧𝐨𝐰 𝐰𝐡𝐲 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐡𝐞𝐫𝐞.\n"
               "𝐂𝐡𝐨𝐨𝐬𝐞 𝐨𝐧𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 𝐫𝐞𝐚𝐬𝐨𝐧𝐬 𝐰𝐡𝐲 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐡𝐞𝐫𝐞:\n\n"
               "`1`. 𝐓𝐨 𝐂𝐡𝐚𝐭 𝐖𝐢𝐭𝐡 「 亗HAC͜͡KER亗 」\n"
               "`2`. 𝐓𝐨 𝐒𝐩𝐚𝐦 「 亗HAC͜͡KER亗 」'𝐬 𝐈𝐧𝐛𝐨𝐱.\n"

               "`3`. 𝐓𝐨 𝐄𝐧𝐪𝐮𝐢𝐫𝐞 𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠.\n"
               "`4`. 𝐓𝐨 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠.\n"
               "`5`. 𝐓𝐨 𝐆𝐢𝐯𝐞 𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠.")
         ONE = ("𝐎𝐤𝐚𝐲. 𝐘𝐨𝐮𝐫 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐞𝐝. 𝐃𝐨 𝐧𝐨𝐭 𝐬𝐩𝐚𝐦 𝐦𝐲 𝐦𝐚𝐬𝐭𝐞𝐫'𝐬 𝐢𝐧𝐛𝐨𝐱.𝐘𝐨𝐮 𝐜𝐚𝐧 𝐞𝐱𝐩𝐞𝐜𝐭 𝐚 𝐫𝐞𝐩𝐥𝐲 𝐰𝐢𝐭𝐡𝐢𝐧 24 𝐥𝐢𝐠𝐡𝐭 𝐲𝐞𝐚𝐫𝐬. 𝐇𝐞 𝐢𝐬 𝐚 𝐛𝐮𝐬𝐲 𝐦𝐚𝐧, 𝐮𝐧𝐥𝐢𝐤𝐞 𝐲𝐨𝐮 𝐩𝐫𝐨𝐛𝐚𝐛𝐥𝐲.\n\n"
                "𝐘𝐨𝐮 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐛𝐥𝐨𝐜𝐤𝐞𝐝 𝐚𝐧𝐝 𝐫𝐞𝐩𝐨𝐫𝐭𝐞𝐝 𝐢𝐟 𝐲𝐨𝐮 𝐬𝐩𝐚𝐦 𝐧𝐢𝐛𝐛𝐚.\n\n"
                "𝐔𝐬𝐞 `/start` 𝐭𝐨 𝐠𝐨 𝐛𝐚𝐜𝐤 𝐭𝐨 𝐭𝐡𝐞 𝐦𝐚𝐢𝐧 𝐦𝐞𝐧𝐮.")
         TWO = (" `███████████████████████████\n███████▀▀▀░░░░░░░▀▀▀███████\n████▀░░░░░░░░░░░░░░░░░▀████\n███│░░░░░░░░░░░░░░░░░░░│███\n██▌│░░░░░░░░░░░░░░░░░░░│▐██\n██░└┐░░░░░░░░░░░░░░░░░┌┘░██\n██░░└┐░░░░░░░░░░░░░░░┌┘░░██\n██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n██▌░│██████▌░░░▐██████│░▐██\n███░│▐███▀▀░░▄░░▀▀███▌│░███\n██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██\n██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n████▄─┘██▌░░░░░░░▐██└─▄████\n█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████\n█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████\n███████▄░░░░░░░░░░░▄███████\n██████████▄▄▄▄▄▄▄██████████\n███████████████████████████`\n\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐝𝐨 𝐧𝐨𝐭 𝐬𝐩𝐚𝐦 「 亗HAC͜͡KER亗 」'𝐬 𝐈𝐧𝐛𝐨𝐱 𝐮𝐧𝐥𝐞𝐬𝐬 𝐲𝐨𝐮 𝐰𝐢𝐬𝐡 𝐭𝐨 𝐛𝐞 𝐛𝐥𝐨𝐜𝐤𝐞𝐝 𝐚𝐧𝐝 𝐫𝐞𝐩𝐨𝐫𝐭𝐞𝐝.")
         THREE = (" `███████████████████████████\n███████▀▀▀░░░░░░░▀▀▀███████\n████▀░░░░░░░░░░░░░░░░░▀████\n███│░░░░░░░░░░░░░░░░░░░│███\n██▌│░░░░░░░░░░░░░░░░░░░│▐██\n██░└┐░░░░░░░░░░░░░░░░░┌┘░██\n██░░└┐░░░░░░░░░░░░░░░┌┘░░██\n██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n██▌░│██████▌░░░▐██████│░▐██\n███░│▐███▀▀░░▄░░▀▀███▌│░███\n██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██\n██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n████▄─┘██▌░░░░░░░▐██└─▄████\n█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████\n█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████\n███████▄░░░░░░░░░░░▄███████\n██████████▄▄▄▄▄▄▄██████████\n███████████████████████████`\n\n𝐒𝐨 𝐮𝐧𝐜𝐨𝐨𝐥, 𝐭𝐡𝐢𝐬 𝐢𝐬 𝐧𝐨𝐭 𝐲𝐨𝐮𝐫 𝐡𝐨𝐦𝐞. 𝐆𝐨 𝐛𝐨𝐭𝐡𝐞𝐫 𝐬𝐨𝐦𝐞𝐨𝐧𝐞 𝐞𝐥𝐬𝐞. 𝐉𝐚𝐫𝐯𝐢𝐬 𝐛𝐥𝐨𝐜𝐤𝐞𝐝 𝐚𝐧𝐝 𝐫𝐞𝐩𝐨𝐫𝐭𝐞𝐝 𝐘𝐨𝐮")
         FOUR = ("𝐎𝐤𝐚𝐲. 「 亗HAC͜͡KER亗 」 𝐡𝐚𝐬 𝐧𝐨𝐭 𝐬𝐞𝐞𝐧 𝐲𝐨𝐮𝐫 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐲𝐞𝐭.𝐇𝐞 𝐮𝐬𝐮𝐚𝐥𝐥𝐲 𝐫𝐞𝐬𝐩𝐨𝐧𝐝𝐬 𝐭𝐨 𝐩𝐞𝐨𝐩𝐥𝐞 𝐓𝐡𝐨𝐮𝐠𝐡 𝐢𝐝𝐤 𝐚𝐛𝐨𝐮𝐭 𝐫𝐞𝐭𝐚𝐫𝐭𝐞𝐝 𝐨𝐧𝐞𝐬.\n𝐇𝐞'𝐥𝐥 𝐫𝐞𝐬𝐩𝐨𝐧𝐝 𝐰𝐡𝐞𝐧 𝐡𝐞 𝐜𝐨𝐦𝐞𝐬 𝐛𝐚𝐜𝐤, 𝐢𝐟 𝐡𝐞 𝐰𝐚𝐧𝐭𝐬 𝐭𝐨.𝐓𝐡𝐞𝐫𝐞'𝐬 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐚 𝐥𝐨𝐭 𝐨𝐟 𝐩𝐞𝐧𝐝𝐢𝐧𝐠 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐝𝐨 𝐧𝐨𝐭 𝐬𝐩𝐚𝐦 「 亗HAC͜͡KER亗 」'𝐬 𝐈𝐧𝐛𝐨𝐱 𝐮𝐧𝐥𝐞𝐬𝐬 𝐲𝐨𝐮 𝐰𝐢𝐬𝐡 𝐭𝐨 𝐛𝐞 𝐛𝐥𝐨𝐜𝐤𝐞𝐝 𝐚𝐧𝐝 𝐫𝐞𝐩𝐨𝐫𝐭𝐞𝐝")
         FIVE = ("`𝐎𝐤𝐚𝐲. 𝐩𝐥𝐞𝐚𝐬𝐞 𝐡𝐚𝐯𝐞 𝐭𝐡𝐞 𝐛𝐚𝐬𝐢𝐜 𝐦𝐚𝐧𝐧𝐞𝐫𝐬 𝐚𝐬 𝐭𝐨 𝐧𝐨𝐭 𝐛𝐨𝐭𝐡𝐞𝐫 「 亗HAC͜͡KER亗 」 𝐭𝐨𝐨 𝐦𝐮𝐜𝐡. 𝐈𝐟 𝐡𝐞 𝐰𝐢𝐬𝐡𝐞𝐬 𝐭𝐨 𝐡𝐞𝐥𝐩 𝐲𝐨𝐮, 𝐡𝐞 𝐰𝐢𝐥𝐥 𝐫𝐞𝐬𝐩𝐨𝐧𝐝 𝐭𝐨 𝐲𝐨𝐮 𝐬𝐨𝐨𝐧.`\n𝐃𝐨 𝐧𝐨𝐭 𝐚𝐬𝐤 𝐫𝐞𝐩𝐞𝐚𝐭𝐝𝐥𝐲 𝐞𝐥𝐬𝐞 𝐲𝐨𝐮 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐛𝐥𝐨𝐜𝐤𝐞𝐝 𝐚𝐧𝐝 𝐫𝐞𝐩𝐨𝐫𝐭𝐞𝐝.")
         LWARN = ("𝐓𝐡𝐢𝐬 𝐢𝐬 𝐲𝐨𝐮𝐫 𝐥𝐚𝐬𝐭 𝐰𝐚𝐫𝐧𝐢𝐧𝐠. 𝐃𝐎 𝐍𝐎𝐓 𝐬𝐞𝐧𝐝 𝐚𝐧𝐨𝐭𝐡𝐞𝐫 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐞𝐥𝐬𝐞 𝐲𝐨𝐮 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐛𝐥𝐨𝐜𝐤𝐞𝐝 𝐚𝐧𝐝 𝐫𝐞𝐩𝐨𝐫𝐭𝐞𝐝. 𝐊𝐞𝐞𝐩 𝐩𝐚𝐭𝐢𝐞𝐧𝐜𝐞. 「 亗HAC͜͡KER亗 」 𝐰𝐢𝐥𝐥 𝐫𝐞𝐬𝐩𝐨𝐧𝐝 𝐲𝐨𝐮 𝐀𝐒𝐀𝐏.\n𝐂𝐥𝐢𝐜𝐤 `/𝐁𝐚𝐜𝐤 𝐓𝐨 𝐌𝐚𝐢𝐧 𝐌𝐞𝐧𝐮` 𝐓𝐨 𝐆𝐨 𝐁𝐚𝐜𝐤 𝐓𝐨 𝐓𝐡𝐞 𝐌𝐚𝐢𝐧 𝐌𝐞𝐧𝐮")
         B = (".block")
         XYZ = (" `███████████████████████████\n███████▀▀▀░░░░░░░▀▀▀███████\n████▀░░░░░░░░░░░░░░░░░▀████\n███│░░░░░░░░░░░░░░░░░░░│███\n██▌│░░░░░░░░░░░░░░░░░░░│▐██\n██░└┐░░░░░░░░░░░░░░░░░┌┘░██\n██░░└┐░░░░░░░░░░░░░░░┌┘░░██\n██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n██▌░│██████▌░░░▐██████│░▐██\n███░│▐███▀▀░░▄░░▀▀███▌│░███\n██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██\n██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n████▄─┘██▌░░░░░░░▐██└─▄████\n█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████\n█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████\n███████▄░░░░░░░░░░░▄███████\n██████████▄▄▄▄▄▄▄██████████\n███████████████████████████`\n\n𝐒𝐨 𝐮𝐧𝐜𝐨𝐨𝐥, 𝐭𝐡𝐢𝐬 𝐢𝐬 𝐧𝐨𝐭 𝐲𝐨𝐮𝐫 𝐡𝐨𝐦𝐞. 𝐆𝐨 𝐛𝐨𝐭𝐡𝐞𝐫 𝐬𝐨𝐦𝐞𝐨𝐧𝐞 𝐞𝐥𝐬𝐞. 𝐉𝐚𝐫𝐯𝐢𝐬 𝐛𝐥𝐨𝐜𝐤𝐞𝐝 𝐚𝐧𝐝 𝐫𝐞𝐩𝐨𝐫𝐭𝐞𝐝 𝐘𝐨𝐮")
     
        async with borg.conversation(chat) as conv:
         await borg.send_message(chat, PM)
         chat_id = event.from_id
         response = await conv.get_response(chat)
         y = response.text
         if y == "1":
             await borg.send_message(chat, ONE)
             response = await conv.get_response(chat)
             await event.delete()
             if not response.text == "/start":
                 await response.delete()
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 await event.delete()
                 await response.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "2":
             await borg.send_message(chat, B)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, TWO)
                 await asyncio.sleep(3)
                 await event.client(functions.contacts.BlockRequest(chat_id))
         

         elif y == "3":
             await borg.send_message(chat, FOUR)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 await event.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "4":
             await borg.send_message(chat,FIVE)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "5":
             await borg.send_message(chat,XYZ)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         else:
             await borg.send_message(chat, "`𝐘𝐨𝐮 𝐡𝐚𝐯𝐞 𝐞𝐧𝐭𝐞𝐫𝐞𝐝 𝐚𝐧 𝐢𝐧𝐯𝐚𝐥𝐢𝐝 𝐜𝐨𝐦𝐦𝐚𝐧𝐝. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 /𝐬𝐭𝐚𝐫𝐭 𝐚𝐠𝐚𝐢𝐧 𝐨𝐫 𝐝𝐨 𝐧𝐨𝐭 𝐬𝐞𝐧𝐝 𝐚𝐧𝐨𝐭𝐡𝐞𝐫 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐢𝐟 𝐲𝐨𝐮 𝐝𝐨 𝐧𝐨𝐭 𝐰𝐢𝐬𝐡 𝐭𝐨 𝐛𝐞 𝐛𝐥𝐨𝐜𝐤𝐞𝐝 𝐚𝐧𝐝 𝐫𝐞𝐩𝐨𝐫𝐭𝐞𝐝.`")
             response = await conv.get_response(chat)
             z = response.text
             if not z == "/start":
                 await borg.send_message(chat, LWARN)
                 await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))

