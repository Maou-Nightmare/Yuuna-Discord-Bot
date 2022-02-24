
import datetime
from nextcord.colour import Color
from nextcord.embeds import Embed
from nextcord.ext import tasks
from nextcord.ext import commands

client = nextcord.Client()
client = commands.Bot(command_prefix = "INSERT PREFIX HERE")


#Simple Embed
@client.command()
async def embed(ctx):
  em= nextcord.Embed(
    title = "EMBED TITLE",
    color= nextcord.Color.red,      #You can either set nextcord.Color.random, nextcord.Color.red/blue/green or use a hexcode
    description= "EMBED DESCRIPTION"
  )
  em.set_footer(
    text= "EMBED FOOTER"
  )
  em.set_image(url= "INSERT IMAGE URL HERE") #EG https://media.discordapp.net/attachments/729686585825558538/911032888122810418/image_3.png?width=831&height=467
  await ctx.send(embed=em)
  
  
  #Advanced Embed/Embed With Thumbnail, Timestamp, Icon, Fields and Authior
  @client.command()
  async def advembed(ctx):
    em = nextcord.Embed(
       title = "EMBED TITLE",
       colour= nextcord.Color.red, 
       timestamp= ctx.message.created_at,
       description = "EMBED DESCRIPTION"
    )
    em.set_author(name= "EMBED AUTHOR"),
    em.set_thumbnail(url= "INSERT IMAGE URL HERE"), 
    em.set_footer(text= "EMBED FOOTER",
    icon_url= "INSERT IMAGE URL HERE")
 
    em.add_field(name= "FIELD NAME", value= "FIELD VALUE/DESCRIPTION", inline= False) # You Can Apply Either True or False. True = Inline with each other, False = Not Inlined.
    em.add_field(name= "FIELD NAME", value= "FIELD VALUE/DESCRIPTION", inline= False)
    em.add_field(name= "FIELD NAME", value= "FIELD VALUE/DESCRIPTION", inline= False)
    )
    await ctx.send(embed=em)
  
  
client.run("INSERT BOT TOKEN HERE")
