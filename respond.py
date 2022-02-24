


client = nextcord.Client()
client = commands.Bot(command_prefix = "INSERT BOT PREFIX HERE")

@client.event
async def on_ready():
  print(" {0.user} has logged in successfully".format(client))
  

#Ping Command
@client.command()
async def ping(ctx):
  await ctx.send("Pong!")
  
#Ping Command(With Mention)
@client.command()
 async def ping(ctx):
    user= ctx.author.mention
    await ctx.send(f"Pong! {user.mention}")

    
client.run("INSERT YOUR BOT TOKEN HERE")
