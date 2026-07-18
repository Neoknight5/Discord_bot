import discord
from discord.ext import commands
from datetime import datetime, timedelta
import random
import json

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Neobot is ready")


@bot.command()
async def kick(ctx,member:discord.Member,*,message):
    if not ctx.guild.me.guild_permissions.kick_members:
        await ctx.send("❌ I don't have permission to kick members. \n :(")
    elif ctx.author.guild_permissions.administrator:
        await member.kick(reason=f"{message} \n:(")
        await ctx.send(f"✅ {member} has been kicked from the server.:( \n - reason: ```{message}")  
    else:
        await ctx.send(f"your dont had permission to kick anyone !! \n - only administrator (admin) have it ^-^ ")
	
@bot.command()
async def warn(ctx,member:discord.Member,*,message):
    name = str(member.id)
    if name == str(bot.user.id):
        await ctx.send("❌ I can't warn myself. \n :(")
        return
    try:
        with open("data.json","r")as file :
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}
    if not ctx.guild.me.guild_permissions.kick_members:
        await ctx.send("❌ I don't have permission to warn members. \n :(")
    elif ctx.author.guild_permissions.administrator:
        if name not in data:
            data[name] = {"cash": 0,"lt_wokr":"","last_daily":"","warn" : 0}
        if "warn" not in data[name]:
            data[name]["warn"] = 0
        data[name]["warn"] += 1
        with open("data.json","w") as file :
            json.dump(data,file,indent=4)
        await ctx.send(f"😢 {member.mention} has been warned from the server.:( \n - reason: ```{message}```")
    if data[name]["warn"] == 3:
        await ctx.send(f"⚠️ {member.mention} has been warned 3 times and will be timed out for 5 minutes. \n - reason: ```didnt stop after the warn```")
        data[name]["warn"] = 0
        current = datetime.now().astimezone()
        next = current + timedelta(minutes=5)
        await member.timeout(next,reason="warned 3 times \n ***- reason:-*** ```didnt stop after the warns```")
        with open("data.json","w") as file :
            json.dump(data,file,indent=4)
