import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import re
import datetime
from datetime import timedelta

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_current_time(self):
        asia_dhaka_timezone = datetime.timezone(datetime.timedelta(hours=6))
        current_time = datetime.datetime.now(asia_dhaka_timezone).strftime("%Y-%m-%d %I:%M %p")
        return current_time

    @commands.hybrid_command(name="announce", aliases=["msg"])
    async def msg(self, ctx, channel_id: int,ping: str, *, message):
        mentions = []

        if ping.lower() == "@everyone":
            mentions.append(discord.AllowedMentions(everyone=True))
        elif ping.lower() == "@here":
            mentions.append(discord.AllowedMentions(here=True))
        else:
            user = discord.utils.get(ctx.guild.members, name=ping.lstrip("@"))
            if not user:
                user = discord.utils.get(ctx.guild.roles, name=ping.lstrip("@"))

            if user:
                mentions.append(user)

        full_message = f"{ping} {message}"

        announcement_channel = self.bot.get_channel(channel_id)

        if announcement_channel:
            if ctx.message.attachments:
                for attachment in ctx.message.attachments:
                    await announcement_channel.send(file=await attachment.to_file(), content=full_message, allowed_mentions=discord.AllowedMentions(*mentions))
            else:
                await announcement_channel.send(content=full_message, allowed_mentions=discord.AllowedMentions(*mentions))
            await ctx.send("Announcement sent successfully!", delete_after=5)
            await ctx.message.delete()
        else:
            await ctx.send("Invalid announcement channel ID. Please check the configuration.")

    @commands.hybrid_command(name="ban")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user: discord.Member, reason: str = None):
        embed = discord.Embed(
            title="Punishment Given",
            description=f"{user.mention} **is banned**",
            color=discord.Color.red()
        )
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.add_field(name="Banned by", value=f"{ctx.author.mention}", inline= True)
        embed.set_footer(text=f"Punishment given at {self.get_current_time()}")
        await user.send(embed=embed)
        await ctx.send(embed=embed)
        await user.ban(reason=reason)
        await ctx.message.delete()

    @commands.hybrid_command(name="kick")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user: discord.Member, reason: str = None):
        embed = discord.Embed(
            title="Punishment Given",
            description=f"{user.mention} **is Kicked out**",
            color=discord.Color.red()
        )
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.add_field(name="Banned by", value=f"{ctx.author.mention}", inline= True)
        embed.set_footer(text=f"Punishment given at {self.get_current_time()}")
        await user.send(embed=embed)
        await ctx.send(embed=embed)
        await user.kick(reason=reason)
        await ctx.message.delete()  

    @commands.hybrid_command(name="mute")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user: discord.Member,minutes: int, reason: str = None):
        dalta = timedelta(minutes=minutes)
        embed = discord.Embed(
            title="Punishment Given",
            description=f"{user.mention} **is now Muted of `{dalta}` Minutes**",
            color=discord.Color.red()
        )
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.add_field(name="Banned by", value=f"{ctx.author.mention}", inline= True)
        embed.set_footer(text=f"Punishment given at {self.get_current_time()}")
        await user.send(embed=embed)
        await ctx.send(embed=embed)
        await user.timeout(dalta,reason=reason)
        await ctx.message.delete()  



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower() == "ip":
            response = (
                "# <:up_uniprox_on_top:1232885554501128263> Server Information <:up_uniprox_on_top:1232885554501128263>\n"
                "**<:up_java:1232896732438724709> Java Edition <:up_java:1232896732438724709>**\n"
                "- IP <a:up_arrow:1232897837881360486> `play.uniprox.top`\n\n"
                "**<:up_Bedrock:1232896728328568902> Bedrock/Pocket Edition <:up_Bedrock:1232896728328568902>**\n"
                "- IP <a:up_arrow:1232897837881360486> `pe.uniprox.top`\n"
                "- Port <:portal:1233018239815127100> `19132`"
            )
            await message.channel.send(response,delete_after=30)
        else:
            pattern = re.compile(r'{(.*?)}')
            match = re.search(pattern, message.content)
            if match:
                expression = match.group(1)
                try:
                    result = eval(expression)
                    await message.reply(f'{result}')
                except Exception:
                    pass

async def setup(bot):
    await bot.add_cog(Mod(bot))