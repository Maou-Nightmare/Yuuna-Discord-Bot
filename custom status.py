import json
import aiofiles
from nextcord import channel, guild, user, webhook
from nextcord import message
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
import nextcord
from nextcord.ext import tasks
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions, MissingPermissions
from random import choice
import os, platform


client = nextcord.Client()
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = "yu!", help_command=None, case_insensitive=True, intents=intents)


@client.event
async def on_ready():  
  await client.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="weebcity.club | Yuuna stable version 1.0"))
  print(" {0.user} has logged in successfully".format(client))
  
  async def ch_pr():
  await client.wait_until_ready()

  statuses = ["All of my beautiful Users >:3 | Yuuna stable version 1.0 ", "weebcity.club | Yuuna stable version 1.0", "yu!commands | Yuuna stable version 1.0"]

  while not client.is_closed():

    status = random.choice(statuses)

    await client.change_presence(activity= nextcord.Activity(type=nextcord.ActivityType.watching, name= status))

    await asyncio.sleep(15)
client.loop.create_task(ch_pr())





client.run(TOKEN)
