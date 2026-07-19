import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Bot Online!")


@bot.command()
async def embed(ctx):
    embed = discord.Embed(
        title="📌 Embed Title",
        description="This is the embed description.\nYou can write anything here.",
        color=discord.Color.blue(),
        url="https://github.com/",
        timestamp=datetime.now()
    )

    # Author
    embed.set_author(
        name=ctx.author.display_name,
        icon_url=ctx.author.display_avatar.url,
        url="https://github.com/"
    )

    # Thumbnail
    embed.set_thumbnail(
        url=ctx.guild.icon.url if ctx.guild.icon else ctx.author.display_avatar.url
    )

    # Image
    embed.set_image(
        url="https://picsum.photos/800/300"
    )

    # Fields
    embed.add_field(
        name="📊 Field 1",
        value="This is Field 1.",
        inline=True
    )

    embed.add_field(
        name="⭐ Field 2",
        value="This is Field 2.",
        inline=True
    )

    embed.add_field(
        name="💻 Field 3",
        value="This field is on a new line.",
        inline=False
    )

    embed.add_field(
        name="📁 Field 4",
        value="Another field.",
        inline=True
    )

    embed.add_field(
        name="❤️ Field 5",
        value="Supports **Markdown**.",
        inline=True
    )

    embed.add_field(
        name="🔗 Field 6",
        value="[Github](https://github.com)",
        inline=False
    )

    # Footer
    embed.set_footer(
        text="NeoBot • Embed Example",
        icon_url=ctx.bot.user.display_avatar.url
    )

    await ctx.send(embed=embed)


bot.run("YOUR_BOT_TOKEN")
