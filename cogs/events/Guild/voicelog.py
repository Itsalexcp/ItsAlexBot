import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands
from defaults.style import voicestate_embed, joined_ats, left_ats


class DisconnectButton(disnake.ui.Button):
    def __init__(self, user: disnake.Member):
        self.user = user
        super().__init__(label="Trennen",
                         style=disnake.ButtonStyle.danger,
                         emoji=emojis.IconDisconnect)

    async def callback(self, interaction: disnake.Interaction):
        await interaction.response.defer()
        await self.user.move_to(None)
        await interaction.message.edit(embed=voicestate_embed(self.user, "Disconnected"), view=None)


class VoiceStateEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_voice_state_update(self, member: disnake.Member, before: disnake.VoiceState, after: disnake.VoiceState):
        bot = self.bot
        if before.channel is None and after.channel is not None:
            embed = voicestate_embed(title="Voicechannel betreten",
                                     member=member,
                                     channel=after.channel.mention,
                                     joined_at=joined_ats,)

            self.view = disnake.ui.View()
            self.view.add_item(DisconnectButton(member))
            await bot.get_channel(defaults.channels.voice_tracker).send(embed=embed, view=self.view)

        elif before.channel is not None and after.channel is None:
            embed = voicestate_embed(title="Voicechannel verlassen",
                                     member=member,
                                     channel=before.channel.mention,
                                     left_at=left_ats,
                                     )
            await bot.get_channel(defaults.channels.voice_tracker).send(embed=embed)

        if before.channel != after.channel:
            embed = voicestate_embed(title="Voicechannel gewechselt",
                                     member=member,
                                     channel=before.channel.mention,
                                     left_at=left_ats,
                                     )
            embed.add_field(name="Gewechselt zu:", value=after.channel.mention)
            self.view = disnake.ui.View()
            self.view.add_item(DisconnectButton(member))
            await bot.get_channel(defaults.channels.voice_tracker).send(embed=embed, view=self.view)


def setup(bot):
    bot.add_cog(VoiceStateEvent(bot))

