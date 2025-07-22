import discord
from discord.ext import commands

# You'll need to replace "YOUR_BOT_TOKEN" with your actual bot token
TOKEN = "YOUR_BOT_TOKEN"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def message_role(ctx, role: discord.Role, *, message):
    for member in role.members:
        try:
            await member.send(message)
            await ctx.send(f"Sent message to {member.name}")
        except:
            await ctx.send(f"Could not send message to {member.name}")

bot.run(TOKEN)
