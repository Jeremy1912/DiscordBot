import os
import discord
import urllib
import keep_alive
import asyncio
import time
from discord.ext import commands


sebi = commands.Bot(command_prefix='!', activity=discord.Activity(type=discord.ActivityType.watching, name="ProGo beim valorant spielen zu"))
#sebi.remove_command('help')
sebi.owner_id = 780727019133992981
__version__ = '1.0'

@sebi.event
async def on_ready():
  while 1:
    urllib.request.urlopen("https://ProGoBot.lpsebi.repl.co")
    await asyncio.sleep(500)
  print("Logging in...")
  print(f"__version__")

@sebi.command()
async def creator(ctx):
  embed=discord.Embed(color=0xff0000)
  embed.set_author(name="Creator!")
  embed.add_field(name="The creator of this bot is ", value="<@780727019133992981>", inline=True)
  embed.set_footer(text="ProGoBot")
  await ctx.send(embed=embed)

@sebi.command()
async def hi(ctx):
  await ctx.send("Hi")

@sebi.command()
async def progo(ctx):
  await ctx.send("ProGo")

@sebi.command()
async def ping(ctx):
  embed=discord.Embed(color=0xff0000)
  embed.set_author(name="My Ping:")
  embed.add_field(name="⌛", value=f"{round(sebi.latency * 1000)} ms", inline=True)
  embed.set_footer(text="ProGoBot")
  await ctx.send(embed=embed)



@sebi.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Dazu hast du keine Rechte!", color=0xff0000)
        embed.set_author(name="Error!", icon_url="https://sebibot.lpsebi.repl.co/favicon.png")
        embed.set_footer(text= "Error code: discord.ext.commands.errors.MissingPermissions: You are missing permission(s) to run this command.")
        await ctx.send(embed=embed)


@sebi.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(title="Ich habe dazu keine Rechte!", color=0xff0000)
        embed.set_author(name="Error!", icon_url="https://sebibot.lpsebi.repl.co/favicon.png")
        embed.set_footer(text="Error code: discord.ext.commands.errors.BotMissingPermissions: Bot is missing permission(s) to run this command.")
        await ctx.send(embed=embed)


@sebi.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Du hast dazu keine Rechte!", color=0xff0000)
        embed.set_author(name="Error!", icon_url="https://sebibot.lpsebi.repl.co/favicon.png")
        embed.set_footer(text="Error code: discord.ext.commands.errors.MissingPermissions: You are missing permission(s) to run this command.")
        await ctx.send(embed=embed)


@sebi.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Diesen Command gibt es nicht!", color=0xff0000)
        embed.set_author(name="Error!", icon_url="https://sebibot.lpsebi.repl.co/favicon.png")
        embed.set_footer(text="Error code: discord.ext.commands.errors.CommandNotFound: Command is not found.")
        await ctx.send(embed=embed)



keep_alive.keep_alive()
ENV_TOKEN = os.environ['TOKEN']
sebi.run(ENV_TOKEN)