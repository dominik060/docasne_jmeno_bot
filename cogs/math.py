import discord
import math
from discord.ext import commands
from discord.ext.commands import bot


class math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def m(self, ctx, *, expression: str):
        calculation = eval(expression)
        em = discord.embeds(color=discord.Color.green())
        em.add_field(name="Math:", value=f"{expression}")
        em.add_field(name="Answer:", value=f"{calculation}")
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(math(bot))