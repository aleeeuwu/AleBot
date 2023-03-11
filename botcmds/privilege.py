import discord
from discord.ext import commands
import json
import os

# you'll have to import this function like "from botcmds.priviliges import admin_check" since having it in a file called "admin_check" makes python think I'm trying to call the file as a function
async def admin_check(userid):
    if str(userid) in admin_list.keys() or await foobot.is_owner(discord.Object(id=int(userid))):
        return True
    else:
        return False

@commands.hybrid_group(description='Checks to see if you are a privileged user')
async def privilege(ctx):
    if ctx.invoked_subcommand is None:
        if await admin_check(ctx.author.id):
            await ctx.send("You are a privileged user")
        else:
            await ctx.send('You are not a privileged user')

@privilege.command()
async def add(ctx, id):
    #this doesn't work
    if id == None:
        await ctx.send('Please specify the id of the user you want to make privileged')
        return

    if await admin_check(ctx.author.id):
        if await admin_check(id):
            await ctx.send('This user is already privileged')
        else:
            admin_list[id] = 1

            json_object = json.dumps(admin_list, indent=4)
            with open("assets/adminList.json", "w") as o:
                o.write(json_object)
                o.close()

            await ctx.send('This user is now a privileged user')
    else:
        await ctx.send('You need privileges to use this command!')

async def setup(bot):
    bot.add_command(privilege)
    global foobot
    foobot = bot
    global admin_list
    if os.path.exists("assets/adminList.json"):
        with open("assets/adminList.json", "r") as o:
            admin_list = json.loads(o.read())
            o.close()
    else:
        admin_list = {}
        with open("assets/adminList.json", "w") as o:
            json_object = json.dumps(admin_list, indent=4)
            o.write(json_object)
            o.close()

