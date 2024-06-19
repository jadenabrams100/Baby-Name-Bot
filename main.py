from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands
from responses import get_response, load_json

# Load in token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)


# Bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = commands.Bot(command_prefix='!' ,intents = intents)

# Message functionality
def process_message(user_message: str) -> str:
    additionalNames: int = -1
    try:
        additionalNames = int(user_message)
    except:
        additionalNames = 0
    
    if additionalNames < 0:
        return "Nice Try"
    if additionalNames > 150:
        return "Too many middle names"
    try:
        response: str = get_response(additionalNames)
        return response
    except Exception as e:
        print(e)
        return ":("

# The main command
@client.command(name="baby")
async def test(ctx: commands.Context, arg: str = "") -> None:
    try:
        await ctx.send(process_message(arg))
    except Exception as e:
        print("Something happened, and we can't respond")
        print(e)
# Handling Startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# Main function
def main() -> None:
    load_json()
    client.run(token=TOKEN)

# Entry point
if __name__ == '__main__':
    main()