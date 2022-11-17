import disnake
from disnake.ext import commands
import datetime


class ServerStatsCommand(commands.Cog):
    """This will be for a stats command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def serverstats(
            self,
            inter,
            server: disnake.Guild = None):
        if server is None:
            server = inter.guild
        else:
            pass

        embed = disnake.Embed(
            title="Server Stats für " + server.name,
            description="Detailierte Informationen über den Server",
            color=disnake.Colour.yellow(),
            timestamp=datetime.datetime.now(),
        )

        embed.set_author(
            name=inter.guild
        )
        embed.set_footer(
            text="Das ist ein Service von ItsAlex Enterprise",
            icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
                     "/AppIconGhostStation.png",
        )
        embed.set_thumbnail(url=server.icon)

        embed.add_field(name="Name", value=server.name, inline=False)
        embed.add_field(name="ID", value=server.id, inline=False)
        embed.add_field(name="Owner", value=server.owner, inline=False)
        embed.add_field(name="Beschreibung", value=server.description, inline=False)
        embed.add_field(name="Server Boost Level", value=server.premium_tier, inline=False)
        embed.add_field(name="Server Boosts", value=server.premium_subscription_count, inline=False)
        embed.add_field(name="Server Features", value=server.features, inline=False)
        embed.add_field(name="Member Count", value=server.member_count, inline=False)
        x = server.afk_timeout
        y = x / 60
        if x <= 3600:
            z = y / 60
            embed.add_field(name="AFK Timeout", value=f"{int(z)} Stunde", inline=False)
        else:
            embed.add_field(name="AFK timeout", value=f"{int(y)} Minuten", inline=False)
        embed.add_field(name="AFK channel", value=server.afk_channel, inline=False)

        await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(ServerStatsCommand(bot))
