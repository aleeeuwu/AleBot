from discord.ext import commands
import json

# have to do this because importing a global variable like "from asdf import g" doesn't work (but for some reason importing an array does)
import botcmds.gilbert as g

@commands.hybrid_group(description='gilbert scoreboard')
async def scoreboard(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Type "ale!scoreboard guesses" or "ale!scoreboard tries"')

@scoreboard.command()
async def guesses(ctx):
    if not g.namesLoaded:
        await ctx.send("Command currently disabled because the names aren't loaded yet")
        return

    if not g.scoresList:
        await ctx.send("The guesses scoreboard is currently empty")
        return
    # really dumb, need to do this because I can't get the user's name before the bot logs on
    #with open("scores.json", "r") as o:
    #    scores = json.loads(o.read())
    #if not namesList:
    #    for userid in triesList:
    #        currentUser = await foobot.fetch_user(userid)
    #        namesList[userid] = currentUser.name
    
    boardStr = ''
    
    for i in sorted(g.scoresList.items(), key=lambda x:x[1], reverse=True):
        boardStr += (g.namesList[i[0]] + " - " + str(i[1]) + '\n')
    
    await ctx.send(boardStr)

@scoreboard.command()
async def tries(ctx):
    if not g.namesLoaded:
        await ctx.send("Command currently disabled because the names aren't loaded yet")
        return

    if not g.triesList:
        await ctx.send("The tries scoreboard is currently empty")
        return
    #with open("tries.json", "r") as o:
    #    tries = json.loads(o.read())
    #if not namesList:
    #    for userid in triesList:
    #        currentUser = await foobot.fetch_user(userid)
    #        namesList[userid] = currentUser.name
    
    boardStr = ''
    
    for i in sorted(g.triesList.items(), key=lambda x:x[1], reverse=True):
        boardStr += (g.namesList[i[0]] + " - " + str(i[1]) + '\n')
    
    await ctx.send(boardStr)

async def setup(bot):
    bot.add_command(scoreboard)
    global foobot
    foobot = bot
