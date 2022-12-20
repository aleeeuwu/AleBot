import discord
from discord.ext import commands
import json
import os

# you'll have to import this function like "from botcmds.priviliges import adminCheck" since having it in a file called "adminCheck" makes python think I'm trying to call the file as a function
def adminCheck(userid):
    return (str(userid) in adminList.keys() or foobot.is_owner(discord.Object(id=int(userid))))

@commands.hybrid_group()
async def privilege(ctx):
    if ctx.invoked_subcommand is None:
        if adminCheck(ctx.author.id):
            await ctx.send("You are a privileged user")
        else:
            await ctx.send('You are not a privileged user')

@privilege.command()
async def add(ctx, id):
    #this doesn't work
    if id == None:
        await ctx.send('Please specify the id of the user you want to make privileged')
        return

    if adminCheck(ctx.author.id):
        if adminCheck(id):
            await ctx.send('This user is already privileged')
        else:
            adminList[id] = 1

            json_object = json.dumps(adminList, indent=4)
            with open("adminList.json", "w") as o:
                o.write(json_object)

            await ctx.send('This user is now a privileged user')
    else:
        await ctx.send('You need privileges to use this command!')

async def setup(bot):
    bot.add_command(privilege)
    global foobot
    foobot = bot
    global adminList
    if os.path.exists("adminList.json"):
        with open("adminList.json", "r") as o:
            adminList = json.loads(o.read())
    else:
        adminList = {}
        with open("adminList.json", "w") as o:
            json_object = json.dumps(adminList, indent=4)
            o.write(json_object)

