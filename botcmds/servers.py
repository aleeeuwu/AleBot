from discord.ext import commands
from botcmds.privilege import adminCheck

@commands.hybrid_command()
async def servers(ctx):
    if adminCheck(ctx.author.id):
        cunk = ''
        for guild in foobot.guilds:
            cunk = cunk + guild.name + '\n'
        await ctx.send(cunk)
    else:
        await ctx.send('You need privileges to use this command!')

async def setup(bot):
    bot.add_command(servers)
    global foobot
    foobot = bot
