import discord
from discord.ext import commands
import time
import json
import os

async def bonus_check(guild_id: int, user_id: int):
    
    print('Not implemented: bonus check')
    return

@commands.hybrid_command(description='Activate the Gilbert multiplier to temporarily double your points earned from a guess!')
async def gilbonus(ctx):
    
    #Checks to see if there's a scoreboard wins file for the server
    if not os.path.exists("scoreboards/wins/" + str(ctx.guild.id) + ".json"):
        await ctx.send("The wins scoreboard is currently empty")
        return
    
    #Reads the scoreboard file for the server
    else:
        wins = {}
        with open("scoreboards/wins/" + str(ctx.guild.id) + ".json", "r") as o:
            wins = json.loads(o.read())
            o.close()

    #Checks if the user is in the file
    if str(ctx.author.id) not in wins.keys():
        await ctx.send("You currently do not have any Gilpoints in this server")
        return

    class Confirm(discord.ui.View):
        @discord.ui.button(label='Activate', style=discord.ButtonStyle.green)
        async def confirm(self, interaction, button):
            if interaction.user.id == ctx.author.id:
                await interaction.response.send_message(interaction.user.display_name + ' has activated their Gilbert score multiplier!', ephemeral=False)
                self.value = True
                self.stop()
    
    view = Confirm()
    
    await ctx.send('Do you want to activate your Gilbert score multiplier in this server?', view=view, ephemeral=True)
    
    # Wait for the View to stop listening for input...
    await view.wait()
    
    # If the button was pressed...
    if view.value:
        if ctx.guild.id not in bonuses.keys():
            bonuses[ctx.guild.id] = {}
        bonuses[ctx.guild.id][ctx.author.id] = int(time.time())
        # CODE TO ACTIVATE MULTIPLIER GOES HERE
        print('[' + time.asctime() + ']', 'User ID', ctx.author.id, 'in guild ID', ctx.guild.id, 'activated Gilbert multiplier.')

async def setup(bot):
    bot.add_command(gilbonus)
    global bonuses
    bonuses = {}