import discord
import asyncio
import os
import configparser
from discord.ext import commands
from botcmds.privilege import admin_check
import logging

logging.basicConfig(level=logging.INFO)

# Load configuration file (aleconfig.ini)
config = configparser.ConfigParser()
config.read('aleconfig.ini')

#watch out for the order of this:
cmd_names = ["privilege", "classic_commands", "management_commands", "cat", "comic_commands_thx_kittrz", "frisk", "mokou", "gilbert", "scoreboard", "gilblist", "uptime"];

class MyClient(commands.Bot):
    def __init__(self, *, command_prefix, intents: discord.Intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
    async def setup_hook(self):
        if not os.path.isdir("assets"):
            print("assets directory not found, creating it now")
            os.makedirs("assets")
        for name in cmd_names:
            print(name)
            await self.load_extension('botcmds.' + name)
        await self.tree.sync(guild=None)

intents = discord.Intents.default()
intents.message_content = True

#Prefix taken from aleconfig.ini
bot = MyClient(command_prefix=config["Main"]['prefix'], intents=intents)

@bot.hybrid_command()
async def reload(ctx):
    if admin_check(ctx.author.id):
        for name in cmd_names:
            await bot.reload_extension('botcmds.' + name)
        await bot.tree.sync(guild=None)
        await ctx.send('reloaded! (probably)')

@bot.hybrid_command()
async def owner(ctx):
    if await bot.is_owner(ctx.author):
        await ctx.send('you are the owner')
    else:
        await ctx.send('you are not')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("Unknown command. Do ale!help to see the command list")
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        await ctx.send("Something went wrong. Check your console for details.")
    print(error)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
#funny status

    try:
        onlinestatusini = config["Main"]['online_status']
    except:
        print('No online status set in config file. using default')
        onlinestatusini = 'online'

    if onlinestatusini == 'online': onlinestatus = discord.Status.online
    elif onlinestatusini == 'idle': onlinestatus = discord.Status.idle
    elif onlinestatusini == 'dnd': onlinestatus = discord.Status.dnd
    elif onlinestatusini == 'offline' or onlinestatusini == 'invisible': onlinestatus = discord.Status.invisible
    else:print('Invalid online status, using default')


    customstatus = discord.CustomActivity(name='gaming edition')
    try:
        customstatus = discord.CustomActivity(name=config['Main']['custom_status'])
    except:
        print('No custom status set in config file. using default')


    await bot.change_presence(status=onlinestatus, activity=customstatus)


token = config['Main']['token']

async def main():
    async with bot:
        await bot.start(token)

asyncio.run(main())
