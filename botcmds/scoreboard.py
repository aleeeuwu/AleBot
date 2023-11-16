from discord.ext import commands
import json
import os
from botcmds.gilbert import get_scoreboard

@commands.hybrid_group(description='Gilbert scoreboard')
async def scoreboard(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Type "ale!scoreboard wins" or "ale!scoreboard attempts"')

@scoreboard.command()
async def wins(ctx):
    wins = await get_scoreboard("wins", ctx.guild.id)
    
    if wins == {}:
        await ctx.send("The wins scoreboard is currently empty")
        return
    
    async with ctx.typing():
        await ctx.guild.chunk(cache=True)
        
        board = ''
        
        for i in sorted(wins.items(), key=lambda x:x[1], reverse=True):
            user = ctx.guild.get_member(int(i[0]))
            if user is None:
                user = await foobot.fetch_user(int(i[0]))
            board += (user.display_name + " - " + str(i[1]) + '\n')
        
    await ctx.send(board)

@scoreboard.command()
async def attempts(ctx):
    attempts = await get_scoreboard("attempts", ctx.guild.id)
    
    if attempts == {}:
        await ctx.send("The attempts scoreboard is currently empty")
        return
    
    async with ctx.typing():
        await ctx.guild.chunk(cache=True)
        
        board = ''
        
        for i in sorted(attempts.items(), key=lambda x:x[1], reverse=True):
            user = ctx.guild.get_member(int(i[0]))
            if user is None:
                user = await foobot.fetch_user(int(i[0]))
            board += (user.display_name + " - " + str(i[1]) + '\n')
    
    await ctx.send(board)

async def setup(bot):
    bot.add_command(scoreboard)
    global foobot
    foobot = bot