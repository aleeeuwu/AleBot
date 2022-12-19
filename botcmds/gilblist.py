from discord.ext import commands
import json
import os

@commands.hybrid_command(description='namelist of gilberts')
async def gilblist(ctx):
    with open("Gilberts.json", "r") as o:
        listGilbert = json.loads(o.read())
    
    list = ''
    first = True
    
    for i in listGilbert:
        if not first:
            list += ', '
        list += listGilbert[i][0]
        first = False
        
    await ctx.send(list)

async def setup(bot):
    # probably inefficient because this is checked for in gilbert.py already but whatever
    if not os.path.exists("Gilberts.json"):
        print("gilberts list not found, command disabled")
        return
    bot.add_command(gilblist)
