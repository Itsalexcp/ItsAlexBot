import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands


class ChannelUpdateEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before: disnake.abc.GuildChannel, after: disnake.abc.GuildChannel):
        bot = self.bot
        if before.name != after.name:
            embed = defaults.style.event_embed
            embed.title = "Channelname geändert"
            embed.description = f"Der Channelname wurde von **{before.name}** zu **{after.name}** geändert"
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

        if before.topic != after.topic:
            embed = defaults.style.event_embed
            embed.title = "Channeltopic geändert"
            embed.description = f"Der Channeltopic wurde von **{before.topic}** zu **{after.topic}** geändert"
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

        if before.position != after.position:
            embed = defaults.style.event_embed
            embed.title = "Channelposition geändert"
            embed.description = f"Die Channelposition wurde von **{before.position}** zu **{after.position}** geändert"
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

        if before.category != after.category:
            embed = defaults.style.event_embed
            embed.title = "Channelkategorie geändert"
            embed.description = f"Die Channelkategorie wurde von **{before.category}** zu **{after.category}** geändert"
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

        if before.slowmode_delay != after.slowmode_delay:
            embed = defaults.style.event_embed
            embed.title = "Channelslowmode geändert"
            embed.description = f"Der Channelslowmode wurde von **{before.slowmode_delay}** zu **{after.slowmode_delay}** geändert"
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

        if before.nsfw != after.nsfw:
            embed = defaults.style.event_embed
            embed.title = "Channelnsfw geändert"
            embed.description = f"Der Channelnsfw wurde von **{before.nsfw}** zu **{after.nsfw}** geändert"
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: disnake.abc.GuildChannel):
        bot = self.bot
        embed = defaults.style.event_embed
        embed.title = "Channel erstellt"
        embed.add_field(name="Name", value=channel.name + channel.mention, inline=False)
        embed.add_field(name="ID", value=channel.id)
        embed.add_field(name="Position", value=channel.position)
        embed.add_field(name="Kategorie", value=channel.category)
        embed.add_field(name="Erstellt am", value=channel.created_at)
        embed.add_field(name="Zum Channel", value=channel.jump_url)
        await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: disnake.abc.GuildChannel):
        bot = self.bot
        embed = defaults.style.event_embed
        embed.title = "Channel gelöscht"
        embed.add_field(name="Name", value=channel.name, inline=False)
        embed.add_field(name="ID", value=channel.id)
        embed.add_field(name="Erstellt am", value=channel.created_at)
        await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(ChannelUpdateEvent(bot))
