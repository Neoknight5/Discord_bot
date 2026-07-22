class MyDropdown(ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Anime",
                description="View your anime collection",
                emoji="🎌",
                value="anime"
            ),
            discord.SelectOption(
                label="Sticker",
                description="View your stickers",
                emoji="⭐",
                value="sticker"
            ),
            discord.SelectOption(
                label="Wallpaper",
                description="View your wallpapers",
                emoji="🖼️",
                value="wallpaper"
            )
        ]
            #chat
        super().__init__(
            placeholder="Choose a category...",
            min_values=1, #chat
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        choice = self.values[0]

        if choice == "anime":
            await interaction.response.send_message("Anime selected!")

        elif choice == "sticker":
            await interaction.response.send_message("Sticker selected!")

        elif choice == "wallpaper":
            await interaction.response.send_message("Wallpaper selected!")

class MyView(ui.View):#chat
    def __init__(self):
        super().__init__()
        self.add_item(MyDropdown())

@bot.command()
async def menu(ctx):
    view = MyView()
    await ctx.send("Choose one:", view=view)




