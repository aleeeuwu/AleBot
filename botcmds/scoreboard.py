from discord.ext import commands
import json
import os

# have to do this because importing a global variable like "from asdf import g" doesn't work (but for some reason importing an array does)
import botcmds.gilbert as g

@commands.hybrid_group(description='Gilbert scoreboard')
async def scoreboard(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Type "ale!scoreboard wins" or "ale!scoreboard attempts"')

@scoreboard.command()
async def wins(ctx):
    if not g.names_loaded:
        await ctx.send("Command currently disabled because the names aren't loaded yet")
        return

    if not os.path.exists("scoreboards/wins/" + str(ctx.guild.id) + ".json"):
        await ctx.send("The wins scoreboard is currently empty")
        return

    with open("scoreboards/wins/" + str(ctx.guild.id) + ".json", "r") as o:
        wins = json.loads(o.read())
        o.close()

    # really dumb, need to do this because I can't get the user's name before the bot logs on
    #with open("assets/scores.json", "r") as o:
    #    scores = json.loads(o.read())
    #if not names_list:
    #    for userid in tries_list:
    #        current_user = await foobot.fetch_user(userid)
    #        names_list[userid] = current_user.name
    
    board = ''
    
    for i in sorted(wins.items(), key=lambda x:x[1], reverse=True):
        board += (g.names_list[i[0]] + " - " + str(i[1]) + '\n')
    
    await ctx.send(board)

@scoreboard.command()
async def attempts(ctx):
    if not g.names_loaded:
        await ctx.send("Command currently disabled because the names aren't loaded yet")
        return

    if not os.path.exists("scoreboards/attempts/" + str(ctx.guild.id) + ".json"):
        await ctx.send("The attempts scoreboard is currently empty")
        return

    with open("scoreboards/attempts/" + str(ctx.guild.id) + ".json", "r") as o:
        attempts = json.loads(o.read())
        o.close()

    #if not names_list:
    #    for userid in tries_list:
    #        current_user = await foobot.fetch_user(userid)
    #        names_list[userid] = current_user.name
    
    board = ''
    
    for i in sorted(attempts.items(), key=lambda x:x[1], reverse=True):
        board += (g.names_list[i[0]] + " - " + str(i[1]) + '\n')
    
    await ctx.send(board)

async def setup(bot):
    bot.add_command(scoreboard)
    global foobot
    foobot = bot
