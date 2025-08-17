#ANIK IS THE CODDER
import discord 
from discord.ext import commands,tasks
import config
from discord import utils
from cogs.ticket import Ticket_luncher
from cogs.rank import Rank

intents = discord.Intents.all()
intents.message_content = True


bot = commands.Bot(command_prefix="up!", intents=intents,help_command=None)


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(f"Pong! My latency is {round(bot.latency * 1000)}ms.", delete_after=15)
    await ctx.message.delete()


@bot.event
async def on_message(message):
    if message.content == "<@1226042798092845076>":
        await message.reply(f"My prefix is `un!`")

    await bot.process_commands(message)
    
@bot.command(name="sy")
@commands.has_permissions(administrator=True)
async def sync(ctx):
    await bot.tree.sync()
    await ctx.send("SYNC", delete_after=2)
    await ctx.message.delete()

@bot.command(name='rules')
async def rules(ctx):
    embed = discord.Embed(
        title="Community Rules Reminder",
        description="Hey Everyone! 👋\n\nWe want to remind you of our community rules to ensure a positive and respectful environment for all members. Please take a moment to review them:",
        color=discord.Color.green()
    )
    rules = [
        "1. **Be respectful:** Treat everyone with kindness, regardless of age.",
        "2. **No inappropriate language:** Keep it clean and friendly.",
        "3. **Protect privacy:** Never share personal information without permission.",
        "4. **No spam:** Avoid excessive emojis or reactions.",
        "5. **Avoid sensitive topics:** Let's keep the conversation positive.",
        "6. **No personal attacks:** Keep discussions constructive.",
        "7. **No hacking or cheating:** Instant ban for any illegal activity.",
        "8. **Voice channel etiquette:** Minimize background noise for a better experience.",
        "9. **Be modest and polite:** Foster a welcoming atmosphere.",
        "10. **Respect staff decisions:** They are here to maintain order.",
        "11. **Post in the right channels:** Keep things organized.",
        "12. **Constructive criticism:** Share feedback for community improvement.",
        "13. **No advertisements:** Server, Discord, or DM promotions are not allowed.",
        "14. **Rule updates:** Admins may modify rules for community well-being."
    ]

    embed.add_field(name="Community Rules", value='\n'.join(rules), inline=False)
    embed.set_footer(text="Thank you for being part of our community! 🙌")

    await ctx.send(embed=embed)

    
    
activities = [
    discord.Game(name="Use `!help`"),
    discord.Activity(type=discord.ActivityType.watching, name="Proximity Emipre"),
]


@bot.event
async def on_ready():
    cog_list = ["mod","error","wel","sat","ticket","rank","meme","mode"]
    view_list = ['Ticket_luncher','Rank']

    for cog in cog_list:
        try:
            await bot.load_extension(f"cogs.{cog}")
            print(f"Loaded {cog} cog.")
        except Exception as e:
            print(f"Failed to load {cog} cog. Error: {e}")
    for view in view_list:
        try:
            bot.add_view(globals()[view]())
            print(f"Loaded {view} view.")
        except Exception as e:
            print(f"Failed to load {view} view. Error: {e}")

	
    print(
        """
 ____   _____ __     __  ____  __   __  ____      _     _   _     _        _        _     _   _ 
|  _ \ | ____|\ \   / / | __ ) \ \ / / |  _ \    / \   | \ | |   / \      / \      / \   | | | |
| | | ||  _|   \ \ / /  |  _ \  \ V /  | |_) |  / _ \  |  \| |  / _ \    / _ \    / _ \  | |_| |
| |_| || |___   \ V /   | |_) |  | |   |  _ <  / ___ \ | |\  | / ___ \  / ___ \  / ___ \ |  _  |
|____/ |_____|   \_/    |____/   |_|   |_| \_\/_/   \_\|_| \_|/_/   \_\/_/   \_\/_/   \_\|_| |_|
                                                                                                
                                                    """
    )

@tasks.loop(seconds=15)
async def change_activity():
    activities = [
        discord.Game(name="Use `!help`"),
        discord.Activity(type=discord.ActivityType.watching, name="UniProx Network"),
    ]

    activity = activities[change_activity.current_loop % len(activities)]
    await bot.change_presence(activity=activity)


bot.run(config.TOKEN)