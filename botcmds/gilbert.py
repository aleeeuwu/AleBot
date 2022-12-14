from discord.ext import commands
import json
import random

@commands.command(description='gilbert')
async def gilbert(ctx, *, guessGilbert=None):
    if not namesLoaded:
        await ctx.send("Command currently disabled because the names aren't loaded yet")
        return
    # really dumb, need to do this because I can't get the user's name before the bot logs on
    #if not namesList:
    #    for userid in triesList:
    #        currentUser = await foobot.fetch_user(userid)
    #        namesList[userid] = currentUser.name

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

    if idofuser not in namesList:
        currentUser = await foobot.fetch_user(idofuser)
        namesList[idofuser] = currentUser.name

    #sends a message if it was correct or not
    if guessGilbert.lower() in valueGilbert:
        await ctx.send('Congratulations, ' + ctx.author.mention + '!' + ' You are the Godbert, you got 1 Gilpoint!')

        #to open a file to read
        #with open("scores.json", "r") as o:
        #    scores = json.loads(o.read())

        #if user exists they get one point...
        if str(idofuser) in (scoresList.keys()):
            scoresList[str(idofuser)] += 1

        #and if they don't, they get added
        else:
            scoresList[str(idofuser)] = 1
        
        #finally it writes the score to the file
        json_object = json.dumps(scoresList, indent=4)
        with open("scores.json", "w") as o:
            o.write(json_object)

        #now for the tries:
        #with open("tries.json", "r") as o:
        #    tries = json.loads(o.read())

        if str(idofuser) in (triesList.keys()):
            triesList[str(idofuser)] += 1

        else:
            triesList[idofuser] = 1
        
        json_object = json.dumps(triesList, indent=4)
        with open("tries.json", "w") as o:
            o.write(json_object)

    #in case of catastrophic failure:
    else:
        await ctx.send('Tough luck!')
        #with open("tries.json", "r") as o:
        #    tries = json.loads(o.read())

        if str(idofuser) in (triesList.keys()):
            triesList[str(idofuser)] += 1

        else:
            triesList[str(idofuser)] = 1
        
        json_object = json.dumps(triesList, indent=4)
        with open("tries.json", "w") as o:
            o.write(json_object)

async def setup(bot):
    bot.add_command(gilbert)
    global foobot
    foobot = bot
    global listGilbert
    with open("Gilberts.json", "r") as o:
        listGilbert = json.loads(o.read())
    # different name so that importing it in scoreboard.py doesn't make it import the function
    global triesList
    with open("tries.json", "r") as o:
        triesList = json.loads(o.read())
    global scoresList
    with open("scores.json", "r") as o:
        scoresList = json.loads(o.read())


    global namesList
    namesList = {}
    global namesLoaded 
    namesLoaded = False
