import disnake
from disnake.ext import commands
import datetime
from defaults import emojis
import pytz


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
        embed.set_footer(text="Powered by itsalex.cp#0001", icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1043262304726286376/DE_SnowsgivingClydeLight.png")

        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name=f"{emojis.IconMembers} Name", value=member.name, inline=True)
        embed.add_field(name=f"{emojis.IconId} ID", value=member.id, inline=True)
        embed.add_field(name=f"{emojis.ChannelText} Discriminator", value=member.discriminator, inline=True)
        if member.status == disnake.Status.online:
            embed.add_field(
                name="Status",
                value=f"{emojis.StatusOnline} Online",
                inline=False
            )
            if member.is_on_mobile():
                embed.add_field(
                    name="Eingeloggt mit",
                    value=f"{emojis.StatusPhoneOnline} Handy",
                    inline=False
                )
            else:
                embed.add_field(
                    name="Eingeloggt mit",
                    value=f"{emojis.StatusOnline} Desktop",
                    inline=False
                )
        elif member.status == disnake.Status.idle:
            embed.add_field(
                name="Status",
                value=f"{emojis.StatusIdle} Abwesend",
                inline=False
            )
            if member.is_on_mobile():
                embed.add_field(
                    name="Eingeloggt mit",
                    value=f"{emojis.StatusPhoneIdle} Handy",
                    inline=False
                )
            else:
                embed.add_field(
                    name="Eingeloggt mit",
                    value=f"{emojis.StatusIdle} Desktop",
                    inline=False
                )
        elif member.status == disnake.Status.dnd:
            embed.add_field(
                name="Status",
                value=f"{emojis.StatusDND} Bitte nicht stören",
                inline=False
            )
            if member.is_on_mobile():
                embed.add_field(
                    name="Eingeloggt mit",
                    value=f"{emojis.StatusPhoneDND} Handy",
                    inline=False
                )
            else:
                embed.add_field(
                    name="Eingeloggt mit",
                    value=f"{emojis.StatusDND} Desktop",
                    inline=False
                )
        elif member.status == disnake.Status.offline:
            embed.add_field(
                name="Status",
                value=f"{emojis.StatusOffline} Offline",
                inline=False
            )
            if member.is_on_mobile():
                embed.add_field(
                    name="Eingeloggt mit",
                    value=f"{emojis.StatusPhoneOffline} Handy",
                    inline=False
                )
            else:
                embed.add_field(
                    name="Eingeloggt mit",
                    value=f"{emojis.StatusOffline} Desktop",
                    inline=False
                )

        embed.add_field(name=f"{emojis.IconMembers} Server beigetreten", value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=True)
        embed.add_field(name=f"{emojis.NitroTag} Höchste Rolle", value=member.top_role.mention, inline=True)
        embed.add_field(name=f"{emojis.IconClock} Bei Discord seit", value=member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=True)
        embed.add_field(name=f"{emojis.IconServerInsights} Auf " + member.guild.name + " seit", value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=True)

        await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(UserStats(bot))
