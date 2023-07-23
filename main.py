import discord
import asyncio
import os
from discord.ext import commands
from botcmds.privilege import admin_check
import logging

logging.basicConfig(level=logging.INFO)

#watch out for the order of this:
cmd_names = ["privilege", "classic_commands", "management_commands", "cat", "comic_commands_thx_kittrz", "frisk", "mokou", "gilbonus", "gilbert", "scoreboard", "gilblist", "uptime"];

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
bot = MyClient(command_prefix='ale!', intents=intents)

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
#funny game
    game = discord.Game("gaming edition")
#funny status
    await bot.change_presence(status=discord.Status.online, activity=game)

with open('token.txt', 'r') as f:
    token = f.readline()
    f.close()

async def main():
    async with bot:
        await bot.start(token)

asyncio.run(main())
