import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands
import datetime


class UserStats(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def userstats(
            self,
            inter,
            member: disnake.Member = None,):
        if member is None:
            member = inter.author
        else:
            pass
        embed = disnake.Embed(
            title="User Stats für " + member.name,
            description="Detailierte Informationen über den Benutzer",
            color=disnake.Colour.yellow(),
            timestamp=datetime.datetime.now(),
            )

        embed.set_author(
            name=member.name + "#" + member.discriminator
        )
        embed.set_footer(
            text="Das ist ein Service von ItsAlex Enterprise",
            icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
                        "/AppIconGhostStation.png",
        )
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="Name", value=member.name, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Status", value=member.status, inline=True)
        embed.add_field(name="Höchste Rolle", value=member.top_role.mention, inline=True)
        embed.add_field(name="Bei Discord seit", value=member.created_at, inline=True)
        embed.add_field(name="Auf " + member.guild.name + " seit", value=member.joined_at, inline=True)
        if member.is_on_mobile():
            embed.add_field(name="Eingeloggt mit", value="Handy", inline=True)
        else:
            embed.add_field(name="Eingeloggt mit", value="Computer", inline=True)
        await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(UserStats(bot))
