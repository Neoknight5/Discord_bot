import discord
from dicord.ext import commands
import datetime
from datetime import datetime,timedelta
import random
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!",intents = intents)

@bot.event
async def on_ready():
	print("Neobot is ready")

#___________deleting process_________

#_______daily____________
@bot.command()
async def daily(ctx):
	name = str(ctx.author.id)
	data = {}
	#load
	try :
	with open("data.json","r") as file :
		data = json.laod(file)
	except FileNotFoundError :
		data = {}
	if name not in data :
		data[name] = {
		"cash" : 0 , "last_daily" : "","lt_work";""
		}
	now = datetime.now()
	coins =  random.randint(1,1000)
	if data[name]["last_daily"] == "" :
		data[name]["last_daily"] = now.isoformat()
		data[name]["lt_work"] = ""
		with open("data.json","w") as file :
			json.dump(data,file,indent=4)
		await ctx.send("you received **{coins}** come after 10 seconds ^-^")
	else :
		last_daily = datetime.fromisoformat(data[name]["last_daily"])
	if now-last_dailt > timedelta(hours=12):
		data[name]["last_daily"] = now.isoformat()
		data[name]["cash",] += coins
		with open("data.json","w") as file :
			json.dump(data,file,indent=4)
		await ctx.send(f"you received **{coins}** time for claiming again^-^")
	else:
		remain = timedelta(hours=12) - (now-last_daily)
		await ctx.send(f"wait **{remain}** time for claiming again ^-^")

#__________balance_________
@bot.command()
async def balance(ctx):
	name = str(ctx.author.id)
	try :
		with open("data.json","r") as file :
			data = json.load(file)
	except FileNotFoundError :
		data = {}
		with open("data.json","w") as file :
			json.dump(data,file)
		if name not in data :
			data[name] = {"cash" : 0 ,"lt_work" : "" ,"last_daily" :	"" }
		await ctx.send(f"{ctx.author.display_name} total balance {data[name]["cash"]} ^-^")
	
#_______work_________

@bot.command()
async def work(ctx):
	name = str(ctx.author.id)
	coinsn = random.randint(50,5000)
	
	try :
		with open("data.json") as file :
			data = json.laod(file)
	except FileNotFoundError :
		data = {}
	
	if name not in data :
		data[name] = {"cash" : 0 ,"lt_work" :	"" ,"last_daily" : "" }
		
	now = datetime.now()
	
	if data[name]["lt_work"] == "" :
		data[name]["lt_work"] = now.isoformat()
		data[name]["cash"] += coins
		
		with open("data.json","w") as file :
			json.dump(data,file,indent=4)
		await ctx.send(f"as your workdone , this is your reward ***{coins}*** coins! Come back after 1 minute !	^-^")
	else :
		remain = time.delta(minutes=1) - (now.lt_work)
		sec_left = int(remain.total_seconds())
		await ctx.send(f"you already claimed your reward ! please wait another {sec_left} seconds ^-^")


bot.run("keep it secret")	
