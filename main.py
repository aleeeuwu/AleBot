#textphone = False
#first_phone_channel = 0
#second_phone_channel = 0

import discord
import asyncio
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='ale!', intents=intents)

cmdNames = ["classicCommands", "cat", "neofetch", "wget", "dir", "comicCommandsTHXkittrz", "frisk", "mokou", "servers", "gilbold", "gilbert", "scoreboard", "gilblist"];
# commands that dont need api keys or text files so it doesn't just crash when testing
#cmdNames = ["classicCommands", "neofetch", "wget", "dir", "comicCommandsTHXkittrz", "servers"];
async def setup():
    for name in cmdNames:
        print(name)
        await bot.load_extension('botcmds.' + name)

@bot.command()
async def reload(ctx):
    if await bot.is_owner(ctx.author):
        for name in cmdNames:
            await bot.reload_extension('botcmds.' + name)
        await ctx.send('reloaded! (probably)')

@bot.command()
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

#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#    if textphone == True:
#        if int(message.channel.id) == int(first_phone_channel):
#            channel = await bot.fetch_channel(int(second_phone_channel))
#            await channel.send(message.author.name + ': ' + message.content)
#        if int(message.channel.id) == int(second_phone_channel):
#            channel = await bot.fetch_channel(int(first_phone_channel))
#            await channel.send(message.author.name + ': ' + message.content)
#    await bot.process_commands(message)

with open('token.txt', 'r') as f:
    token = f.readline()

async def main():
    async with bot:
        await setup()
        await bot.start(token)

asyncio.run(main())

#bot.run(token)
