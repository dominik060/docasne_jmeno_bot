import discord
import yellow
from discord.ext import commands
import asyncio
import datetime
import random
from discord.ext.commands import bot
import time

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(fun(bot))