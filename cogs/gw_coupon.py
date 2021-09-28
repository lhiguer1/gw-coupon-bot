import discord
import os
import calendar
from datetime import datetime
from discord.ext import commands
import gw_coupon_downloader

class GWCoupon(commands.Cog):
    """Retrives Goodwill Coupons"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gw_coupon', help="Get Goodwill coupon.")
    async def gw_coupon(self, ctx: commands.Context):
        COUPON_DIR = gw_coupon_downloader.COUPON_PATH
        if not os.path.exists(COUPON_DIR):
            os.mkdir(COUPON_DIR)
        
        coupon_path = os.path.join(COUPON_DIR, calendar.month_name[datetime.today().month].lower()+'.png')
        
        if not os.path.isfile(coupon_path):
            async with ctx.typing():
                gw_coupon_downloader.download()
        
        try:
            coupon_png = discord.File(coupon_path)
            await ctx.send('De marca baby!', file=coupon_png)
        except:
            pass

def setup(bot):
    bot.add_cog(GWCoupon(bot))