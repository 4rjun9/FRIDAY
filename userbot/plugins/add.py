"""Invite the user(s) to the current chat
Syntax: .invite <User(s)>"""

from telethon import functions
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="add ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit("`.invite` 𝐔𝐬𝐞𝐫 𝐓𝐨 𝐀 𝐂𝐡𝐚𝐭, 𝐍𝐨𝐭 𝐓𝐨 𝐀 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("𝐈𝐧𝐯𝐢𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("𝐈𝐧𝐯𝐢𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲")
