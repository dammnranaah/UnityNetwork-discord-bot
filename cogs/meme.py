import os
import json
import random
import discord
from discord.ext import commands, tasks

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.images_folder = "images"
        self.target_channel_id = 1227595962961231913 
        self.send_meme.start()

    def cog_unload(self):
        self.send_meme.cancel()

    @tasks.loop(hours=1)
    async def send_meme(self):
        channel_id = self.target_channel_id
        if channel_id:
            if not os.path.exists(self.images_folder):
                print("The 'images' folder does not exist.")
                return

            image_files = [f for f in os.listdir(self.images_folder) if os.path.isfile(os.path.join(self.images_folder, f))]

            if not image_files:
                print("No images found in the 'images' folder.")
                return

            random_image = os.path.join(self.images_folder, random.choice(image_files))

            channel = self.bot.get_channel(channel_id)

            if channel:
                await channel.send(file=discord.File(random_image))
            else:
                print(f"Error: Channel with ID '{channel_id}' not found.")
        else:
            print("Error: Channel ID not set in the configuration.")

    @send_meme.before_loop
    async def before_send_meme(self):
        await self.bot.wait_until_ready()





async def setup(bot):
    await bot.add_cog(Meme(bot))