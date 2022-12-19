from discord.ext import commands
import json
import random
import asyncio
import os

@commands.hybrid_command(description='gilbert')
async def gilbert(ctx, *, guess=None):
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
    if guess is None:
        return

    if idofuser not in namesList:
        currentUser = await foobot.fetch_user(idofuser)
        namesList[idofuser] = currentUser.name

    #sends a message if it was correct or not
    if guess.lower() in valueGilbert:
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

async def getNames():
    print("getting scoreboard names")
    # have to import THIS FILE because of weird python and asyncio shenanigans lmao
    import botcmds.gilbert as g
    if not namesList:
        for userid in triesList:
            currentUser = await foobot.fetch_user(userid)
            namesList[userid] = currentUser.name
    g.namesLoaded = True
    print("names stored")


async def setup(bot):
    global foobot
    foobot = bot
    global listGilbert
    if os.path.exists("Gilberts.json"):
        with open("Gilberts.json", "r") as o:
            listGilbert = json.loads(o.read())
        bot.add_command(gilbert)
    else:
        print("gilberts list not found, command disabled")
    # different name so that importing it in scoreboard.py doesn't make it import the function
    global triesList
    if os.path.exists("tries.json"):
        with open("tries.json", "r") as o:
            triesList = json.loads(o.read())
    else:
        triesList = {}
        json_object = json.dumps(triesList, indent=4)
        with open("tries.json", "w") as o:
            o.write(json_object)

    global scoresList
    if os.path.exists("scores.json"):
        with open("scores.json", "r") as o:
            scoresList = json.loads(o.read())
    else:
        scoresList = {}
        json_object = json.dumps(scoresList, indent=4)
        with open("scores.json", "w") as o:
            o.write(json_object)


    global namesList
    namesList = {}
    global namesLoaded 
    namesLoaded = False
    asyncio.ensure_future(getNames())
