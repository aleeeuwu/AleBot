from discord.ext import commands
import json

@commands.group()
async def privilege(ctx):
    if ctx.invoked_subcommand is None:
        with open("adminList.json", "r") as o:
            adminList = json.loads(o.read())
    
        if str(ctx.author.id) in (adminList.keys()):
            await ctx.send('You are a privileged user')
        else:
            return

@privilege.command()
async def add(ctx, id):
    #this doesn't work
    if id == None:
        await ctx.send('Please specify the id of the user you want to make privileged')
        return

    #this could be turned into a function
    with open("adminList.json", "r") as o:
        adminList = json.loads(o.read())

    if str(ctx.author.id) in (adminList.keys()):
        if str(id) in (adminList.keys()):
            await ctx.send('This user is already privileged')
        else:
            adminList[id] = 1

            json_object = json.dumps(adminList, indent=4)
            with open("adminList.json", "w") as o:
                o.write(json_object)

            await ctx.send('This user is now a privileged user')
    else:
        return

async def setup(bot):
    bot.add_command(privilege)