# Imports of the packages and libraries that are required for the bot to run
import discord
from discord.ext import commands 

# Defines the prefix to execute commands, replace the '!' with whatever you like to change the command prefix
client = commands.Bot(command_prefix="!")

# Prints to the console when the bot is active.
@client.event
async def on_ready():
    print("Cheems is awake")

# Creates a simple "Hello" command which replies to the user.
@client.command()
async def hello(ctx):
    await ctx.reply("Hi there, my name is Cheems!")

# Creates a simple command which sends a message in the chat with examples of aliases.
@client.command(aliases=['yes', 'agreed'])
async def ofcourse(ctx):
    await ctx.send("Yes, that's correct!")

# Creates a simple function which responds to messages in any Discord channel, as well as allowing for commands to still be processed. 
@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if message.content.lower() == 'i love you cheems':
            await message.reply("I love you too, friend!")
        if message.content.lower() == 'this server is cool':
            await message.channel.send("This server really **is** cool :yum:")
        await client.process_commands(message)

client.run("[Enter token here]")
