# AleBot

A small project that I made so I could get a grasp around the basics of programming.

It's a huge mess so expect to find issues and problems everywhere.

I'd really appreciate if you have any tips or things you think are worth adding or changing.

## Requirements

As mentioned above the current code is a mess so there are some things to do for the bot to function 100% as expected.

First, Python requirements:

1. Python 3.8 or higher
2. discord.py 2.1.0
3. `asyncio`, `catapi.py`, `requests`, `Pybooru` (the command using this is disabled by default and will probably get deleted soon)

Next, files the bot expects to exist (next to main.py):

1. `token.txt` - Discord bot token. This is the only required file for basic functionality.
2. `catapi.txt` - API key from [TheCatAPI](https://thecatapi.com/).
3. `frisk.txt` - List of links separated by newlines that is called when running "ale!frisk".
4. `gilbert.txt` - List of links separated by newlines that is called when running "ale!gilbold".
5. `Gilberts.json` - JSON file containing links and name aliases used by "ale!gilbert", formatted roughly as follows:
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
6. `scores.json` & `tries.json` - JSON files read from and written to by the "ale!gilbert" command and the "ale!scoreboard" subcommands.
9. `adminList.json` - JSON file containing the IDs of the users that can use privileged commands.
7. `REDDIT.png` - Just an image file uploaded to Discord when calling "ale!REDDIT".
8. `mokou/` - A folder with 700 images named `1.jpg` to `700.jpg`. The intended images for this folder can be found [here](https://twitter.com/jokanhiyou/status/1556186890428039168).
