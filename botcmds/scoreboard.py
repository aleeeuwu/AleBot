from discord.ext import commands
import json

# kinda dumb, imports the global variable
from botcmds.gilbert import scoresList, triesList, namesList

@commands.group(description='gilbert scoreboard')
async def scoreboard(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Type "ale!scoreboard guesses" or "ale!scoreboard tries"')

@scoreboard.command()
async def guesses(ctx):
    # really dumb, need to do this because I can't get the user's name before the bot logs on
    #with open("scores.json", "r") as o:
    #    scores = json.loads(o.read())
    if not namesList:
        for userid in triesList:
            currentUser = await foobot.fetch_user(userid)
            namesList[userid] = currentUser.name
    
    boardStr = ''
    
    for i in sorted(scoresList.items(), key=lambda x:x[1], reverse=True):
        boardStr += (namesList[i[0]] + " - " + str(i[1]) + '\n')
    
    await ctx.send(boardStr)

@scoreboard.command()
async def tries(ctx):
    #with open("tries.json", "r") as o:
    #    tries = json.loads(o.read())
    if not namesList:
        for userid in triesList:
            currentUser = await foobot.fetch_user(userid)
            namesList[userid] = currentUser.name
    
    boardStr = ''
    
    for i in sorted(triesList.items(), key=lambda x:x[1], reverse=True):
        boardStr += (namesList[i[0]] + " - " + str(i[1]) + '\n')
    
    await ctx.send(boardStr)

async def setup(bot):
    bot.add_command(scoreboard)
    global foobot
    foobot = bot
