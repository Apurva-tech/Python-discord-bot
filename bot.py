from discord.ext import commands
from dotenv import load_dotenv

TOKEN = "#"

bot = commands.Bot(command_prefix='!')

@bot.command(name='faq', help='Searches the FAQ for the most relevant section corresponding to the provided keyword.')
async def faq(ctx, keyword):
    response = keyword
    await ctx.send(response)

def get_qoute():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    msg = message.content
    if message.author == bot.user:
        return
    if 'quote' in msg.lower():
        response = get_qoute()
        await message.channel.send(response)

bot.run(TOKEN)
