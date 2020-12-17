import re
from urllib import parse, request
import discord
import requests
from discord.ext import commands
import random
class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def youtube(self, ctx, *, search):
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
        await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

    @commands.command(aliases=['8b'], pass_context=True)
    async def _8ball(self, ctx, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        em = discord.Embed(color=discord.Color.grey())
        em.add_field(name="Otázka: ", value=f"{question}", inline=False)
        em.add_field(name="Odpověď: ", value=f"{random.choice(responses)}")
        await ctx.channel.send(embed=em)

    @commands.command()
    async def cat(self, ctx):
        response = requests.get('https://aws.random.cat/meow')
        data = response.json()
        await ctx.channel.send(data['file'])

    @commands.command()
    async def say(self, ctx, *args):
        response = ""
        for arg in args:
            response = response + " " + arg
        await ctx.channel.send(response)

def setup(bot):
    bot.add_cog(fun(bot))