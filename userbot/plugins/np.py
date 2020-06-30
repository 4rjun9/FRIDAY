"""Emoji
Available Commands:
.np
Credits to @pureindialover
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("np"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0,65)
    #input_str = event.pattern_match.group(1)
   # if input_str == "np":
    await event.edit("np")
    animation_chars = [
            "😎",
            "☠️",
            "😈",
            "Loading.",
            "Loading..",
            "Loading...",
            "Loading....",
            "Loading.....",
            "𝐍𝐨....",
            "𝐍𝐨 𝐨𝐧𝐞....",
            "𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧....",
            "𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩....",
            "𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩 𝐦𝐞....",
            "𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩 𝐦𝐞 𝐍𝐨....",
            "𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩 𝐦𝐞 𝐍𝐨 𝐨𝐧𝐞....",
            "𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩 𝐦𝐞 𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧....",
            "𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩 𝐦𝐞 𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩....",
            "𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩 𝐦𝐞 𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩 𝐭𝐡𝐞....",
            "𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩 𝐦𝐞 𝐍𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐬𝐭𝐨𝐩 𝐭𝐡𝐞 𝐟𝐮𝐭𝐮𝐫𝐞😈",
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 25])
