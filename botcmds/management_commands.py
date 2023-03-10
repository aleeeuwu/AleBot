import discord
from discord.ext import commands
import subprocess
from botcmds.privilege import admin_check

@commands.hybrid_command(description='Download a file from the internet')
async def wget(ctx, link, filename=None):
    if await admin_check(ctx.author.id):
        if filename is None:
            p = subprocess.Popen(['bash', '-c', 'wget ' + link], cwd='assets')
        else:
            p = subprocess.Popen(['bash', '-c', 'wget ' + link + ' -O \"' + filename + '\"'], cwd='assets')
        p.wait()
        await ctx.send('File saved! (probably!)')
    else:
        await ctx.send('You need privileges to use this command!')

@commands.hybrid_command(description='sends a file from the host\'s device.')
async def send(ctx, arg):
    if await admin_check(ctx.author.id):
        await ctx.send(file=discord.File(arg))
    else:
        await ctx.send('You need privileges to use this command!')

#deletes a message by its id
@commands.hybrid_command(description='deletes a message by its id')
async def delete(ctx,arg):
    if await admin_check(ctx.author.id):
        msg = await ctx.channel.fetch_message(arg)
        await msg.delete()
    else:
        await ctx.send('You need privileges to use this command!')

@commands.hybrid_command()
async def neofetch(ctx):
    text = subprocess.check_output(['bash', '-c', 'neofetch --stdout'])
    await ctx.send(text.decode())

@commands.hybrid_command()
async def servers(ctx):
    if await admin_check(ctx.author.id):
        server_names = ''
        for guild in foobot.guilds:
            server_names = server_names + guild.name + '\n'
        await ctx.send(server_names)
    else:
        await ctx.send('You need privileges to use this command!')

@commands.hybrid_command(descriptions='Get a list of files in the current directory')
async def dir(ctx, dir=None):
    if await admin_check(ctx.author.id):
        if dir is None:
            command = subprocess.Popen(['bash', '-c', 'ls -1'], stdout=subprocess.PIPE)
        else:
            command = subprocess.Popen(['bash', '-c', 'ls -1 \"' + dir + '\"'], stdout=subprocess.PIPE)
        command.wait()
        text = command.stdout.read()
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


