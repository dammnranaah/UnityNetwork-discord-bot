from typing import Optional
import discord
from discord.ext import commands, tasks
from discord.interactions import Interaction
import config
from discord import app_commands
import asyncio


message_legend = (
    "**__Legend Rank Information__**\n"
    "**💰 Price:** **350 Taka Only**\n"
    "**🛡️ Kit:** Fully Maxed Diamond Armour, Tools, and other items\n"
    "**🔧 Commands:**\n"
    "/feed - Refill your hunger bar\n"
    "/heal - Refill your hearts\n"
    "/anvil - Use an anvil anywhere\n"
    "/enderchest - Use enderchest anywhere\n"
    "/ecraft - Use crafting table anywhere\n"
    "/sethome name - Teleport to a home that you've previously set\n"
    "/setwarp name - Teleports you to a warp\n"
    "/playtime - Check your playtime anytime\n"
    "/tpa <player> - Teleport to a player\n"
    "/tpr - Teleports you to a random location somewhere in the world\n"
    "Type any color code and then write your text and send for colored chat\n"
    "/eglow color - For an outline in your character\n"
    "/nick - Change your username color\n"
    "/trash - Get rid of useless items easily\n"
    "/msg <player> <message> - Send a private message to a player\n"
    "/r <message> - Reply to your recent message\n"
    "/ignore <player> - Ignore player's messages\n"
    "/suicide - Self-Kill\n"
    "**Chat Formatting:** Ability to use color codes in both nick and chat"
)


message = (
        "**__Immortal Rank Information__**\n"
        "**💰 Price:** **500 Taka Only**\n"
        "**🛡️ Kit:** Fully Maxed Netherite Armour, Tools, and 1 full Shulker Box of potions\n"
        "**🔧 Commands:**\n"
        "__/feed__ - Refill your hunger bar\n"
        "__/heal__ - Refill your hearts\n"
        "__/anvil__ - Use an anvil anywhere\n"
        "__/enderchest__ - Use enderchest anywhere\n"
        "__/ecraft__ - Use crafting table anywhere\n"
        "__/smithingtable__ - Use smithing table anywhere\n"
        "__/stonecutter__ - Use stonecutter anywhere\n"
        "__/rest__ - Makes phantoms not attack you\n"
        "__/sethome__ name - Teleport to a home that you've previously set\n"
        "__/setwarp__ name - Teleports you to a warp\n"
        "__/playtime__ - Check your playtime anytime\n"
        "__/tpa__ <player> - Teleport to a player\n"
        "__/tpr__ - Teleports you to a random location somewhere in the world\n"
        "Type any color code and then write your text and send for colored chat\n"
        "__/trash__ - Get rid of useless items easily\n"
        "__/msg__ <player> <message> - Send a private message to a player\n"
        "__/r__ <message> - Reply to your recent message\n"
        "__/ignore__ <player> - Ignore player's messages\n"
        "__/suicide__ - Self-Kill\n"
        "**Chat Formatting:** Ability to use color codes in both nick and chat"
    )


class Rank(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="Elite",custom_id="elite")
    async def Elite_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Elite Rank Information",
            description="💰 **Price:** **200 Taka Only**\n"
                        "🛡️ **Kit:** Normal Diamond Armour, Tools, and other items\n"
                        "🔧 **Commands:**\n"
                        "/feed - Refill your hunger bar\n"
                        "/heal - Refill your hearts\n"
                        "/anvil - Use an anvil anywhere\n"
                        "/enderchest - Use enderchest anywhere\n"
                        "/tpa <player> - Teleport to a player\n"
                        "/tpr - Teleports you to a random location somewhere in the world\n"
                        "Type any color code and then write your text and send for colored chat\n"
                        "/trash - Get rid of useless items easily\n"
                        "/msg <player> <message> - Send a private message to a player\n"
                        "/r <message> - Reply to your recent message\n"
                        "/ignore <player> - Ignore player's messages\n"
                        "**Chat Formatting:** Ability to use color codes in both nick and chat",
            color=discord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="Legend", custom_id="legend")
    async def legend_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Legend Information",
            description=message_legend,
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed,ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="Immortal",custom_id="immortal")
    async def immortal_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Immortal Information",
            description=message,
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)



class Ranks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="rrr")
    @commands.has_permissions(administrator=True)
    async def rank(self, ctx):
        embed = discord.Embed(
            title="All Information about the Ranks",
            description="**:globe_with_meridians::sparkles: Dominate the Minecraft Server! Unlock Exclusive Ranks Today!** :sparkles::globe_with_meridians:\n\n:rocket: **Elevate Your Gameplay! Choose Your Rank and Dive into Endless Adventures!** :rocket:\n\n:crossed_swords: **Unleash Powerful Perks and Commands! Upgrade Your Gaming Experience!** :crossed_swords:\n\n:gem: **Ready to Rule? Grab Your Desired Rank Now  Just Open the Ticket!** :gem:\n\n:fire: **Click Below to Explore the World of Possibilities and Boost Your Minecraft Journey!** :fire:",
            color=discord.Color.blurple()
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/1195046008745361509/1233005236759564338/standard_2.gif?ex=662b851c&is=662a339c&hm=3885b8ab533d5130be67173f1dda22b58cc8854ecc3f72dbb316de255432f9ef&")
        await ctx.send(embed=embed, view=Rank())

    @app_commands.command(name="order_rank", description=" use to Order a rank")
    @app_commands.choices(rank=[
        app_commands.Choice(name="Elite", value="Elite"),
        app_commands.Choice(name="Legend", value="Legend"),
        app_commands.Choice(name="Immortal", value="Immortal")
    ],payment=[
        app_commands.Choice(name="Bkash", value="Bkash"),
        app_commands.Choice(name="Nagad", value="Nagad")
    ])
    async def order_rank(self, interaction: Interaction, rank: app_commands.Choice[str], payment: app_commands.Choice[str]):
        if rank.value == "Elite":
            if payment.value == "Bkash":
                embed = discord.Embed(
                    title="Elite Rank",
                    description="To buy this it will cost `200 taka` by Bkash",
                    color=discord.Color.blurple()
                )
                embed.add_field(name="Bkash Number", value="```Bkash Not Available in this Time Sorry```", inline=False)
                embed.add_field(name="After payment use `!paid` and send the screen shot", value="", inline=False)
                embed.add_field(name="If your are goribs does  not have a touch mobile open a ticket", value="", inline=False)
                embed.set_footer(text="Payment system by Team UniProx")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            elif payment.value == "Nagad":
                embed = discord.Embed(
                    title="Elite Rank",
                    description="To buy this it will cost `200 taka` by Nagad",
                    color=discord.Color.blurple()
                )
                embed.add_field(name="Nagad Number", value="```01869113329```", inline=False)
                embed.add_field(name="After payment use `!paid` and send the screen shot", value="", inline=False)
                embed.add_field(name="If your are goribs does  not have a touch mobile open a ticket", value="", inline=False)
                embed.set_footer(text="Payment system by Team UniProx")
                await interaction.response.send_message(embed=embed, ephemeral=True)

        elif rank.value == "Legend":
            if payment.value == "Bkash":
                embed = discord.Embed(
                    title="Legend Rank",
                    description="To buy this it will cost `350 taka` by Bkash",
                    color=discord.Color.blurple()
                )
                embed.add_field(name="Bkash Number", value="```Bkash Not Available in this Time Sorry```", inline=False)
                embed.add_field(name="After payment use `!paid` and send the screen shot", value="", inline=False)
                embed.add_field(name="If your are goribs does  not have a touch mobile open a ticket", value="", inline=False)
                embed.set_footer(text="Payment system by Team UniProx")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            elif payment.value == "Nagad":
                embed = discord.Embed(
                    title="Elite Rank",
                    description="To buy this it will cost `350 taka` by Nagad",
                    color=discord.Color.blurple()
                )
                embed.add_field(name="Nagad Number", value="```01869113329```", inline=False)
                embed.add_field(name="After payment use `!paid` and send the screen shot", value="", inline=False)
                embed.add_field(name="If your are goribs does  not have a touch mobile open a ticket", value="", inline=False)
                embed.set_footer(text="Payment system by Team UniProx")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        elif rank.value == "Immortal":
            if payment.value == "Bkash":
                embed = discord.Embed(
                    title="Immortal Rank",
                    description="To buy this it will cost `500 taka` by Bkash",
                    color=discord.Color.blurple()
                )
                embed.add_field(name="Bkash Number", value="```Bkash Not Available in this Time Sorry```", inline=False)
                embed.add_field(name="After payment use `!paid` and send the screen shot", value="", inline=False)
                embed.add_field(name="If your are goribs does  not have a touch mobile open a ticket", value="", inline=False)
                embed.set_footer(text="Payment system by Team UniProx")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            elif payment.value == "Nagad":
                embed = discord.Embed(
                    title="Elite Rank",
                    description="To buy this it will cost `500 taka` by Nagad",
                    color=discord.Color.blurple()
                )
                embed.add_field(name="Nagad Number", value="```01869113329```", inline=False)
                embed.add_field(name="After payment use `p!paid` and send the screen shot", value="", inline=False)
                embed.add_field(name="If your are goribs does  not have a touch mobile open a ticket", value="", inline=False)
                embed.set_footer(text="Payment system by Team UniProx")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("Contact to Team UniProx", ephemeral=True)

    @commands.command(name="paid")
    async def paid(self, ctx, transaction_id: str):
        if ctx.message.attachments:
            for attachment in ctx.message.attachments:
                ch = discord.utils.get(ctx.guild.channels, id=1232999734604726272)
                embed = discord.Embed(title="Payment issued", description=f" Transaction id: ```{transaction_id}```", color=discord.Color.green())
                embed.set_image(url=attachment.url)
                embed.add_field(name="User", value=f"{ctx.author.mention}", inline=False)
                await ch.send(embed=embed)
                embed.set_footer(text="Payment system by Team UniProx")
                await ctx.send("Your payment is under review", delete_after=5)
                await ctx.message.delete()
        else:
            await ctx.send("Please send the screenshot of your payment", delete_after=5)
            await ctx.message.delete()

class CMDD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="issuerank", description=" use to issue a rank")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.choices(rank=[
        app_commands.Choice(name="Elite", value="Elite1"),
        app_commands.Choice(name="Legend", value="Legend2"),
        app_commands.Choice(name="Immortal", value="Immortal3")
    ])
    async def issuerank(self, interaction: Interaction, rank: app_commands.Choice[str], user: discord.Member):
        if rank.value == "Elite1":
            role = discord.utils.get(interaction.guild.roles, id=1226043852721225728)
            await user.add_roles(role)
            embed = discord.Embed(
                title="Thanks for your Donation by buying a Rank",
                description=f"Rank: ```Elite```",
                color=discord.Color.green()
            )
            embed.add_field(name="User", value=f"{user.mention}", inline=False)
            embed.set_footer(text=f"Rank issue by {interaction.user.name}")
            ch = discord.utils.get(interaction.guild.channels, id=config.rank_channel)
            await ch.send(embed=embed)
            await interaction.response.send_message("Rank issued", ephemeral=True)
        elif rank.value == "Legend2":
            role = discord.utils.get(interaction.guild.roles, id=1226043851110875146)
            await user.add_roles(role)
            embed = discord.Embed(
                title="Thanks for your Donation by buying a Rank",
                description=f"Rank: ```Legend```",
                color=discord.Color.green()
            )
            embed.add_field(name="User", value=f"{user.mention}", inline=False)
            embed.set_footer(text=f"Rank issue by {interaction.user.name}")
            ch = discord.utils.get(interaction.guild.channels, id=config.rank_channel)
            await ch.send(embed=embed)
            await interaction.response.send_message("Rank issued", ephemeral=True)
        elif rank.value == "Immortal3":
            role = discord.utils.get(interaction.guild.roles, id=1226043852289343579)
            await user.add_roles(role)
            embed = discord.Embed(
                title="Thanks for your Donation by buying a Rank",
                description=f"Rank: ```Immortal```",
                color=discord.Color.green()
            )
            embed.add_field(name="Buyer", value=f"{user.mention}", inline=False)
            embed.set_footer(text=f"Rank issue by {interaction.user.name}")
            ch = discord.utils.get(interaction.guild.channels, id=config.rank_channel)
            await ch.send(embed=embed)
            await interaction.response.send_message("Rank issued", ephemeral=True)
        else:
            await interaction.response.send_message("Contact to Team UniProx", ephemeral=True)

        

async def setup(bot):
    await bot.add_cog(CMDD(bot))
    await bot.add_cog(Ranks(bot))