#_____________pay_________
@bot.command()
async def pay(ctx, member: discord.Member, num: int):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    name = str(ctx.author.id)
    send_name = str(member.id)

    if member == ctx.author:
        await ctx.send("❌ You can't pay yourself.")
        return

    if num <= 0:
        await ctx.send("❌ Enter a valid amount.")
        return

    if name not in data:
        data[name] = {
            "cash": 0,
            "lt_work": "",
            "last_daily": ""
        }
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        await ctx.send("You don't have an account yet ^-^ Run `!daily` first.")
        return

    if send_name not in data:
        data[send_name] = {
            "cash": 0,
            "lt_work": "",
            "last_daily": ""
        }
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        await ctx.send(f"{member.display_name} doesn't have an account yet.")
        return

    if data[name]["cash"] < num:
        await ctx.send(
            f"{ctx.author.display_name} is poor hihi ^^,\n"
            "Your balance is too low to pay another user."
        )
        return

    data[name]["cash"] -= num
    data[send_name]["cash"] += num

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    await ctx.send(
        f"**{ctx.author.display_name}** transferred **{num}** coins to **{member.display_name}** ^-^"
    )
