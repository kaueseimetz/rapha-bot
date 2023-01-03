#Imported libraries

import discord
from discord.ext import commands
import codecs

#vital variables

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
KEY = open("bot.key", "r").read() #Bot Key

bot = commands.Bot(command_prefix='/', intents=intents) 

#variables of texts

bot_commands = codecs.open("commands.txt", "r", "utf-8").read() #Commands for bot
rules = codecs.open("rules.txt", "r", "utf-8").read()
version = codecs.open("version.txt", "r").read()
RIP_he = codecs.open("RIP_he.txt", "r", "utf-8").read()
RIP_she = codecs.open("RIP_she.txt", "r", "utf-8").read()

#variables of versions

Discord_version = "2.0.1"
Bot_version = "1.1"

#Event OnReady()
@bot.event
async def on_ready():
    print(f"Discord version: {Discord_version}")
    print(f"Bot vesion: {Bot_version}")
    print(f"Estou conectado como {bot.user}")

#Event OnMessage()    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return     
    await bot.process_commands(message)    

#Command Rules
@bot.command(name="regras")
async def send_rules(ctx):
    name = ctx.author.name 
    await ctx.send(rules)
    
#Command Version 
@bot.command(name="bot.version")
async def bot_version(ctx):
    await ctx.send(version)
    
#List Commands
@bot.command(name="commands")
async def commands(ctx):
    await ctx.send(bot_commands)

# F Pelé
@bot.command(name="RIP_Pele")
async def RIP_Pele(ctx):
    await ctx.send(RIP_he)

# F Bethinha
@bot.command(name="RIP_Beth")
async def RIP_Beth(ctx):
    await ctx.send(RIP_she)
    
@bot.command(name="RIP_EU")
async def bot_version(ctx):
    await ctx.send(f"{ctx.author.mention} foi de base...")
    await ctx.send("foi de comes e bebes...")
    await ctx.send("foi de F...")
    await ctx.send("infelizmente não tankou...")

#@bot.command(name="KILL_BOT_USER_NOW")
#async def KILL_BOT():
#    exit()

bot.run(KEY)