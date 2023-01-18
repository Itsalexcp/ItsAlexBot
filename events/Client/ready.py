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
            embed = defaults.style.status_on_embed
            status_channel = bot.get_channel(1038885263641952336)
            await status_channel.send(embed=embed)
        else:
            print('Bot ist offline.')
            embed = defaults.style.status_off_embed
            await bot.get_channel(defaults.channels.status).send(embed=embed)
        return

        # Presence


def setup(bot):
    bot.add_cog(ReadyEvent(bot))
