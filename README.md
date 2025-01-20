# AleBot

A small project that I made so I could get a grasp around the basics of programming.

It's a huge mess so expect to find issues and problems everywhere.

I'd really appreciate if you have any tips or things you think are worth adding or changing.

## Requirements

As mentioned above the current code is a mess so there are some things to do for the bot to function 100% as expected.

First, Python requirements (versions listed are what have been tested, newer versions may still work):

1. Python 3.8 or higher
2. discord.py 2.1.0
3. `asyncio`, `catapi.py`, `requests`

Next, files the bot expects to exist (next to main.py):

1. `aleconfig.ini` - Bot configuration, including the Discord bot token and (optionally) an API key from [TheCatAPI](https://thecatapi.com/). This is the only required file for basic functionality. An example is provided in this repository.
2. `assets/frisk.txt` - List of links separated by newlines that is called when calling the "frisk" command.
3. `assets/gilbert.txt` - List of links separated by newlines that is called when calling the "gilbold" command.
4. `assets/Gilberts.json` - JSON file containing links and name aliases used by the "gilbert" command, formatted roughly as follows:
```
{
    "https://cdn.discordapp.com/attachments/934379530729164810/934379708601237534/Ale.png": [
        "Ale"
    ],
    "https://cdn.discordapp.com/attachments/934379530729164810/934379935424974918/Trevor.png": [
        "Trevor",
        "TCAtrevor"
    ]
}
```
5. `assets/REDDIT.png` - Just an image file uploaded to Discord when calling the "reddit" command.
6. `assets/mokou/` - A folder with 700 images named `1.jpg` to `700.jpg`. The intended images for this folder can be downloaded from [a Tweet by the artist](https://twitter.com/jokanhiyou/status/1556186890428039168).

Some commands run under bash so on Windows you will need Windows Subsystem for Linux for them to work (the bot runs outside of the subsystem and will only call it when needed). With bash you should only need to install `neofetch` using a package manager.
