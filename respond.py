import nextcord


client = nextcord.Client()

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
