import os
import disnake
import defaults
import asyncio
from defaults import style
from defaults import channels
from disnake.ext import commands

started = False
APP_ID = os.environ.get("HEROKU_APP_ID")
APP_NAME = os.environ.get("HEROKU_APP_NAME")
RELEASE_VERSION = os.environ.get("HEROKU_RELEASE_VERSION")
RELEASE_TIME = os.environ.get("HEROKU_RELEASE_CREATED_AT")
SLUG_DESCRIPTION = os.environ.get("HEROKU_SLUG_DESCRIPTION")
SLUG_COMMIT = os.environ.get("HEROKU_SLUG_COMMIT")
PREVIOUS_SLUG = os.environ.get("PREVIOUS_SLUG")
DISNAKE_VERSION = disnake.__version__
with open('runtime.txt', 'r') as f:
    python_version = f.read().strip()


def check_slug():
    if SLUG_COMMIT == PREVIOUS_SLUG:
        return True
    if SLUG_COMMIT != PREVIOUS_SLUG:
        os.environ.update({"PREVIOUS_SLUG": os.environ.get("HEROKU_SLUG_COMMIT")})
        return False


ReadyEmbedBUILD = disnake.Embed(
    title="Bot Status",
    description="Bot ist online gegangen.",
    color=style.primaryColor,
    timestamp=disnake.utils.utcnow()
)
if check_slug():
    ReadyEmbedBUILD.add_field(name="Action", value="Bot wurde neu gestartet.", inline=True)
if not check_slug():
    ReadyEmbedBUILD.add_field(name="Action", value="Bot wurde neu deployed.", inline=True)
ReadyEmbedBUILD.add_field(name="Bot Version", value=RELEASE_VERSION, inline=True)
ReadyEmbedBUILD.add_field(name="Bot Build", value=SLUG_DESCRIPTION, inline=True)
ReadyEmbedBUILD.add_field(name="Bot Commit", value=SLUG_COMMIT, inline=True)
ReadyEmbedBUILD.add_field(name="Python Version", value=python_version, inline=True)
ReadyEmbedBUILD.add_field(name="Disnake Version", value=DISNAKE_VERSION, inline=True)
ReadyEmbedBUILD.add_field(name="Heroku App ID", value=APP_ID, inline=True)
ReadyEmbedBUILD.add_field(name="Heroku App Name", value=APP_NAME, inline=True)
ReadyEmbedBUILD.add_field(name="Heroku Release Time", value=RELEASE_TIME, inline=True)
ReadyEmbedBUILD.set_footer(text="Bot Status", icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864/AppIconGhostStation.png")


class ReadyEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        bot = self.bot
        status_channel = bot.get_channel(1038885263641952336)
        global started
        if not started:
            print("Eingeloggt als Bot {}".format(bot.user.name))
            bot.loop.create_task(status_task(bot))
            print("\nBot ist erfolgreich online gegangen.\n\nLäuft aktuell auf folgenden Server:\n")
            for s in bot.guilds:
                print("  - %s (%s) \nOwner: %s (%s) \nMitglieder: %s Mitglieder \nErstellt am: %s" % (
                    s.name, s.id, s.owner, s.owner_id, s.member_count, s.created_at.strftime("%d.%m.%Y, %H:%M Uhr")))
            started = True
            await status_channel.send(embed=ReadyEmbedBUILD)
        else:
            print('Bot ist offline.')
            embed = defaults.style.status_off_embed
            await bot.get_channel(defaults.channels.status).send(embed=embed)
        return


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


def setup(bot):
    bot.add_cog(ReadyEvent(bot))
