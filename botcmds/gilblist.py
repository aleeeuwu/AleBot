from discord.ext import commands
import json

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
    bot.add_command(gilblist)
