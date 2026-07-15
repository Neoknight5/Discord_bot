import discord
from discord.ext import commands

import datetime
from datetime import datetime,timedelta

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
async def timeout(ctx,member:discord.Member,message):
	if ctx.author.guild_permissions.administrator:
		ind = len(message) - 1
		if message[ind] == "s":
			n = message[0:ind]
			val = int(n)
			current =  datetime.now().astimezone()
			next = current + timedelta(seconds=val)
			await member.timeout(next)
			await ctx.send(f"{member.mention} had timeout :(")
	elif not ctx.guild.me.guild_permissions.kick_members:
	   await ctx.send("❌ I don't have permission to kick members. \n :(")	
	if ctx.author.guild_permissions.administrator:
		if message[ind] == "m":
			n = message[0:ind]
			val = int(n)
			current =  datetime.now().astimezone()
			next = current + timedelta(minutes=val)
			await member.timeout(next)
			await ctx.send(f"{member.mention} had timeout :(")
	elif not ctx.guild.me.guild_permissions.kick_members:
	   await ctx.send("❌ I don't have permission to kick members. \n :(")	
	if ctx.author.guild_permissions.administrator:
		if message[ind] == "h":
			n = message[0:ind]
			val = int(n)
			current =  datetime.now().astimezone()
			next = current + timedelta(hours=val)
			await member.timeout(next)
			await ctx.send(f"{member.mention} had timeout :(")
	elif not ctx.guild.me.guild_permissions.kick_members:
	   await ctx.send("❌ I don't have permission to kick members. \n :(")
	if ctx.author.guild_permissions.administrator:
		if message[ind] == "d":
			n = message[0:ind]
			val = int(n)
			current =  datetime.now().astimezone()
			next = current + timedelta(days=val)
			await member.timeout(next)
			await ctx.send(f"{member.mention} had timeout :(")
	elif not ctx.guild.me.guild_permissions.kick_members:
	   await ctx.send("❌ I don't have permission to kick members. \n :(")	
	if ctx.author.guild_permissions.administrator:
		if message[ind] == "w":
			n = message[0:ind]
			val = int(n)
			current =  datetime.now().astimezone()
			next = current + timedelta(weeks=val)
			await member.timeout(next)
			await ctx.send(f"{member.mention} had timeout :(")
	elif not ctx.guild.me.guild_permissions.kick_members:
	   await ctx.send("❌ I don't have permission to kick members. \n :(")
