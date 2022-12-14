from discord.ext import commands
from botcmds.privilege import adminCheck

@commands.group()
async def phone(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('you have to specify something dummy')

@phone.command()
async def start(ctx, phonechannelid2: int):
    if adminCheck(ctx.author.id):
        global textphone
        global first_phone_channel
        global second_phone_channel
        textphone = True
        first_phone_channel = int(ctx.channel.id)
        second_phone_channel = int(phonechannelid2)
        await ctx.send('Phone started')
        #await bot.fetch_channel(second_phone_channel).send('Incoming call! Say hello!')
        print(first_phone_channel)
        print(second_phone_channel)
        print(textphone)
    else:
        await ctx.send('You need privileges to use this command!')

@phone.command()
async def stop(ctx):
    if adminCheck(ctx.author.id):
        global textphone
        global first_phone_channel
        global second_phone_channel
        textphone = False
        first_phone_channel = 0
        second_phone_channel = 0
        await ctx.send('Phone stopped')
    else:
        await ctx.send('You need privileges to use this command!')

async def setup(bot):
    bot.add_command(phone)
