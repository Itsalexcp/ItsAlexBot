import disnake


class DefaultEmbed(disnake.Embed):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = disnake.Colour.blurple()
        self.timestamp = disnake.utils.utcnow()

    def set_author(self, **kwargs):
        super().set_author(**kwargs)
        self.set_footer(text="This is a service by ItsAlex Enterprise",
                        icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
                                 "/AppIconGhostStation.png")

    def set_footer(self, **kwargs):
        super().set_footer(**kwargs)
        self.set_footer(text="This is a service by ItsAlex Enterprise",
                        icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
                                 "/AppIconGhostStation.png")

    def set_thumbnail(self, **kwargs):
        super().set_thumbnail(**kwargs)
        self.set_thumbnail(url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
                               "/AppIconGhostStation.png")


