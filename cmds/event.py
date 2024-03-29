from discord.ext import commands
from core.classes import Cog_Extension
import json

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["日常聊天"]))
        await channel.send(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["日常聊天"]))
        await channel.send(f"{member} leave!")


async def setup(bot):
    await bot.add_cog(Event(bot))
