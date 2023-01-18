import disnake
import defaults
import asyncio
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
        global started
        if not started:
            print("Bot ist online.")
            print("Eingeloggt als Bot {}".format(bot.user.name))
            bot.loop.create_task(status_task(bot))
            print("\nBot ist erfolgreich online gegangen.\n\nLäuft aktuell auf folgenden Server:\n")
            for s in bot.guilds:
                print("  - %s (%s) \nOwner: %s (%s) \nMitglieder: %s Mitglieder \nErstellt am: %s" % (
                    s.name, s.id, s.owner, s.owner_id, s.member_count, s.created_at.strftime("%d.%m.%Y, %H:%M Uhr")))
            started = True
            import os
            import sys

            if os.environ.get('DYNO') == "worker":
                # get the timestamp of the restart
                release_timestamp = os.environ.get('HEROKU_RELEASE_CREATED_AT')
                # get the version of the app deployed
                commit_hash = os.environ.get('HEROKU_SLUG_COMMIT')
                # send "Restarted by Heroku" message with timestamp and version
                message = f"Restarted by Heroku at {release_timestamp}. Python version: {sys.version}, Discord.py version: {disnake.__version__}, CommitHash: {commit_hash}"
                print(message)
                await bot.get_channel(1038885263641952336).send(message)
            else:
                # send "I am online" message
                print("I am online")

        else:
            print('Bot ist offline.')
            embed = defaults.style.status_off_embed
            await bot.get_channel(defaults.channels.status).send(embed=embed)
        return

        # Presence


def setup(bot):
    bot.add_cog(ReadyEvent(bot))
