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

        await ctx.send('De marca baby!', file=coupon_png)

def setup(bot):
    bot.add_cog(GWCoupon(bot))