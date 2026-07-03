#_____________pay_________
@bot.command()
async def pay(ctx,member : discord.Member,num:int):
	try :
		with ope("data.json","r") as file :
			data = json.load(file)
	except (FileNotFoundError,json.JSONDecodeError):
			data = {}
		name = str(ctx.author.id)
		send_name = str(member.id)
		if name not in data :
			data[name] = {"cash" : 0 ,"lt_work" :"","last_daily":""}
			return
			with open("data.json","w") as file :
				json.dump(data,file,indent=4)
			await ctx.send(f"you dont have an account yet ^-^ . run !daily and balance first _")
		elif send_name not in data :
			data[send_name] = {"lt_work":"","last_daily" :	"" , "cash" :""}
			with  open("data.json","w") as file :
				json.dump(data,file,indent=4)
			return 
		elif data[name]["cash"] < num :
			await ctx.send(f"{ctx.author.display_name} is poor hiihi^^ , \n your balance is too low to pay any other user ^-^")
		return
		else :
			data[name]["cash"] -= num
			data[send_name]["cash"] += num
			with open("data.json","w") as file :
				json.dump(data,file,indent=4)
		await ctx.send(f" '{ctx.author.disdplay_name}' transfered ***{num}*** coins to {member.display_name}^-^")
