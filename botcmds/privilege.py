from discord.ext import commands
import json

@commands.command()
async def privilege(ctx):
        with open("adminList.json", "r") as o:
            adminList = json.loads(o.read())
    
        if str(ctx.author.id) in (adminList.keys()):
            await ctx.send('You are a privileged user')
        else:
            return

@commands.command()
async def privilegeadd(ctx, id):
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
    bot.add_command(privilegeadd)