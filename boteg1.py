# pip install discord.py
import discord
from discord.ext import commands

token = "" # Nunca compartir

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=";",intents=intents) # Variable del bot

@bot.event # Evento del bot
async def on_ready(_): # async: Espera a Discord, on_ready: Para chequear si el bot corre
    print(f"Corriendo como {bot.user}")

@bot.command() # Para comandos
async def ping(ctx): # ctx: para mandar mensajes
    await ctx.send("pong") # await: Espera a Discord

bot.run(token) # Enciende el bot por su token
