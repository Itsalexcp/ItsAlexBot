import os
import datetime
import disnake
import defaults
import asyncio
import requests
import json
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands

started = False



async def status_task(bot: commands.Bot):
    while True:
        await bot.change_presence(activity=disnake.Game(f"Mit {len(bot.guilds)} Servern"),
                                  status=disnake.Status.online)
        await asyncio.sleep(30)
        await bot.change_presence(activity=disnake.Game(f"Mit {len(bot.users)} Benutzern"),
                                  status=disnake.Status.online)
        await asyncio.sleep(30)
        await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="itsalex.cp#0001 zu"),
                                  status=disnake.Status.online)
        await asyncio.sleep(30)
        await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name="Updates"),
                                  status=disnake.Status.online)
        await asyncio.sleep(30)


class ReadyEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        bot = self.bot
        api_key = os.environ.get("HEROKU_ITSALEX_API")
        app_name = "itsalexbot"
        endpoint = f"https://api.heroku.com/apps/{app_name}/releases"
        # Store the time when the bot was last started
        start_time = datetime.datetime.now()
        status_channel = bot.get_channel(1038885263641952336)
        global started
        if not started:
            current_time = datetime.datetime.now()
            uptime = current_time - start_time
            response = requests.get(endpoint, headers={
                "Accept": "application/vnd.heroku+json; version=3",
                "Authorization": f"Bearer {api_key}"
            })
            data = json.loads(response.text)
            latest_release = data[0]
            current_commit_hash = latest_release["commit"]
            previous_commit_hash = data[1]["commit"]
            is_new_build = current_commit_hash != previous_commit_hash
            build_number = os.environ.get("HEROKU_RELEASE_VERSION")
            if is_new_build:
                channel = status_channel
                await channel.send(f"Neuer Build deployed!\n Commit Hash: {current_commit_hash}\n Build Number: {build_number}\n Zeit: {current_time}")
            else:
                channel = status_channel
                await channel.send(f"Dyno Restart, Bot ist wieder online\n Build Number: {build_number}\n Uptime: {uptime}\n Zeit: {current_time}")
            print("Bot ist online.")
            print("Eingeloggt als Bot {}".format(bot.user.name))
            bot.loop.create_task(status_task(bot))
            print("\nBot ist erfolgreich online gegangen.\n\nLäuft aktuell auf folgenden Server:\n")
            for s in bot.guilds:
                print("  - %s (%s) \nOwner: %s (%s) \nMitglieder: %s Mitglieder \nErstellt am: %s" % (
                    s.name, s.id, s.owner, s.owner_id, s.member_count, s.created_at.strftime("%d.%m.%Y, %H:%M Uhr")))
            started = True
            embed = defaults.style.status_on_embed
            await status_channel.send(embed=embed)
        else:
            print('Bot ist offline.')
            embed = defaults.style.status_off_embed
            await bot.get_channel(defaults.channels.status).send(embed=embed)
        return

        # Presence


def setup(bot):
    bot.add_cog(ReadyEvent(bot))
