import discord
from discord.ext import commands
import random
import os
import requests
import asyncio

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def eightball(ctx, *, question: str):
    """Ask the magic 8-ball a question."""
    responses = ['Yes', 'No', 'Maybe', 'Ask again later', 'Definitely']
    await ctx.send(f'🎱 {random.choice(responses)}')

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    with open('images/'+random.choice(images), 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def animal(ctx):
    animals = os.listdir('animals')
    with open('animals/'+random.choice(animals), 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('timer')
async def timer(ctx, seconds):
    await ctx.send(f'Okay I will tell you to throw your trash in {seconds} seconds!')
    await asyncio.sleep(int(seconds))
    await ctx.send(f'Throw your trash!')

@bot.command('advice')
async def advice(ctx):
    advices = ['Empty and clean your containers', 'Purchase recycled items', 'Recycling at workplace', 'Avoid some materials', 'Compost your food scraps', 'Keep recyclables loose', 'Know your plastics', 'Reduce and reuse', 'Source seperate with multiple bins']
    await ctx.send(f'{random.choice(advices)}')

@bot.command('guideline')
async def guideline(ctx):
    await ctx.send('$add [a] [b] = Adds a + b.\n'
                   '$roll aDb = Rolls an aDb dice (example: 2d6).\n'
                   '$choose [a] [b] = Picks between A or B.\n'
                   '$repeat [a] [b] = Repeats A, B times.\n'
                   '$joined [a] = Shows when A joined.\n'
                   '$cool [a] = Checks if A is cool.\n'
                   '$hello = Bot says hello.\n'
                   '$heh [b] = Bot sends "he" B times.\n'
                   '$eightball [a] = Magic 8-ball answer.\n'
                   '$mem = Random meme is sent.\n'
                   '$animal = Random animal picture.\n'
                   '$timer [a] = Sets a timer to throw trash for A seconds.\n'
                   '$advice = Sends a random advice for recycling.\n')

bot.run(token)
