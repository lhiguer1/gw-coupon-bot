import discord
from discord.ext import commands

class GWCoupon(commands.Cog):
    """Retrives Goodwill Coupons"""
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_before_invoke(self, ctx):
        await ctx.send(f'[DEBUG] cog_before_invoke')


    async def cog_after_invoke(self, ctx):
        await ctx.send(f'[DEBUG] cog_after_invoke')

    @commands.command(name='gw_coupon')
    async def gw_coupon(self, ctx):
        cat_pics = list()
        cat_pics.append(discord.File(open('./cat0.jpg', 'rb'), filename='cat0.jpg'))
        cat_pics.append(discord.File(open('./cat1.jpg', 'rb'), filename='cat1.jpg'))

        await ctx.send(f'De marca baby!')
        await ctx.send(files=cat_pics)

def setup(bot):
    bot.add_cog(GWCoupon(bot))