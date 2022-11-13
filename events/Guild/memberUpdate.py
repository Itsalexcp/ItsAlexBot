import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands


class MemberUpdateEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before: disnake.Member, after: disnake.Member):
        bot = self.bot
        if before.nick != after.nick:
            embed = defaults.style.event_embed
            embed.title = "Nickname geändert"
            embed.description = f"Der Nickname von **{before.mention}** wurde von **{before.nick}** zu **{after.nick}** geändert"
            await bot.get_channel(defaults.channels.member_tracker).send(embed=embed)

        if before.roles != after.roles:
            embed = defaults.style.event_embed
            embed.title = "Rollen geändert"
            embed.description = f"Die Rollen von **{before.mention}** wurden geändert"
            embed.add_field(name="Vorher", value=f"{before.roles}")
            embed.add_field(name="Nachher", value=f"{after.roles}")
            await bot.get_channel(defaults.channels.member_tracker).send(embed=embed)

        if before.premium_since != after.premium_since:
            embed = defaults.style.event_embed
            embed.title = "Boost geändert"
            embed.description = f"Der Boost von **{before.mention}** wurde von **{before.premium_since}** zu **{after.premium_since}** geändert"
            await bot.get_channel(defaults.channels.member_tracker).send(embed=embed)

        if before.voice != after.voice:
            embed = defaults.style.event_embed
            embed.title = "Voice geändert"
            embed.description = f"Der Voice von **{before.mention}** wurde von **{before.voice}** zu **{after.voice}** geändert"
            await bot.get_channel(defaults.channels.member_tracker).send(embed=embed)

        if before.avatar != after.avatar:
            embed = defaults.style.event_embed
            embed.title = "Avatar geändert"
            embed.description = f"Der Avatar von **{before.mention}** wurde geändert"
            embed.set_image(url=after.avatar.url)
            await bot.get_channel(defaults.channels.member_tracker).send(embed=embed)

        if before.banner != after.banner:
            embed = defaults.style.event_embed
            embed.title = "Banner geändert"
            embed.description = f"Das Banner von **{before.mention}** wurde geändert"
            embed.set_image(url=after.banner.url)
            await bot.get_channel(defaults.channels.member_tracker).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):
        embed = defaults.style.event_embed
        embed.title = "Member gejoint"
        embed.description = f"**{member.mention}** hat den Server gejoint"
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="ID", value=f"{member.id}")
        embed.add_field(name="Erstellt", value=f"{member.created_at}")
        embed.add_field(name="Beigetreten", value=f"{member.joined_at}")
        embed.add_field(name="Boost", value=f"{member.premium_since}")

        await self.bot.get_channel(defaults.channels.member_tracker).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: disnake.Member):
        embed = defaults.style.event_embed
        embed.title = "Member left"
        embed.description = f"**{member.mention}** hat den Server verlassen"
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="ID", value=f"{member.id}")
        embed.add_field(name="Erstellt", value=f"{member.created_at}")
        embed.add_field(name="Beigetreten", value=f"{member.joined_at}")
        embed.add_field(name="Boost", value=f"{member.premium_since}")

        await self.bot.get_channel(defaults.channels.member_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(MemberUpdateEvent(bot))

