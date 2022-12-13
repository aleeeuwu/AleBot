from discord.ext import commands
import json
import random

@commands.command(description='gilbert')
async def gilbert(ctx, *, guessGilbert=None):
    with open("Gilberts.json", "r") as o:
        listGilbert = json.loads(o.read())

    #picks random bert
    randomGilbert = random.choice(list(listGilbert.keys()))

    #list of values of the random bert in lowercase
    valueGilbert = [item.lower() for item in listGilbert[randomGilbert]]

    #hope
    idofuser = ctx.author.id

    #sends random bert
    await ctx.send(randomGilbert)

    #exception if no guess
    if guessGilbert is None:
        return

    #sends a message if it was correct or not
    if guessGilbert.lower() in valueGilbert:
        await ctx.send('Congratulations, ' + ctx.author.mention + '!' + ' You are the Godbert, you got 1 Gilpoint!')

        #to open a file to read
        with open("scores.json", "r") as o:
            scores = json.loads(o.read())

        #if user exists they get one point...
        if str(idofuser) in (scores.keys()):
            scores[str(idofuser)] += 1

        #and if they don't, they get added
        else:
            scores[str(idofuser)] = 1
        
        #finally it writes the score to the file
        json_object = json.dumps(scores, indent=4)
        with open("scores.json", "w") as o:
            o.write(json_object)

        #now for the tries:
        with open("tries.json", "r") as o:
            tries = json.loads(o.read())

        if str(idofuser) in (tries.keys()):
            tries[str(idofuser)] += 1

        else:
            tries[idofuser] = 1
        
        json_object = json.dumps(tries, indent=4)
        with open("tries.json", "w") as o:
            o.write(json_object)

    #in case of catastrophic failure:
    else:
        await ctx.send('Tough luck!')
        with open("tries.json", "r") as o:
            tries = json.loads(o.read())

        if str(idofuser) in (tries.keys()):
            tries[str(idofuser)] += 1

        else:
            tries[str(idofuser)] = 1
        
        json_object = json.dumps(tries, indent=4)
        with open("tries.json", "w") as o:
            o.write(json_object)

async def setup(bot):
    bot.add_command(gilbert)
