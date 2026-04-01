from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands
from responses import get_name, load_json, multi_name
from random import randint

# Load in token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


# Bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = commands.Bot(command_prefix='!' ,intents = intents)

# Message functionality
def process_message(user_message: str) -> str:
    additionalNames: int = -1
    # handle a random amount of baby names

    if user_message == 'r':
        return get_name(randint(0, 150))
    # get multiple names in a row if the user does x followed by something
    elif user_message.startswith('x') and len(user_message) > 1:
        return multi_name(user_message[1:])
    
    # standard case, parse number of middle names
    try:
        #get how many middle names we want
        additionalNames = int(user_message)
    except:
        #default case
        additionalNames = 0
    
    # handle well-formed, malicious user input
    if additionalNames < 0:
        return "Nice Try"
    if additionalNames > 150:
        return "Too many middle names"
    # main call to get the name
    try:
        response: str = get_name(additionalNames)
        return response
    except Exception as e:
        print(e)
        return ":("

# The main command
@client.command(name="baby", help="""Gets a baby name. Use !baby <n> to get a baby name with n middle names and !baby r to get a random number of middle names.\n
                                    Use an x with a number next to it to get multiple names at once!""")
async def baby(ctx: commands.Context, arg: str = "") -> None:
    try:
        await ctx.send(process_message(arg))
    except Exception as e:
        print("Something happened, and we can't respond")
        print(e)
# Handling Startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# about command
@client.command(name="about", help="learn about this bot")
async def about(ctx: commands.Context) -> None:
    try:
        await ctx.send("""Made by Jaden!\n
                       GitHub: https://github.com/jadenabrams100/Baby-Name-Bot""")
    except Exception as e:
        print("Something happened and we couldn't respond")
        print(e)


# Main function
def main() -> None:
    load_json()
    client.run(token=TOKEN)

# Entry point
if __name__ == '__main__':
    main()