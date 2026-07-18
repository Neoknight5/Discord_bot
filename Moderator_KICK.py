import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot Online!")

@bot.command()
async def kick(ctx,member:discord.Member,*,message):
    if not ctx.guild.me.guild_permissions.kick_members:
        await ctx.send("❌ I don't have permission to kick members. \n :(")
    elif ctx.author.guild_permissions.administrator:
        await member.kick(reason=f"{message} \n:(")
        await ctx.send(f"✅ {member} has been kicked from the server.:( \n - reason: ```{message}```")  
    else:
        await ctx.send(f"your dont had permission to kick anyone !! \n - only administrator (admin) have it ^-^ ")
	
	

bot.run("^-^")
