from discord.ext import commands
import json

@commands.group(description='gilbert scoreboard')
async def scoreboard(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Type "ale!scoreboard guesses" or "ale!scoreboard tries"')

@scoreboard.command()
async def guesses(ctx):
    with open("scores.json", "r") as o:
        scores = json.loads(o.read())
    
    boardStr = ''
    
    for i in sorted(scores.items(), key=lambda x:x[1], reverse=True):
        currentUser = await foobot.fetch_user(i[0])
        boardStr += (currentUser.name + " - " + str(i[1]) + '\n')
    
    await ctx.send(boardStr)

@scoreboard.command()
async def tries(ctx):
    with open("tries.json", "r") as o:
        tries = json.loads(o.read())
    
    boardStr = ''
    
    for i in sorted(tries.items(), key=lambda x:x[1], reverse=True):
        currentUser = await foobot.fetch_user(i[0])
        boardStr += (currentUser.name + " - " + str(i[1]) + '\n')
    
    await ctx.send(boardStr)

async def setup(bot):
    await bot.add_command(scoreboard)
    global foobot
    foobot = bot