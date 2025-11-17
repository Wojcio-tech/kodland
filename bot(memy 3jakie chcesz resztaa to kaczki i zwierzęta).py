import discord
from discord.ext import commands
import os, random
import requests

description = '''Bot z memami i kaczkami.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Dodaje dwie liczby."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    """Wysyła losowy mem z lokalnego folderu."""
    local_memes = ("mem1.jpeg", "mem2.jpeg", "mem3.jpeg")
    chosen_mem = random.choice(local_memes) 

    try:
        with open(chosen_mem, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send(f"Nie mogę znaleźć pliku `{chosen_mem}`. Upewnij się, że jest w tym samym folderze co bot.")

def get_duck_image_url(): 
    """Pobiera URL losowej kaczki z API."""
    url = 'https://random-d.uk/api/random'
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        return data['url']
    except requests.exceptions.RequestException:
        return None

@bot.command('duck')
async def duck(ctx):
    '''Wysyła losowe zdjęcie kaczki.'''
    image_url = get_duck_image_url()
    if image_url:
        await ctx.send(image_url)

def get_random_animal_url():
    apis = {
        'cat': {'url': 'https://api.thecatapi.com/v1/images/search', 'key': 'url', 'is_list': True},
        'dog': {'url': 'https://dog.ceo/api/breeds/image/random', 'key': 'message', 'is_list': False},
        'fox': {'url': 'https://randomfox.ca/floof/', 'key': 'image', 'is_list': False}
    }
    
    max_tries = 5
    for _ in range(max_tries):
        choice = random.choice(list(apis.keys()))
        api_details = apis[choice]
        
        try:
            res = requests.get(api_details['url'])
            res.raise_for_status()
            data = res.json()
            
            if api_details['is_list']:
                if data and isinstance(data, list):
                    return data[0].get(api_details['key'])
            else:
                return data.get(api_details['key'])
                        
        except Exception:
            continue
            
    return None

@bot.command('animal')
async def animal(ctx):
    '''Wysyła losowe zwierzę (kot, pies lub lis).'''
    image_url = get_random_animal_url()
    
    if image_url:
        await ctx.send(image_url)

def get_meme_url():
    """Pobiera URL losowego mema z zewnętrznego API."""
    url = 'https://meme-api.com/v1/gimme'
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        return data.get('url')
    except requests.exceptions.RequestException:
        return None

@bot.command(name='random_mem')
async def random_mem(ctx):
    '''Wysyła losowego mema z Internetu.'''
    meme_url = get_meme_url()
    
    if meme_url:
        await ctx.send(meme_url)

bot.run('TUTAJ_WKLEJ_SWÓJ_TOKEN_BOTA')
