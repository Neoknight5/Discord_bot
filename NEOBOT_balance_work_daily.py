import discord
from discord.ext import commands
from datetime import datetime, timedelta
import random
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Neobot is ready")


@bot.command()
async def daily(ctx):
    name = str(ctx.author.id)

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if name not in data:
        data[name] = {
            "cash": 0,
            "last_daily": "",
            "lt_work": ""
        }

    now = datetime.now()
    coins = random.randint(1, 1000)

    if data[name]["last_daily"] == "":
        data[name]["last_daily"] = now.isoformat()
        data[name]["cash"] += coins

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        await ctx.send(f"🎉 You received **{coins}** coins! Come back after **12 hours** ^-^")
        return

    last_daily = datetime.fromisoformat(data[name]["last_daily"])

    if now - last_daily >= timedelta(hours=12):
        data[name]["last_daily"] = now.isoformat()
        data[name]["cash"] += coins

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        await ctx.send(f"🎉 You received **{coins}** coins! ^-^")
    else:
        remain = timedelta(hours=12) - (now - last_daily)
        await ctx.send(f"⏳ Wait **{remain}** before claiming again! ^-^")


@bot.command()
async def balance(ctx):
    name = str(ctx.author.id)

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if name not in data:
        data[name] = {
            "cash": 0,
            "lt_work": "",
            "last_daily": ""
        }

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    await ctx.send(f"💰 {ctx.author.display_name}, your balance is **{data[name]['cash']}** coins! ^-^")


@bot.command()
async def work(ctx):
    name = str(ctx.author.id)
    coins = random.randint(50, 1000)

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if name not in data:
        data[name] = {
            "cash": 0,
            "lt_work": "",
            "last_daily": ""
        }

    now = datetime.now()

    if data[name]["lt_work"] == "":
        data[name]["lt_work"] = now.isoformat()
        data[name]["cash"] += coins

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        await ctx.send(f"💼 Work complete! You earned **{coins}** coins! Come back after **1 minute** ^-^")
        return

    last_work = datetime.fromisoformat(data[name]["lt_work"])

    if now - last_work >= timedelta(minutes=1):
        data[name]["lt_work"] = now.isoformat()
        data[name]["cash"] += coins

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        await ctx.send(f"💼 Great job! You earned **{coins}** coins! ^-^")
    else:
        remain = timedelta(minutes=1) - (now - last_work)
        sec_left = int(remain.total_seconds())

        await ctx.send(f"⏳ You already worked! Please wait **{sec_left}** seconds. ^-^")


bot.run("^-^")
