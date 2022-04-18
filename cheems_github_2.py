# Imports of the packages and libraries that are required for the bot to run
import discord
from discord.ext import commands 
import random
from random import randint

# Defines the prefix to execute commands, replace the '!' with whatever you like to change the command prefix
client = commands.Bot(command_prefix="!")

# Responses for the 8-Ball command
responses = [
    'it is certain',
    'it is decidedly so',
    'without a doubt',
    'yes definitely',
    'you may rely on it',
    'as I see it, yes',
    'most like',
    'outlook good',
    'yes',
    'signs point to yes',
    'reply hazy, try again',
    'ask again later',
    'better not tell you now',
    'cannot predict now',
    'concentrate and ask again',
    'do not count on it',
    'my reply is no',
    'my sources say no',
    'outlook not so good',
    'very doubtful'
]

# Used to open the bot's token
with open([Enter/File/name/here]) as f:
    token = f.readline()
    token = token[13:] # This is used to adjust string length and is therefore optional. 


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

# Posts a gif of party cheems in the channel
@client.command(aliases=['rave', 'party time', 'party'])
async def partytime(ctx):
    await ctx.send("https://tenor.com/bFg80.gif")

# Posts a gif of samurai cheems in the channel
@client.command(aliases=['ninja', 'flower'])
async def samurai(ctx):
    await ctx.reply("https://tenor.com/bD9Ul.gif")

# Calls on the random function and 'responses' list to tell fortune like a magic 8-ball
@client.command(aliases=['fortune', '8ball', 'genie'])
async def eightball(ctx):
    await ctx.reply(random.choice(responses))

# Calls on the random function to 'flip a coin'
@client.command(aliases=['coin', 'toss', 'flip', 'coin toss'])
async def cointoss(ctx):
    coin_toss = ['heads!', 'tails!']
    await ctx.reply("The coin landed on " + random.choice(coin_toss))

# Calls on the random integer (randint) function to 'roll a dice'
@client.command(aliases=['dice', 'roll', 'die'])
async def diceroll(ctx):
    x = randint(1, 6)
    await ctx.send("You rolled a " + str(x))

# Creates a simple function which responds to messages in any Discord channel, as well as allowing for commands to still be processed. 
@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if message.content.lower() == 'i love you cheems':
            await message.reply("I love you too, friend!")
        if message.content.lower() == 'where are you cheems?':
            await message.reply("I am here friend! <:cheems:965594070351216690>") # This commands responds with a custom emote from my server, replace the section in angle brackets to fit your own emote
        if message.content.lower() == 'i am feeling comfy':
            await message.reply("I am feeling super comfy too! <:cheemsComfy:965594019054886932>") # This command responds with a custom emote from my server, replace the section in angle brackets to fit your own emote
        if message.content.lower() == 'this server is cool':
            await message.channel.send("This server really **is** cool :yum:")
        await client.process_commands(message)

client.run(token)