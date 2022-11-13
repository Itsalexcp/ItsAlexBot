import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands


class GuildUpdateEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_update(self, before: disnake.Guild, after: disnake.Guild):
        bot = self.bot
        if before.name != after.name:
            embed = defaults.style.event_embed
            embed.title = "Servername geändert"
            embed.description = f"Der Servername wurde von **{before.name}** zu **{after.name}** geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.premium_tier != after.premium_tier:
            embed = defaults.style.event_embed
            embed.title = "Serverboost geändert"
            embed.description = f"Der Serverboost wurde von **{before.premium_tier}** zu **{after.premium_tier}** geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.verification_level != after.verification_level:
            embed = defaults.style.event_embed
            embed.title = "Serververifizierung geändert"
            embed.description = f"Die Serververifizierung wurde von **{before.verification_level}** zu **{after.verification_level}** geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.owner_id != after.owner_id:
            embed = defaults.style.event_embed
            embed.title = "Serverbesitzer geändert"
            embed.description = f"Der Serverbesitzer wurde von **<@{before.owner_id}>** zu **<@{after.owner_id}>** geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.vanity_url_code != after.vanity_url_code:
            embed = defaults.style.event_embed
            embed.title = "Server Vanity geändert"
            embed.description = f"Der Server Vanity wurde von {before.vanity_url_code} zu {after.vanity_url_code} geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.description != after.description:
            embed = defaults.style.event_embed
            embed.title = "Serverbeschreibung geändert"
            embed.description = f"Die Serverbeschreibung wurde von **{before.description}** zu **{after.description}** geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.banner != after.banner:
            embed = defaults.style.event_embed
            embed.title = "Serverbanner geändert"
            embed.description = f"Der Serverbanner wurde von {before.banner} zu {after.banner} geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.splash != after.splash:
            embed = defaults.style.event_embed
            embed.title = "Serversplash geändert"
            embed.description = f"Der Serversplash wurde von {before.splash} zu {after.splash} geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.discovery_splash != after.discovery_splash:
            embed = defaults.style.event_embed
            embed.title = "Serverdiscovery Splash geändert"
            embed.description = f"Der Serverdiscovery Splash wurde von {before.discovery_splash} zu {after.discovery_splash} geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.system_channel != after.system_channel:
            embed = defaults.style.event_embed
            embed.title = "Serversystem Channel geändert"
            embed.description = f"Der Serversystem Channel wurde von <#{before.system_channel}> zu <#{after.system_channel}> geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.rules_channel != after.rules_channel:
            embed = defaults.style.event_embed
            embed.title = "Serverrules Channel geändert"
            embed.description = f"Der Serverrules Channel wurde von <#{before.rules_channel}> zu <#{after.rules_channel}> geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.public_updates_channel != after.public_updates_channel:
            embed = defaults.style.event_embed
            embed.title = "Serverpublic_updates_channel geändert"
            embed.description = f"Der Serverpublic_updates_channel wurde von <#{before.public_updates_channel}> zu <#{after.public_updates_channel}> geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.preferred_locale != after.preferred_locale:
            embed = defaults.style.event_embed
            embed.title = "Serverpreferred_locale geändert"
            embed.description = f"Der Serverpreferred_locale wurde von **{before.preferred_locale}** zu **{after.preferred_locale}** geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.afk_channel != after.afk_channel:
            embed = defaults.style.event_embed
            embed.title = "Serverafk Channel geändert"
            embed.description = f"Der Serverafk Channel wurde von {before.afk_channel} zu {after.afk_channel} geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.afk_timeout != after.afk_timeout:
            x = before.afk_timeout
            x1 = x / 60
            y = after.afk_timeout
            y1 = y / 60
            embed = defaults.style.event_embed
            embed.title = "Serverafk Timeout geändert"
            embed.description = f"Der Serverafk Timeout wurde von **{x1} Minuten** zu **{y1} Minuten** geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.default_notifications != after.default_notifications:
            embed = defaults.style.event_embed
            embed.title = "Serverdefault notifications geändert"
            embed.description = f"Die Serverdefault Benachrichtigungen wurde von **{before.default_notifications}** zu **{after.default_notifications}** geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.explicit_content_filter != after.explicit_content_filter:
            embed = defaults.style.event_embed
            embed.title = "Serverexplicit_content_filter geändert"
            embed.description = f"Der Serverexplicit content filter wurde von **{before.explicit_content_filter}** zu **{after.explicit_content_filter}** geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)

        if before.mfa_level != after.mfa_level:
            embed = defaults.style.event_embed
            embed.title = "Servermfa level geändert"
            embed.description = f"Der Servermfa level wurde von **{before.mfa_level}** zu **{after.mfa_level}** geändert"
            await bot.get_channel(defaults.channels.guild_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(GuildUpdateEvent(bot))
