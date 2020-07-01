from userbot import CMD_LIST
from userbot.utils import admin_cmd

@command(pattern="^.help ?(.*)")
#@borg.on(admin_cmd(pattern=r"help ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "⚡ " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                with io.BytesIO(str.encode(string)) as out_file:
                    out_file.name = "cmd.txt"
                    await bot.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption="𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒",
                        reply_to=reply_to_id
                    )
                    await event.delete()
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐅𝐨𝐮𝐧𝐝 𝐈𝐧 {}:".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + " is not a valid plugin!")
        else:
            help_string = """𝐉𝐚𝐫𝐯𝐢𝐬\n𝐎𝐰𝐧𝐞𝐫 [「 亗HAC͜͡KER亗 」](https://t.me/Official_White_Devil)\n`𝐉𝐚𝐫𝐯𝐢𝐬 𝐑𝐞𝐯𝐞𝐚𝐥𝐞𝐝 𝐀𝐥𝐥 𝐏𝐥𝐮𝐠𝐢𝐧𝐬`"""
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername,
                help_string
            )
            await results[0].click(
                event.chat_id,
                reply_to=event.reply_to_msg_id,
                hide_via=True
            )
            await event.delete()
