"""Update UserBot code
Syntax: .update"""

import git
from contextlib import suppress
import os
import sys
import asyncio
from userbot.utils import admin_cmd

# -- Constants -- #
IS_SELECTED_DIFFERENT_BRANCH = (
    "𝐥𝐨𝐨𝐤𝐬 𝐥𝐢𝐤𝐞 𝐚 𝐜𝐮𝐬𝐭𝐨𝐦 𝐛𝐫𝐚𝐧𝐜𝐡 {branch_name} "
    "𝐢𝐬 𝐛𝐞𝐢𝐧𝐠 𝐮𝐬𝐞𝐝:\n"
    "𝐢𝐧 𝐭𝐡𝐢𝐬 𝐜𝐚𝐬𝐞, 𝐔𝐩𝐝𝐚𝐭𝐞𝐫 𝐢𝐬 𝐮𝐧𝐚𝐛𝐥𝐞 𝐭𝐨 𝐢𝐝𝐞𝐧𝐭𝐢𝐟𝐲 𝐭𝐡𝐞 𝐛𝐫𝐚𝐧𝐜𝐡 𝐭𝐨 𝐛𝐞 𝐮𝐩𝐝𝐚𝐭𝐞𝐝."
    "𝐩𝐥𝐞𝐚𝐬𝐞 𝐜𝐡𝐞𝐜𝐤 𝐨𝐮𝐭 𝐭𝐨 𝐚𝐧 𝐨𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐛𝐫𝐚𝐧𝐜𝐡, 𝐚𝐧𝐝 𝐫𝐞-𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐮𝐩𝐝𝐚𝐭𝐞𝐫."
)
OFFICIAL_UPSTREAM_REPO = "https://github.com/4rjun9/JARVIS"
BOT_IS_UP_TO_DATE = "𝐉𝐚𝐫𝐯𝐢𝐬 𝐒𝐲𝐬𝐭𝐞𝐦 𝐔𝐩𝐠𝐫𝐚𝐝𝐞𝐝"
NEW_BOT_UP_DATE_FOUND = (
    "𝐍𝐞𝐰 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 {branch_name}\n"
    "changelog: \n\n{changelog}\n"
    "𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠......"
)
NEW_UP_DATE_FOUND = (
    "𝐍𝐞𝐰 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 {branch_name}\n"
    "𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠......"
)
REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
DIFF_MARKER = "HEAD..{remote_name}/{branch_name}"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "re-starting heroku application"
# -- Constants End -- #


#@command(pattern="^.update", outgoing=True)
@borg.on(admin_cmd(pattern=r"update"))
async def updater(message):
    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(IFFUCI_ACTIVE_BRANCH_NAME, origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != IFFUCI_ACTIVE_BRANCH_NAME:
        await message.edit(IS_SELECTED_DIFFERENT_BRANCH.format(
            branch_name=active_branch_name
        ))
        return False

    try:
        repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
    except Exception as e:
        print(e)
        pass

    temp_upstream_remote = repo.remote(REPO_REMOTE_NAME)
    temp_upstream_remote.fetch(active_branch_name)

    changelog = generate_change_log(
        repo,
        DIFF_MARKER.format(
            remote_name=REPO_REMOTE_NAME,
            branch_name=active_branch_name
        )
    )

    if not changelog:
        await message.edit("▄︻̷̿┻̿═━一")
        await asyncio.sleep(1)
 
    message_one = NEW_BOT_UP_DATE_FOUND.format(
        branch_name=active_branch_name,
        changelog=changelog
    )
    message_two = NEW_UP_DATE_FOUND.format(
        branch_name=active_branch_name
    )

    if len(message_one) > 4095:
        with open("change.log", "w+", encoding="utf8") as out_file:
            out_file.write(str(message_one))
        await bot.send_message(
            message.chat_id,
            document="change.log",
            caption=message_two
        )
        os.remove("change.log")
    else:
        await message.edit(message_one)

    temp_upstream_remote.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

    if Var.HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(Var.HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if Var.HEROKU_APP_NAME is not None:
                heroku_app = None
                for i in heroku_applications:
                    if i.name == Var.HEROKU_APP_NAME:
                        heroku_app = i
                if heroku_app is None:
                    await message.edit("Invalid APP Name. Please set the name of your bot in heroku in the var HEROKU_APP_NAME.")
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://",
                    "https://api:" + Var.HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(deploy_start(bot, message, HEROKU_GIT_REF_SPEC, remote))

            else:
                await message.edit("Please create the var HEROKU_APP_NAME as the key and the name of your bot in heroku as your value.")
                return
        else:
            await message.edit(NO_HEROKU_APP_CFGD)
    else:
        await message.edit("No heroku api key found in HEROKU_API_KEY var")
        

def generate_change_log(git_repo, diff_marker):
    out_put_str = ""
    d_form = "%d/%m/%y"
    for repo_change in git_repo.iter_commits(diff_marker):
        out_put_str += f"•[{repo_change.committed_datetime.strftime(d_form)}]: {repo_change.summary} <{repo_change.author}>\n"
    return out_put_str

async def deploy_start(bot, message, refspec, remote):
    await message.edit(RESTARTING_APP)
    await message.edit("😎⌐╦╦═─😎 Deploy Successful🇮🇳 \n **To IndianBranch**")
    await remote.push(refspec=refspec)
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)

    
