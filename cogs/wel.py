import discord
from discord.ext import commands


class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="test")
    async def test(self, ctx, user: discord.Member):
        self.bot.dispatch("member_join", user)
        return await ctx.send("sent")
    
    @commands.Cog.listener()
    async def on_member_join(self, member): 
        channel = member.guild.get_channel(1226034701496619019)
        role = member.guild.get_role(1226043856336715896)
        
        embed = discord.Embed(
            description=(
                "# Welcome to UniProx Network\n"
                f"〢{member.mention}\n\n"
                "❉⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
                "**Check:**\n"
                "✎ https://discord.com/channels/1225988829811572817/1226034701496619019\n"
                "✎ https://discord.com/channels/1225988829811572817/1226039620794581063\n"
                "✎ https://discord.com/channels/1225988829811572817/1226047789658804325\n"
                "✎ https://discord.com/channels/1225988829811572817/1226047273449033748\n"
                "✎ https://discord.com/channels/1225988829811572817/1230037288411594752\n"
                "✎ https://discord.com/channels/1225988829811572817/1230510265116917770\n"
                "✎ https://discord.com/channels/1225988829811572817/1226757347767091231\n"
                "✎ https://discord.com/channels/1225988829811572817/1226042535206715433\n"
                "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯❉\n\n"
                "**Thanks for being with us on UniProx Network**"
            )
        )
        
        embed.set_image(url="https://cdn.discordapp.com/attachments/1230462871054581760/1232634166219247626/standard_1.gif?ex=662a2b86&is=6628da06&hm=d6729ee7a656fcbefef091ddde174c4862cff951e8c00d4374e0c9da0a1f6275&")
        
        await channel.send(embed=embed)
        await member.add_roles(role)

async def setup(bot):
    await bot.add_cog(WelcomeCog(bot))