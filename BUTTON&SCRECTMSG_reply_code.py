@bot.command()
async def sys(ctx):
    view = discord.ui.View()
    button = discord.ui.Button(
        label="hello",
        emoji = "😊",
        style=discord.ButtonStyle.primary
    )
    async def hello_callback(interaction):
        await interaction.response.edit_message(
            content=f"{interaction.user.mention}Hello u clicked the button ^-^",view=None)
    button.callback = hello_callback
    await ctx.send("Click the button below:", view=view, ephemeral=True)
    view.add_item(button)
    
    await ctx.reply("Click the button below:", view=view)
@bot.command()
async def sec_sys(ctx):
    view = discord.ui.View()
    button = discord.ui.Button(
        label="hello",
        emoji = "😊",
        style=discord.ButtonStyle.primary
    )
    # await ctx.reply("Click the button below:", view=view, ephemeral=True)
    async def hello_callback(interaction):
        await interaction.response.send_message(
            content=f"{interaction.user.mention}Hello u clicked the button ^-^",ephemeral=True)
    button.callback = hello_callback
    
    view.add_item(button)
    
    await ctx.reply("Click the button below:", view=view)
