import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands
from defaults.style import guild_embed


class GuildUpdateEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_update(self, before: disnake.Guild, after: disnake.Guild):
        bot = self.bot
        if before.name != after.name:
            embed = guild_embed(title="Name geändert",
                                id = before.id,)
            embed.add_field(name="Art der Änderung", value=f"Name von {before.name} zu {after.name} verändert ")
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.icon != after.icon:
            embed = guild_embed(title="Icon geändert",
                                id = before.id,)
            embed.set_thumbnail(url=after.icon)
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.owner != after.owner:
            embed = guild_embed(title="Owner geändert",
                                id = before.id,)
            embed.add_field(name="Art der Änderung", value=f"Owner von {before.owner} zu {after.owner} verändert ")
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.afk_channel != after.afk_channel:
            embed = guild_embed(title="AFK Channel geändert",
                                id = before.id,)
            embed.add_field(name="Art der Änderung", value=f"AFK Channel von {before.afk_channel} zu {after.afk_channel} verändert ")
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.afk_timeout != after.afk_timeout:
            x = before.afk_timeout
            x1 = x / 60
            y = after.afk_timeout
            y1 = y / 60
            embed = guild_embed(title="AFK Timeout geändert",
                                id = before.id,)
            embed.add_field(name="Art der Änderung", value=f"AFK Timeout von {x1} Minuten zu {y1} Minuten verändert ")
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.description != after.description:
            embed = guild_embed(title="Beschreibung geändert",
                                id = before.id,)
            embed.add_field(name="Art der Änderung", value=f"Beschreibung von {before.description} zu {after.description} verändert ")
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.explicit_content_filter != after.explicit_content_filter:
            embed = guild_embed(title="Explicit Content Filter geändert",
                                id = before.id,)
            embed.add_field(name="Art der Änderung", value=f"Explicit Content Filter von {before.explicit_content_filter} zu {after.explicit_content_filter} verändert ")
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.mfa_level != after.mfa_level:
            embed = guild_embed(title="MFA Level geändert",
                                id = before.id,)
            embed.add_field(name="Art der Änderung", value=f"MFA Level von {before.mfa_level} zu {after.mfa_level} verändert ")
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.verification_level != after.verification_level:
            embed = guild_embed(title="Verification Level geändert",
                                id = before.id,)
            embed.add_field(name="Art der Änderung", value=f"Verification Level von {before.verification_level} zu {after.verification_level} verändert ")
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.vanity_url_code != after.vanity_url_code:
            embed = guild_embed(title="Vanity URL Code geändert",
                                id = before.id,)
            embed.add_field(name="Art der Änderung", value=f"Vanity URL Code von {before.vanity_url_code} zu {after.vanity_url_code} verändert ")
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(GuildUpdateEvent(bot))
