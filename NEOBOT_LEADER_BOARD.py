@bot.command()
async def lb(ctx):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if not data:
        await ctx.send("No members added yet! Use !daily or !work first.")
        return

    leaderboard_data = [
        (user_id, info["cash"])
        for user_id, info in data.items()
    ]

    leaderboard_data.sort(key=lambda x: x[1], reverse=True)

    top_ply = leaderboard_data[:10]

    des_line = []

    for index, (user_id, coins) in enumerate(top_ply, start=1):

        member_id = int(user_id)

        member = ctx.guild.get_member(member_id)

        if member:
            name = member.display_name

        else:
            try:
                member = await ctx.guild.fetch_member(member_id)
                name = member.display_name

            except discord.NotFound:
                name = f"Unknown User ({user_id})"

        des_line.append(
            f"**{index}.** {name} - **{coins}** coins"
        )

    final_des = "\n".join(des_line)

    embed = discord.Embed(
        title="🏆 Leaderboard",
        description=final_des,
        color=discord.Color.green()
    )

    embed.set_footer(text="NeoBot")

    await ctx.send(embed=embed)
