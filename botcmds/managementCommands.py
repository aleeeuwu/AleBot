import discord
from discord.ext import commands
import subprocess
from botcmds.privilege import adminCheck

@commands.hybrid_command()
async def wget(ctx, file, filename):
    if adminCheck(ctx.author.id):
       subprocess.Popen(['powershell', 'wget', file, '-OutFile', filename])
        #i wanted to make it send the command after it got the file, but couldnt get it to work
        #await ctx.send(file=discord.File(filename))
    else:
        await ctx.send('You need privileges to use this command!')

@commands.hybrid_command(description='sends a file from the host\'s device.')
async def send(ctx, arg):
    if adminCheck(ctx.author.id):
        await ctx.send(file=discord.File(arg))
    else:
        await ctx.send('You need privileges to use this command!')

#deletes a message by its id
@commands.hybrid_command(description='deletes a message by its id')
async def delete(ctx,arg):
    if adminCheck(ctx.author.id):
        msg = await ctx.channel.fetch_message(arg)
        await msg.delete()
    else:
        await ctx.send('You need privileges to use this command!')

@commands.hybrid_command()
async def neofetch(ctx):
    p = subprocess.Popen(['bash', 'neofetch', '--stdout'], stdout=subprocess.PIPE)
    text = p.stdout.read()
    retcode = p.wait()
    await ctx.send(text.decode())

@commands.hybrid_command()
async def servers(ctx):
    if adminCheck(ctx.author.id):
        serverNames = ''
        for guild in foobot.guilds:
            serverNames = serverNames + guild.name + '\n'
        await ctx.send(serverNames)
    else:
        await ctx.send('You need privileges to use this command!')

@commands.hybrid_command()
async def dir(ctx):
    if adminCheck(ctx.author.id):
        command = subprocess.Popen(['cmd', '/c', 'dir', '/b'], stdout=subprocess.PIPE)
        text = command.stdout.read()
        retcode = command.wait()
        await ctx.send(text.decode())
    else:
        await ctx.send('You need privileges to use this command!')

async def setup(bot):
    bot.add_command(wget)
    bot.add_command(send)
    bot.add_command(delete)
    bot.add_command(neofetch)
    bot.add_command(servers)
    bot.add_command(dir)
    global foobot
    foobot = bot


