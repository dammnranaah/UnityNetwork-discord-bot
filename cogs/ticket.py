import discord
from discord.ext import commands
import os
from datetime import datetime
import pytz
import chat_exporter
import mysql.connector
import config

def connect_to_database():
    return mysql.connector.connect(
        host="datacenter.nexusportal.xyz",
        user="u53_V9ZF9UJ1rA",
        password="o@fP=m9j@zk9fSer95Y2.wt8",
        database="s53_ticket",
        port=3306,
        autocommit=True
    )



class TT(discord.ui.Modal, title="Ticket submission"):
    name = discord.ui.TextInput(label="Name of service", style=discord.TextStyle.short)
    reason = discord.ui.TextInput(label="Reason", placeholder="Provide your review", max_length=100, style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        
        category_id = config.category_id
        msg = await interaction.response.send_message(content="Creating ticket...", ephemeral=True)

        category = discord.utils.get(interaction.guild.categories, id=category_id)
        if category is None:
            await interaction.response.send_message("Category not found. Please contact the bot owner.", ephemeral=True)
            return

        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True, attach_files=True),
            interaction.guild.get_role(config.ticket_manager): discord.PermissionOverwrite(view_channel=True, send_messages=True, attach_files=True)
        }

        ch = await category.create_text_channel(name=f"ticket - {interaction.user.name}", overwrites=overwrites)
        ch_id = ch.id
        embed = discord.Embed(
            title="New Ticket",
            description=
                f"**Hello {interaction.user.mention},**\n\n"

                "🌟 **Thank you for reaching out to us!** Your ticket has been successfully created under the category **{self.name.value}**. Our dedicated ticket management team has been notified and will get back to you as soon as possible.\n\n"

                "🚀 **Please be patient and refrain from pinging anyone.** We understand the importance of your concern, and we assure you that it will be addressed promptly.\n\n"

                "📚 **In the meantime, here are a few tips:**\n"
                "- Ensure that you've provided all necessary details in your initial message.\n"
                "- Avoid creating multiple tickets for the same issue to streamline the resolution process.\n"
                "- If there are any updates or additional information, feel free to add them to this channel.\n\n"

                "<:JEmoji_Checked:1194679506745708595> **Once again, thank you for choosing us. We appreciate your patience and cooperation.**\n\n"

                "**Best regards**\n"
                "Proximity Empire\n"
                "Management Team\n",
                color=discord.Color.blurple()    
        )
        
        embed.add_field(name="Service name", value=f"```{self.name.value}```", inline=False)
        embed.add_field(name="Reason", value=f"```{self.reason.value}```", inline=False)
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar)
        user_timezone = "Asia/Dhaka"
        utc_time = datetime.utcnow()
        local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(user_timezone))
        formatted_time = local_time.strftime('%Y-%m-%d %I:%M:%S %p')
        embed.set_footer(text=f"📅Ticket Submited on {formatted_time}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1181457743761121300/d97539a18976b625bf26b5f642e1566c.png?size=1024")
        db = connect_to_database()
        cursor = db.cursor(dictionary=True)
        cursor.execute("INSERT INTO ticket (channel_id, user_id) VALUES (%s, %s)", (ch_id, interaction.user.id))
        

        await ch.send("**Please wait here. <@1203020780590469191> will contact you as soon as possible.**", embed=embed)


class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ticket")
    async def ticket(self, ctx):
        embed = discord.Embed(
            title="Need Support Or Want to Buy A Rank",
            description=(
            "# 🌟 Hello there! Having trouble? Looking for help? Want to buy ranks?\n\n"

            "**Support tickets are the best way to get in contact with our staff teams.**\n"
            "**A Support ticket can be opened for any kind of issues.**\n"
            "**Remember our staff team will try their best to get your issues resolved as soon possible."
            "And you can also open ticket for buy any rank.**\n\n"

            "- General Support\n"
            "- Hackers Report\n"
            "- Unban Appeal\n"
            "- Reset Password\n"
            "- Rank Purachase\n"
            "-  Staff Report\n\n"

            "⏰ Our ticket management team will try to reply as fast as possible in each ticket,\n"
            "so please don't ping any staffs." 
        ),
            color=discord.Color.dark_gold()
        )
        embed.set_footer(text="Fun Ticket = Ban\nCOPYRIGHT BY Unity Network")
        await ctx.send(embed=embed, view=Ticket_luncher())



    async def cog_check(self, ctx):
        return ctx.guild is not None

    async def close_ticket(self, ctx, reason):
        channel = ctx.channel
        filename = f"{channel.id}.html"

        export = await chat_exporter.export(channel=channel)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(export)

        db = connect_to_database()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM ticket WHERE channel_id = %s", (channel.id,))
        result = cursor.fetchone()

        if result:
            user_id = result["user_id"]
            ticket_opener = ctx.guild.get_member(user_id)

            if ticket_opener is None:
                ticket_opener = await ctx.guild.fetch_member(user_id)

            if ticket_opener:
                try:
                    embed = discord.Embed(
                        title=f"Ticket closed - {channel.name}",
                        description=f"closed by {ctx.author.name}",
                        color=discord.Color.blurple()
                    )
                    embed.add_field(name="Reason", value=f"{reason}", inline=False)
                    await ticket_opener.send(embed=embed,file=discord.File(filename))
                except discord.Forbidden:
                    await ctx.send(f"I can not dm {ticket_opener.mention}, DMs are closed for them.")
                else:
                    log_channel_id = config.log_channel_id
                    log_channel = self.bot.get_channel(log_channel_id)

                    if log_channel:
                        await log_channel.send(f"Ticket closed. Here are the logs for {ticket_opener.mention}\n Closed by {ctx.author.name}\n Reason: {reason}", file=discord.File(filename))
                    else:
                        await ctx.send("Log channel missing")

                    await ctx.send(f"{ticket_opener.mention} Ticket closed successfully<:done:1188698272840306809>")
                finally:
                    cursor.execute("DELETE FROM ticket WHERE channel_id = %s", (channel.id,))
                    cursor.execute("DELETE FROM ticket WHERE user_id = %s", (user_id,))
                    await ctx.channel.delete()
                    os.remove(filename)
                    cursor.close()
            else:
                await ctx.send("User not found.")
        else:
            await ctx.send("No ticket found for the specified channel ID.")

    @commands.command(name="close", description="Only used for ticket")
    @commands.has_permissions(administrator=True)
    async def close_command(self, ctx, *, reason: str = "No reason given"):
        category_ids = {config.category_id}
        channel = ctx.channel

        if channel.category_id in category_ids:
            await self.close_ticket(ctx, reason)
        else:
            await ctx.send("Invalid category. Make sure to run this command in a ticket channel.")



    @commands.command(name="adduser")
    @commands.has_permissions(administrator=True)
    async def adduser(self, ctx, user: discord.Member):
        try:
            ch = ctx.channel
            await ch.set_permissions(user, read_messages=True, send_messages=True,view_channel=True)
            await ctx.send(f"{user.display_name} added successfully")
            await ctx.message.delete()
        except ValueError:
            await ctx.send("Invalid user")

    @commands.command(name="removeuser")
    @commands.has_permissions(administrator=True)
    async def removeuser(self, ctx, user: discord.Member):
        try:
            ch = ctx.channel
            await ch.set_permissions(user, read_messages=False, send_messages=False,view_channel=False)
            await ctx.send(f"{user.display_name} removed successfully")
            await ctx.message.delete()
        except ValueError:
            await ctx.send("Invalid user")


class Ticket_luncher(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.blurple, custom_id="ticket_button", emoji="🎫")
    async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        db = connect_to_database()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT user_id FROM ticket WHERE user_id = %s", (interaction.user.id,))
        result = cursor.fetchone()
        if result:
            await interaction.response.send_message("You already have an active ticket. Please wait for it to be resolved before opening a new one.", ephemeral=True)
            return
        else:
            await interaction.response.send_modal(TT())


async def setup(bot):
    await bot.add_cog(Ticket(bot))