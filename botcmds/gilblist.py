from discord.ext import commands
import json
import os

@commands.hybrid_command(description='namelist of gilberts')
async def gilblist(ctx):
    with open("assets/Gilberts.json", "r") as o:
        gilbert_list = json.loads(o.read())
        o.close()
    
    list = ''
    first = True
    
    for i in gilbert_list:
        if not first:
            list += ', '
        list += gilbert_list[i][0]
        first = False
        
    await ctx.send(list)

async def setup(bot):
    # probably inefficient because this is checked for in gilbert.py already but whatever
    if not os.path.exists("assets/Gilberts.json"):
        print("assets/Gilberts.json not found, gilblist command disabled")
        return
    bot.add_command(gilblist)
