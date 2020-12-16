import os
import sys
import time
import random
import asyncio
import traceback
import datetime
import discord
from discord.ext import commands
import requests
from pylint import extensions

print(discord.__version__)

TOKEN = os.environ["TOKEN"]

bot = discord.Client()
bot = commands.Bot(command_prefix="?")
# bot.remove_command('help')
init_extension = ['cogs.mod']
if __name__ == '__main__':
    for extension in init_extension:
        try:
            bot.load_extension(extension)
            print(f'Nacteno {extension}')
        except Exception as e:
            print(f'Nepodarilo se nacist {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.command(pass_context=True)
async def info(ctx):
    member = ctx.guild.member_count
    em = discord.Embed(color=discord.Color.green())
    em.title = ('Server Info')
    em.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    em.description = 'Vytvořil D0M1'
    em.add_field(name="Uživatelé", value=member, inline=False)
    em.add_field(name="Servery", value=len(bot.guilds))
    em.add_field(name="Online Uživatelé", value=str(len({m.id for m in bot.get_all_members() if m.status is not discord.Status.offline})))
    em.add_field(name='Kanály', value=f"{sum(1 for g in bot.guilds for _ in g.channels)}")
    await ctx.channel.send(embed=em)


@bot.command()
async def ping(ctx):
    em = discord.Embed(color=discord.Color.blue())
    em.add_field(name=f"Pong 🏓!", value=f"{round(bot.latency * 1000)}ms")
    await ctx.channel.send(embed=em)


@bot.command()
async def time(ctx):
    cas = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    await ctx.send(cas)

@bot.event#nefunguje
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="👾Normální Bytost👾")
    await bot.add_role(member, role)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.channel.send("Tenhle příkaz neznám! Zkus ?help")


@bot.event
async def on_ready():
    print('-' * len(str(bot.user.id)))
    print('Bot:')
    print(bot.user.name)
    print(bot.user.id)
    print('-' * len(str(bot.user.id)))
    await bot.change_presence(activity=discord.Game("?help"))


bot.run(TOKEN, bot=True)
