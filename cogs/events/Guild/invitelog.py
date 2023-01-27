import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands
from defaults.style import invite_embed


class DeleteButton(disnake.ui.Button):
    def __init__(self, invite: disnake.Invite):
        self.invite = invite
        super().__init__(label="Löschen",
                         style=disnake.ButtonStyle.danger,
                         emoji=emojis.AuditLinkDel)

    async def callback(self, interaction: disnake.Interaction):
        await interaction.response.defer()
        await self.invite.delete()


class InviteLogEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_invite_create(self, invite: disnake.Invite):
        bot = self.bot
        embed = invite_embed(title="Einladung erstellt",
                             code=invite.code,
                             created_at=invite.created_at,
                             inviter=invite.inviter,
                             max_age=invite.max_age,
                             max_uses=invite.max_uses,
                             temporary=invite.temporary,
                             uses=invite.uses, )
        self.view = disnake.ui.View()
        self.view.add_item(DeleteButton(invite))
        await bot.get_channel(defaults.channels.invite_tracker).send(embed=embed, view=self.view)

    @commands.Cog.listener()
    async def on_invite_delete(self, invite: disnake.Invite):
        bot = self.bot
        embed = invite_embed(title="Einladung gelöscht",
                             code=invite.code,
                             created_at=invite.created_at,
                             inviter=invite.inviter,
                             uses=invite.uses, )
        await bot.get_channel(defaults.channels.invite_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(InviteLogEvent(bot))