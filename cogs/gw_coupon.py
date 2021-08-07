import discord
import os
import calendar
from datetime import datetime
from discord.ext import commands

class GWCoupon(commands.Cog):
    """Retrives Goodwill Coupons"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gw_coupon')
    async def gw_coupon(self, ctx: commands.Context):
        today = datetime.today()
        
        coupon_png = discord.File(os.path.join('coupons', calendar.month_name[today.month].lower() + '.png'))
        

        # check if this months coupon is in the data structure.
        # if not month in data structure
        ## download coupon
        # return coupn

        await ctx.send(f'De marca baby!')
        await ctx.send(file=coupon_png)

def setup(bot):
    bot.add_cog(GWCoupon(bot))