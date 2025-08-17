import discord
from discord.ext import commands, tasks
import datetime

class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_server_status.start()

    def cog_unload(self):
        self.check_server_status.cancel()

    def get_current_time(self):
        asia_dhaka_timezone = datetime.timezone(datetime.timedelta(hours=6))
        current_time = datetime.datetime.now(asia_dhaka_timezone).strftime("%Y-%m-%d %I:%M %p")
        return current_time

    @tasks.loop(minutes=1)
    async def check_server_status(self):
        try:
            response = requests.get("https://api.mcsrvping.com/query?server=play.uniprox.top")
            data = response.json()

            if data["online"]:
                players_online = data["players"]["online"]
                max_players = data["players"]["max"]
                latency = data["latency"]

                embed = discord.Embed(
                    title="UniProx Network",
                    color=discord.Color.green(),
                )
                embed.add_field(name="Server Status", value="Online ✅", inline=True)
                embed.add_field(name="Total Online 🧑‍💻", value=f"`{players_online}/{max_players}`", inline=True)
                embed.add_field(name='Server Ping', value=f"`{latency}` MS" , inline=False)
                embed.set_footer(text=f"Last checked at {self.get_current_time()}")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1155156564638969930/1178681597411733514/standard_1.gif?ex=6592b747&is=65804247&hm=c1fecc2f853666089e9aa8fbf76d95828eb7d65228b880c502d18f242e901306&")

                channel = self.bot.get_channel(1227597111051288687)
                message_id = 1227601331678871693
                message = await channel.fetch_message(message_id)
                await message.edit(embed=embed)
            else:
                channel = self.bot.get_channel(1227597111051288687)
                message_id = 1227601331678871693
                message = await channel.fetch_message(message_id)
                embed = discord.Embed(
                    title="Unity Network",
                    color=discord.Color.red(),
                )
                embed.add_field(name="Server Status", value="Offline ❌", inline=True)
                embed.set_footer(text=f"Last checked at {self.get_current_time()}")
                await message.edit(embed=embed)
        except Exception as e:
            print(f"{e}")

    @commands.command()
    async def mcstat(self, ctx, channel: discord.TextChannel = None):
        if not channel:
            channel = ctx.channel

        try:
            response = requests.get("https://api.mcsrvping.com/query?server=Spider.BitByte.Host")
            data = response.json()

            if data["online"]:
                players_online = data["players"]["online"]
                max_players = data["players"]["max"]
                latency = data["latency"]

                embed = discord.Embed(
                    title="UniProx Network",
                    color=discord.Color.green(),
                )
                embed.add_field(name="Server Status", value="Online ✅", inline=True)
                embed.add_field(name="Total Online 🧑‍💻", value=f"`{players_online}/{max_players}`", inline=True)
                embed.add_field(name='Server Ping', value=f"`{latency}` MS" , inline=False)
                embed.set_footer(text=f"Last checked at {self.get_current_time()}")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1155156564638969930/1178681597411733514/standard_1.gif?ex=6592b747&is=65804247&hm=c1fecc2f853666089e9aa8fbf76d95828eb7d65228b880c502d18f242e901306&")

                message = await channel.send(embed=embed)
                await ctx.message.delete()
            else:
                embed = discord.Embed(
                    title="UniProx Network",
                    color=discord.Color.red(),
                )
                embed.add_field(name="Server Status", value="Offline ❌", inline=True)
                embed.set_footer(text=f"Last checked at {self.get_current_time()}")

                message = await channel.send(embed=embed)
                await ctx.message.delete()
        except Exception as e:
            print(f"{e}")

async def setup(bot):
    await bot.add_cog(StatusCog(bot))