import disnake
from disnake.ext import commands
import json
import defaults
from defaults import embed


class PingCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Get the bot's current websocket latency."""
        pingembed = embed.DefaultEmbed(
            title="Pong!",
            description=f"**{round(self.bot.latency * 1000)}ms**"
        )
        await inter.response.send_message(embed=pingembed)


def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))
