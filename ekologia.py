  import discord
from discord.ext import commands
import datetime
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

LIGHT_ON_HOUR = 18   
LIGHT_OFF_HOUR = 23  
@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')
@bot.command()
async def swiatlo(ctx):
    
    await ctx.send(f" Włącz światło o godzinie {LIGHT_ON_HOUR}:00, a wyłącz o {LIGHT_OFF_HOUR}:00.")
@bot.command()
async def teraz(ctx):
    
    now = datetime.datetime.now().hour
    if LIGHT_ON_HOUR <= now < LIGHT_OFF_HOUR:
        await ctx.send("Teraz światło powinno być WŁĄCZONE ")
    else:
        await ctx.send("Teraz światło powinno być WYŁĄCZONE ")

@bot.command()
async def smieci(ctx, rodzaj: str):
    rodzaj = rodzaj.lower()
    if rodzaj in ["papier", "gazeta", "karton"]:
        await ctx.send(" To wrzucamy do NIEBIESKIEGO pojemnika (papier).")
    elif rodzaj in ["butelka plastikowa", "folia", "reklamówka"]:
        await ctx.send(" To wrzucamy do ŻÓŁTEGO pojemnika (plastik i metale).")
    elif rodzaj in ["butelka szklana", "słoik"]:
        await ctx.send(" To wrzucamy do ZIELONEGO pojemnika (szkło).")
    elif rodzaj in ["resztki jedzenia", "skórka od banana", "fus z kawy"]:
        await ctx.send(" To wrzucamy do BRĄZOWEGO pojemnika (bio).")
    elif rodzaj in ["bateria", "żarówka", "lek"]:
        await ctx.send(" To są ODPADY NIEBEZPIECZNE – oddaj do specjalnego punktu zbiórki.")
    else:
        await ctx.send(" Nie jestem pewien – sprawdź lokalne zasady segregacji w Twojej gminie.")
    
