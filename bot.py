from discord.ext import commands
import random

TOKEN = "#"

bot = commands.Bot(command_prefix='!')

@bot.command(name='faq', help='Searches the FAQ for the most relevant section corresponding to the provided keyword.')
async def faq(ctx, keyword):
    response = keyword
    await ctx.send(response)

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  mssg = ['hi', 'hello', 'hey']

  if message.content.lower().startswith(tuple(mssg)):
    greetings = ['Hey! How are you?', 'Hello! Glad to see you.']
    await message.channel.send(random.choice(greetings))

bot.run(TOKEN)