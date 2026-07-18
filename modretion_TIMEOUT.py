import discord
from discord.ext import commands

import datetime
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Bot Online!")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


@bot.command()
async def timeout(ctx, member: discord.Member, message):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("❌ You don't have permission to use this command.")
        return

    if not ctx.guild.me.guild_permissions.moderate_members:
        await ctx.send("❌ I don't have permission to timeout members.\n:(")
        return

    ind = len(message) - 1
    unit = message[ind]
    n = message[:ind]

    if not n.isdigit():
        await ctx.send("❌ Invalid time format.")
        return

    val = int(n)
    current = datetime.now().astimezone()

    if unit == "s":
        next = current + timedelta(seconds=val)
    elif unit == "m":
        next = current + timedelta(minutes=val)
    elif unit == "h":
        next = current + timedelta(hours=val)
    elif unit == "d":
        next = current + timedelta(days=val)
    elif unit == "w":
        next = current + timedelta(weeks=val)
    else:
        await ctx.send("❌ Invalid time unit. Use s, m, h, d or w.")
        return

    await member.timeout(next)
    await ctx.send(f"{member.mention} has been timed out :(")
