import disnake
import defaults
from defaults import style
from defaults import channels
from disnake.ext import commands


class MessageDeleteEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: disnake.Message):
        bot = self.bot
        if message.author.bot:
            return
        embed = style.message_embed(title="Nachricht gelöscht",
                                    author=message.author,
                                    content=message.content,
                                    created_at=message.created_at,
                                    channel=message.channel,
                                    attachments=message.attachments,
                                    id=message.id)
        await bot.get_channel(defaults.channels.message_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(MessageDeleteEvent(bot))
