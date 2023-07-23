import discord
from discord.ext import commands
import time

async def bonus_check(guild_id: int, user_id: int):
    # CODE FOR BONUS CHECK FUNCTION GOES HERE
    print('Not implemented: bonus check')
    return

@commands.hybrid_command(description='Activate the Gilbert multiplier to temporarily double your points earned from a guess!')
async def gilbonus(ctx):
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
        # CODE TO ACTIVATE MULTIPLIER GOES HERE
        print('[' + time.asctime() + ']', 'User ID', ctx.author.id, 'in guild ID', ctx.guild.id, 'activated Gilbert multiplier.')

async def setup(bot):
    bot.add_command(gilbonus)