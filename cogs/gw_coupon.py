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
        COUPON_DIR = 'coupons'
        if not os.path.exists(COUPON_DIR):
            os.mkdir(COUPON_DIR)
        
        today = datetime.today()
        coupon_path = os.path.join(COUPON_DIR, calendar.month_name[today.month].lower()+'.png')

        coupon_png = discord.File(coupon_path)

        await ctx.send('De marca baby!', file=coupon_png)

def setup(bot):
    bot.add_cog(GWCoupon(bot))