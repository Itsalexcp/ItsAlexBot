import disnake
from disnake.ext import commands
import datetime


class StatsCommand(commands.Cog):
    """This will be for a stats command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def stats(
            self,
            inter: disnake.ApplicationCommandInteraction,
            user: disnake.Member):
        if user is None:
            user = inter.author
        else:
            pass
        embed = disnake.Embed(
            title="Stats",
            description="Detailierte Informationen über den Benutzer",
            color=disnake.Colour.yellow(),
            timestamp=datetime.datetime.now(),
        )

        embed.set_author(
            name=user.name + "#" + user.discriminator
        )
        embed.set_footer(
            text="Das ist ein Service von ItsAlex Enterprise",
            icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
                     "/AppIconGhostStation.png",
        )

        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
                     "/AppIconGhostStation.png")
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Bot", value=user.bot, inline=True)
        embed.add_field(name="Aktivität", value=user.activity, inline=True)
        embed.add_field(name="Avatar", value=user.avatar, inline=True)

        await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(StatsCommand(bot))
