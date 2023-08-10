import disnake
from disnake.ext import commands
import datetime


class GiveawayCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def parse_duration(self, duration_str: str) -> datetime.timedelta:
        time_mapping = {
            'd': 'days',
            'h': 'hours',
            'm': 'minutes'
        }

        duration = {}
        for unit, name in time_mapping.items():
            value = 0
            if unit in duration_str:
                try:
                    value = int(duration_str.split(unit)[0].split()[-1])
                except ValueError:
                    pass
            duration[name] = value

        return datetime.timedelta(**duration)

    @commands.slash_command(
        name="giveaway",
        description="Start a giveaway",
        options=[
            disnake.Option(
                name="channel",
                description="Channel to post the giveaway in",
                type=disnake.OptionType.CHANNEL,
                required=True
            ),
            disnake.Option(
                name="title",
                description="Title of the giveaway",
                type=disnake.OptionType.STRING,
                required=True
            ),
            # Add other options similarly
        ]
    )
    @commands.has_permissions(administrator=True)
    async def giveaway(self, ctx, channel: disnake.TextChannel, title: str, description: str, prize: str, duration: str,
                       winners: int, application: bool):
        end_time = datetime.datetime.utcnow() + self.parse_duration(duration)
        remaining_time = str(end_time - datetime.datetime.utcnow())

        embed = disnake.Embed(title=title, description=description, color=disnake.Color.green())
        embed.add_field(name="Prize", value=prize, inline=False)
        embed.add_field(name="End Date", value=end_time.strftime('%Y-%m-%d %H:%M:%S UTC'), inline=True)
        embed.add_field(name="Remaining Time", value=remaining_time, inline=True)
        embed.add_field(name="Winners", value=str(winners), inline=True)

        message = await channel.send(embed=embed)
        await message.add_reaction('🎉')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, application: bool, payload: disnake.RawReactionActionEvent):
        if payload.emoji.name == '🎉':
            channel = self.bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            if message.author != self.bot.user:
                return

            user = payload.member
            if application:
                components = [
                    disnake.MessageActionRow(
                        disnake.MessageInput(
                            custom_id="giveaway_application",
                            placeholder="Enter your application here...",
                            min_length=1,
                            max_length=500
                        )
                    )
                ]
                await user.send("Please fill out the application:", components=components)
            else:
                # Directly enter the user into the giveaway
                pass

    @commands.Cog.listener()
    async def on_interaction(self, interaction: disnake.Interaction):
        if interaction.type == disnake.InteractionType.message_component and interaction.custom_id == "giveaway_application":
            application_text = interaction.data['values'][0]

            designated_channel_id = 1234567890  # Replace with your channel ID
            designated_channel = self.bot.get_channel(designated_channel_id)
            await designated_channel.send(f"Application from {interaction.user.name}: {application_text}")

            await interaction.response.send_message("Your application has been submitted!", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(GiveawayCommand(bot))