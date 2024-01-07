import disnake
from disnake.ext import commands
import os


intents = disnake.Intents.all()

activity = disnake.Activity(
    name="сервер proknulo",
    type=disnake.ActivityType.streaming,
    url="https://www.twitch.tv/discord"
)
bot = commands.Bot(command_prefix='.', intents=intents, activity=activity)

@bot.event
async def on_ready():
    print("Bot is ready, bro!")


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")




@bot.slash_command()
async def command(interaction):
    await interaction.response.send_message("дайте значок,суки")

bot.run('MTEyOTgwOTg2OTM4MjM2MTE1OA.GJn0CO.oCbyu3oWq6ii_8kgZsGWlmF_5MZO6nawtCF8bA')