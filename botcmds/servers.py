from discord.ext import commands

@commands.command()
async def servers(ctx):
    cunk = ''
    for guild in foobot.guilds:
        cunk = cunk + guild.name + '\n'
    await ctx.send(cunk)

async def setup(bot):
    bot.add_command(servers)
    global foobot
    foobot = bot
