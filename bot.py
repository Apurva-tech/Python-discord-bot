from discord.ext import commands
from dotenv import load_dotenv

TOKEN = "#"

bot = commands.Bot(command_prefix='!')

@bot.command(name='faq', help='Searches the FAQ for the most relevant section corresponding to the provided keyword.')
async def faq(ctx, keyword):
    response = keyword
    await ctx.send(response)

bot.run(TOKEN)
